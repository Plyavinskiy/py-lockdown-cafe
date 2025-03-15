from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, object]) -> str:
        vaccine_info = visitor.get("vaccine")

        if not isinstance(vaccine_info, dict):
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = vaccine_info.get("expiration_date")

        if not isinstance(expiration_date, date):
            raise OutdatedVaccineError("Invalid vaccine expiration date.")
        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine has expired.")

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
