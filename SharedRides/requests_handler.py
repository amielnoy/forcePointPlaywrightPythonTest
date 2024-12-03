import csv
from ride import RideRequest


class RequestHandler:
    request_list = []


class RequestFromCSV(RequestHandler):
    def read_request_from_csv(self, requests_csv: str):
        with open(requests_csv, 'r') as file:
            try:
                reader = csv.reader(file)
                for row in reader:
                    company, dest, rides = row
                    self.request_list.append(RideRequest(
                        company_name=company.strip(),
                        destination=dest.strip(),
                        number_of_rides_requested=int(rides)
                    ))

            except FileNotFoundError:
                print("File: "f'{requests_csv}' " doesn’t exist")

        return self.request_list
