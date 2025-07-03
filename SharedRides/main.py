from typing import Dict
from ride import RideRequest, RideAllocation
from requests_handler import RequestHandler, RequestFromCSV
from aggregate_requests import AggregateRequests
from request_sender import RequestSender
from ride_distribute import DistributToCustomers
from allocation_sender import AllocationSender

from pathlib import Path


class RideAllocationSystem:
    def __init__(self):
        self.request = RequestFromCSV()
        self.aggregate_requests = AggregateRequests()
        self.request_send = RequestSender()
        self.ride_distribute = DistributToCustomers()
        self.send_allocation = AllocationSender()

    def get_current_directory(self):
        return Path.cwd()
    def process_ride_requests(self, agency: str, input_file: str, output_file: str):
        # Read requests from CSV
        # current_directory = self.get_current_directory()
        # print(f"Current Directory: {current_directory}")
        # input_file =  str(current_directory) + '/' +  'csv_inputs/input.csv'

        requests = self.request.read_request_from_csv(input_file)

        # Aggregate by destination
        aggregated = self.aggregate_requests.aggregate_by_destination(requests)

        # Request rides from external service
        approved_rides = self.request_send.send_request(agency, aggregated)

        # Distribute rides to companies
        allocations = self.ride_distribute.distribute_rides(requests, approved_rides)

        # Write allocations to CSV
        self.send_allocation.allocation_to_csv(allocations, output_file)


def main():
    system = RideAllocationSystem()
    current_directory = system.get_current_directory()
    print(f"Current Directory: {current_directory}")
    input_file = str(current_directory) + '/' + 'csv_inputs/input.csv'
    system.process_ride_requests("agency",input_file, "output.csv")


if __name__ == "__main__":
    main()
