from dataclasses import dataclass


@dataclass
class TransitAgency:
    agency_name: str
    seats: str


class AgencyA(TransitAgency):
    agency_name = "aaa"
    seats = 100
