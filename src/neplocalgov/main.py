import csv
import importlib.resources as pkg_resources


def get_csv_file_path():
    with pkg_resources.path("neplocalgov", "data.csv") as p:
        return str(p)


csv_file_path = get_csv_file_path()


def by_province(province=None):
    result = []
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Province"] == province:
                result.append(row)

    return result


def by_district(district=None):
    result = []
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["District"] == district.upper():
                result.append(row)
    print(result)
    return result
