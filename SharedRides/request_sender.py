import requests
from typing import Dict


class RequestSender:
    def send_request(self, agency_name, request_rides) -> Dict[str, int]:

        # Demonstrate request to  external transit agency
        response = requests.post(endpoint, headers=auth_header, json=request_rides, timeout=time_out)
        return approved_rides
