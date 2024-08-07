# Standard Library
import json
from datetime import datetime

# Django Stuff
from django.db import transaction

# Local Folder
from .models import Aircraft, Flight


def import_data(file_path):
    batch_size = 1000

    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
        unescaped_content = file_content.encode().decode("unicode_escape")

        data = json.loads(unescaped_content)

        aircraft_batch = []
        flight_batch = []

        def parse_time(value):
            if value is not None:
                if isinstance(value, int):
                    if value == 0:
                        return None
                    value = str(value).zfill(4)
                try:
                    return datetime.strptime(value, "%H%M").time()
                except ValueError:
                    return None
            return None

        for entry in data:
            modified_datetime = datetime.fromtimestamp(entry["_modified"])

            if entry["table"] == "Aircraft":
                aircraft = Aircraft(
                    guid=entry["guid"],
                    user_id=entry["user_id"],
                    make=entry["meta"].get("Make", ""),
                    model=entry["meta"].get("Model", ""),
                    reference=entry["meta"].get("Reference", ""),
                    modified=modified_datetime,
                    equipment_type=entry["meta"].get("EquipmentType", ""),
                    type_code=entry["meta"].get("TypeCode", ""),
                    year=entry["meta"].get("Year", ""),
                    category=entry["meta"].get("Category", ""),
                    aircraft_class=entry["meta"].get("Class", ""),
                    gear_type=entry["meta"].get("GearType", ""),
                    engine_type=entry["meta"].get("EngineType", ""),
                    complex=entry["meta"].get("Complex", False),
                    high_performance=entry["meta"].get("HighPerformance", False),
                    pressurized=entry["meta"].get("Pressurized", False),
                    taa=entry["meta"].get("TAA", False),
                )

                aircraft_batch.append(aircraft)

                if len(aircraft_batch) >= batch_size:
                    with transaction.atomic():
                        Aircraft.objects.bulk_create(
                            aircraft_batch, ignore_conflicts=True
                        )
                    aircraft_batch = []

            elif entry["table"] == "Flight":
                date_utc = datetime.strptime(
                    entry["meta"]["DateUTC"], "%Y-%m-%d"
                ).date()
                date_base = datetime.strptime(
                    entry["meta"]["DateBASE"], "%Y-%m-%d"
                ).date()
                date_local = datetime.strptime(
                    entry["meta"]["DateLOCAL"], "%Y-%m-%d"
                ).date()

                flight = Flight(
                    guid=entry["guid"],
                    user_id=entry["user_id"],
                    date_utc=date_utc,
                    date_base=date_base,
                    date_local=date_local,
                    remarks=entry["meta"].get("Remarks", ""),
                    modified=modified_datetime,
                    from_airport=entry["meta"].get("DepCode", ""),
                    to_airport=entry["meta"].get("ArrCode", ""),
                    route=entry["meta"].get("Route", ""),
                    time_out=parse_time(entry["meta"].get("DepTimeUTC")),
                    time_off=parse_time(entry["meta"].get("ToTimeUTC")),
                    time_on=parse_time(entry["meta"].get("LdgTimeUTC")),
                    time_in=parse_time(entry["meta"].get("ArrTimeUTC")),
                    on_duty=parse_time(entry["meta"].get("OnDuty")),
                    off_duty=parse_time(entry["meta"].get("OffDuty")),
                    total_time=entry["meta"].get("minTOTAL", 0),
                    pic=entry["meta"].get("minPIC", 0),
                    sic=entry["meta"].get("minCOP", 0),
                    night=entry["meta"].get("minNIGHT", 0),
                    solo=entry["meta"].get("minSOLO", 0),
                    cross_country=entry["meta"].get("minXC", 0),
                    nvg=entry["meta"].get("minNVG", 0),
                    nvg_ops=entry["meta"].get("minNVGOps", 0),
                    distance=entry["meta"].get("Distance", 0),
                    day_takeoffs=entry["meta"].get("DayTakeoffs", 0),
                    day_landings_full_stop=entry["meta"].get("DayLandingsFullStop", 0),
                    night_takeoffs=entry["meta"].get("NightTakeoffs", 0),
                    night_landings_full_stop=entry["meta"].get(
                        "NightLandingsFullStop", 0
                    ),
                    all_landings=entry["meta"].get("AllLandings", 0),
                    actual_instrument=entry["meta"].get("ActualInstrument", 0),
                    simulated_instrument=entry["meta"].get("SimulatedInstrument", 0),
                    hobbs_start=entry["meta"].get("HobbsStart", 0),
                    hobbs_end=entry["meta"].get("HobbsEnd", 0),
                    tach_start=entry["meta"].get("TachStart", 0),
                    tach_end=entry["meta"].get("TachEnd", 0),
                    holds=entry["meta"].get("Holds", 0),
                    approach1=entry["meta"].get("Approach1", ""),
                    approach2=entry["meta"].get("Approach2", ""),
                    approach3=entry["meta"].get("Approach3", ""),
                    approach4=entry["meta"].get("Approach4", ""),
                    approach5=entry["meta"].get("Approach5", ""),
                    approach6=entry["meta"].get("Approach6", ""),
                    dual_given=entry["meta"].get("DualGiven", 0),
                    dual_received=entry["meta"].get("DualReceived", 0),
                    simulated_flight=entry["meta"].get("SimulatedFlight", 0),
                    ground_training=entry["meta"].get("GroundTraining", 0),
                    instructor_name=entry["meta"].get("InstructorName", ""),
                    instructor_comments=entry["meta"].get("InstructorComments", ""),
                    person1=entry["meta"].get("Person1", ""),
                    person2=entry["meta"].get("Person2", ""),
                    person3=entry["meta"].get("Person3", ""),
                    person4=entry["meta"].get("Person4", ""),
                    person5=entry["meta"].get("Person5", ""),
                    person6=entry["meta"].get("Person6", ""),
                    flight_review=entry["meta"].get("FlightReview", False),
                    checkride=entry["meta"].get("Checkride", False),
                    ipc=entry["meta"].get("IPC", False),
                    nvg_proficiency=entry["meta"].get("NVGProficiency", False),
                    faa6158=entry["meta"].get("FAA6158", False),
                    custom_text=entry["meta"].get("CustomText", ""),
                    custom_numeric=entry["meta"].get("CustomNumeric", 0),
                    custom_hours=entry["meta"].get("CustomHours", 0),
                    custom_counter=entry["meta"].get("CustomCounter", 0),
                    custom_date=datetime.strptime(
                        entry["meta"].get("CustomDate", ""), "%Y-%m-%d"
                    ).date()
                    if entry["meta"].get("CustomDate")
                    else None,
                    custom_datetime=datetime.strptime(
                        entry["meta"].get("CustomDateTime", ""), "%Y-%m-%dT%H:%M:%S"
                    )
                    if entry["meta"].get("CustomDateTime")
                    else None,
                    custom_toggle=entry["meta"].get("CustomToggle", False),
                    pilot_comments=entry["meta"].get("PilotComments", ""),
                )

                flight_batch.append(flight)

                if len(flight_batch) >= batch_size:
                    with transaction.atomic():
                        Flight.objects.bulk_create(flight_batch, ignore_conflicts=True)
                    flight_batch = []

        if aircraft_batch:
            with transaction.atomic():
                Aircraft.objects.bulk_create(aircraft_batch, ignore_conflicts=True)

        if flight_batch:
            with transaction.atomic():
                Flight.objects.bulk_create(flight_batch, ignore_conflicts=True)
