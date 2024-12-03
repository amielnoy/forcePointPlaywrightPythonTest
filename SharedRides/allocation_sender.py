import csv
from typing import List
from ride import RideAllocation


class AllocationSender:
    def allocation_to_csv(self, allocations: List[RideAllocation], output_csv: str):
        with open(output_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            for alloc in allocations:
                writer.writerow([
                    alloc.company_name,
                    alloc.destination,
                    alloc.number_of_rides_approved
                ])
