from typing import Dict, List, Tuple
from ride import RideRequest, RideAllocation
import math


class DistributToCustomers:
    def distribute_rides(self, requests: List[RideRequest], approved_rides: Dict[str, int]) -> List[RideAllocation]:
        """Distribute approved rides to companies"""
        final_allocations = []

        # Groups ride requests by destination
        dest_requests = self.group_requests_by_destination(requests)

        # Process each destination
        for dest, dest_approved_rides in approved_rides.items():
            if dest not in dest_requests:
                continue
            companies_in_dest = dest_requests[dest]
            dest_allocations = self.calculate_per_destination(companies_in_dest, dest_approved_rides)
            final_allocations.extend(dest_allocations)
        return final_allocations

    def group_requests_by_destination(self, requests: List[RideRequest]) -> Dict[str, List[RideRequest]]:
        """Groups ride requests by destination"""
        dest_requests = {}
        for req in requests:
            if req.destination not in dest_requests:
                dest_requests[req.destination] = []
            dest_requests[req.destination].append(req)
        return dest_requests

    def calculate_per_destination(self, companies: List[RideRequest], available_rides: int) -> List[RideAllocation]:
        """Calculates rides distribution for single destination """
        # Calculate initial proportional allocation
        company_allocations, remaining_rides = self.initial_allocation(companies, available_rides)

        # Distribute remaining rides
        final_allocations = self.distribute_remaining_rides(companies, company_allocations, remaining_rides)

        # Convert to RideAllocation objects
        return self.create_ride_allocation_objects(companies, final_allocations)

    def initial_allocation(self, companies: List[RideRequest], available_rides: int) -> Tuple[List[int], int]:
        """Calculate allocation, rounded to number of seats."""
        total_requested = sum(req.number_of_rides_requested for req in companies)
        remaining_rides = available_rides
        company_allocations = []
        for req in companies:
            proportion = req.number_of_rides_requested / total_requested
            raw_allocation = proportion * available_rides
            allocation = min(
                math.floor(raw_allocation / 100) * 100,
                req.number_of_rides_requested
            )
            company_allocations.append(allocation)
            remaining_rides -= allocation
        return company_allocations, remaining_rides

    def distribute_remaining_rides(self,
                                   companies: List[RideRequest],
                                   current_allocations: List[int],
                                   remaining_rides: int
                                   ) -> List[int]:
        """Distributes remaining rides based on gap."""
        allocations = current_allocations.copy()

        while remaining_rides >= 100:
            seats_for_distribute = 100 if remaining_rides >= 100 else remaining_rides
            company_index = self.max_gap_company(companies, allocations, seats_for_distribute)
            if company_index == -1:
                break
            allocations[company_index] += remaining_rides
            remaining_rides -= remaining_rides
        return allocations

    def max_gap_company(
            self,
            companies: List[RideRequest],
            current_allocations: List[int],
            seats_for_distribute=100
    ) -> int:
        """Finds the company with the largest gap that can accept more rides."""
        max_gap = -1
        max_gap_idx = -1

        for i, req in enumerate(companies):
            current_allocation = current_allocations[i]
            if current_allocation + seats_for_distribute <= req.number_of_rides_requested:
                gap = self.calculate_gap_ratio(req.number_of_rides_requested, current_allocation)
                if gap > max_gap:
                    max_gap = gap
                    max_gap_idx = i
        return max_gap_idx

    def calculate_gap_ratio(self, requested: int, allocated: int) -> float:
        """Calculates the gap ratio for a company."""
        return (requested - allocated) / requested

    def create_ride_allocation_objects(self, companies: List[RideRequest], allocations: List[int]) -> List[RideAllocation]:
        """Creates RideAllocation objects from allocations."""
        partial_allocations = []
        for req, allocation in zip(companies, allocations):
            if allocation > 0:
                partial_allocations.append(RideAllocation(
                    company_name=req.company_name,
                    destination=req.destination,
                    number_of_rides_approved=allocation
                ))
        return partial_allocations
