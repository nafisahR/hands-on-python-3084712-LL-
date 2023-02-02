import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

#convert Einstein_csv to Einstein
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
# open the CSV file to read (r) and assigned to variable (f))
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

#for loop variable (laureate) reads through the entire csv file
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
