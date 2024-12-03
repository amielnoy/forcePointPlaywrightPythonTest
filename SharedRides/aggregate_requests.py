from typing import Dict, List
from collections import defaultdict
from ride import RideRequest


class AggregateRequests:
    def aggregate_by_destination(self, requests: List[RideRequest]) -> Dict[str, int]:
        """Create a dict for total requested rides per destination"""
        requests_dict = defaultdict(int)
        for e in requests:
            requests_dict[e.destination] += e.number_of_rides_requested

        return requests_dict
