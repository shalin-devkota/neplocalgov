from bs4 import BeautifulSoup as soup
import requests
import csv
import json

url = (
    "https://www.nepalgov.com/list-of-municipalities-and-rural-municipalities-english/"
)

try:
    response = requests.get(url)
    response.raise_for_status()  # Ensure the response is successful
    data_soup = soup(response.text, "html.parser")
except requests.RequestException as e:
    print(f"Error: {e}")
    exit()  # Exit the script if there's an error fetching the data

data_table = data_soup.find("table", {"id": "tablepress-4"})
data_rows = data_table.find_all("tr")

# Extract headers
header_row = data_rows[0].find_all("th")
headers = [header.text.strip() for header in header_row]

data_list = []  # List to store data for JSON

with open("data/data.csv", "w", newline="", encoding="utf-8") as csvfile, open(
    "data/data.json", "w", encoding="utf-8"
) as jsonfile:
    csv_writer = csv.DictWriter(
        csvfile,
        fieldnames=headers,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL,
    )
    csv_writer.writeheader()

    for row in data_rows[1:]:  # Skip header row
        columns = row.find_all("td")
        row_data = {headers[j]: columns[j].text.strip() for j in range(len(headers))}
        csv_writer.writerow(row_data)
        data_list.append(row_data)

    json.dump(data_list, jsonfile, indent=4)

print("Completed")
