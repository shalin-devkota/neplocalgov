import csv
import json


def by_province(province=None):
    result = []
    with open("src/data/data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Province"] == province:
                result.append(row)

    return result


def by_district(district=None):
    result = []
    with open("src/data/data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["District"] == district.upper():
                result.append(row)
    print(result)
    return result


print(by_district(district="Kathmandu"))
