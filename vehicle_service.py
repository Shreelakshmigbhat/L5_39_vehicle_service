"""Manage vehicle service bookings and service records."""

import hashlib
import json
import shutil
from datetime import date
from pathlib import Path

SERVICE_RATES = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "General": 2500,
    "Brake Check": 1200,
}

SERVICE_RECORDS = {}


def add_service(vehicle_no, service_type="General", history=None):
    """Add a service job for a vehicle."""
    if history is None:
        history = []

    cost = SERVICE_RATES.get(service_type, 0)
    entry = {
        "type": service_type,
        "cost": cost,
        "date": str(date.today()),
    }

    SERVICE_RECORDS.setdefault(vehicle_no, []).append(entry)
    history.append(vehicle_no)
    return history


def cancel_service(vehicle_no, service_type):
    """Cancel all jobs of the specified type for a vehicle."""
    jobs = SERVICE_RECORDS.get(vehicle_no)

    if jobs is None:
        print("No records for", vehicle_no)
        return False

    remaining = [
        job for job in jobs
        if job["type"] != service_type
    ]

    SERVICE_RECORDS[vehicle_no] = remaining
    return len(remaining) < len(jobs)


def get_total_cost(vehicle_no):
    """Calculate the total service cost for a vehicle."""
    return sum(
        job["cost"]
        for job in SERVICE_RECORDS.get(vehicle_no, [])
    )


def job_card_id(vehicle_no):
    """Generate a short job card identifier."""
    vehicle_hash = hashlib.sha256(
        vehicle_no.encode("utf-8")
    ).hexdigest()
    return vehicle_hash[:8]


def busiest_vehicle():
    """Return the vehicle with the most service jobs."""
    if not SERVICE_RECORDS:
        return None

    return max(
        SERVICE_RECORDS,
        key=lambda vehicle: len(SERVICE_RECORDS[vehicle]),
    )


def save_records(file_name="services.json"):
    """Save service records to a JSON file."""
    with open(
        file_name, "w", encoding="utf-8"
    ) as records_file:
        json.dump(SERVICE_RECORDS, records_file, indent=2)


def load_records(file_name="services.json"):
    """Load service records from a JSON file."""
    with open(
        file_name, encoding="utf-8"
    ) as records_file:
        return json.load(records_file)


def backup_records(folder):
    """Back up the JSON records without executing a shell command."""
    source = Path("services.json")
    destination_folder = Path(folder)
    destination_folder.mkdir(parents=True, exist_ok=True)

    shutil.copy2(
        source,
        destination_folder / source.name,
    )


def main():
    """Run the vehicle service demonstration."""
    add_service("KA01AB1234", "Oil Change")
    add_service("KA01AB1234", "Wheel Alignment")
    add_service("KA05XY9876")
    add_service("KA03MN4455", "Brake Check")

    cancel_service("KA05XY9876", "Brake Check")
    cancel_service("KA09ZZ0001", "General")
    cancel_service("KA03MN4455", "Brake Check")

    print(
        "Total for KA01AB1234:",
        get_total_cost("KA01AB1234"),
    )
    print(
        "Total for KA05XY9876:",
        get_total_cost("KA05XY9876"),
    )
    print(
        "Job card for KA01AB1234:",
        job_card_id("KA01AB1234"),
    )

    save_records()
    loaded = load_records()

    print(
        "Vehicles on file:",
        len(loaded),
        "| busiest vehicle:",
        busiest_vehicle(),
    )


if __name__ == "__main__":
    main()
