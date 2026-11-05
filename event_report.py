import json
from pathlib import Path
import csv

def calculate_price(guest, price_per_plate):
    discount = False
    total = guest*price_per_plate
    if guest > 500:
        discount = True
        total = total * 0.9

    return total, discount


def_dir = Path(__file__).resolve().parent

event_path = def_dir / "events.csv"
report_path = def_dir / "report.json"
try:
    with open (event_path, newline="") as f:
        events = csv.DictReader(f)
        grand_total = 0
        valid_events = []
        invalid_events = []
        for row in events:
            try:
                if int(row["guests"]) <= 0:
                    invalid_events.append(row["event"])
                    continue
                else:
                    result = calculate_price(int(row["guests"]), int(row["price_per_plate"]))
                    print(f"{row["event"]} costs {result[0]}")
                    grand_total = grand_total + result[0]
                    valid_events.append({"Event": row["event"], "Guests": int(row["guests"]),"Cost": result[0], "Discount Applied": result[1]})
            except ValueError:
                invalid_events.append(row["event"])
                continue
except FileNotFoundError:
    print (f"Events File Not Found")
    exit(1)


for event in invalid_events:
    print(f"{event} is skipped")

print(f"Grand Total is {grand_total}")

with open (report_path, "w") as f:
    json.dump(valid_events, f, indent=2)