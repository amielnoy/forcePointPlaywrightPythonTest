from dataclasses import dataclass
from agencies import AgencyA


@dataclass
class RideRequest:
    company_name: str
    destination: str
    number_of_rides_requested: int

    def __post_init__(self):
        if self.number_of_rides_requested % AgencyA.seats != 0:
            raise ValueError("Rides requested must be a multiple of" f'{AgencyA.seats}')
        if self.number_of_rides_requested <= 0:
            raise ValueError("Rides requested must be positive")


@dataclass
class RideAllocation:
    company_name: str
    destination: str
    number_of_rides_approved: int

    def __post_init__(self):
        if self.number_of_rides_approved < 0:
            raise ValueError("Rides approved cannot be negative")
