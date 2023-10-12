# Importing all modules here:
from bs4 import BeautifulSoup
import requests
import time
import csv

# URL of the Website:
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Send a get request to the URL:
response = requests.get(START_URL)

# Giving time to load properly (you can adjust the sleep time as needed)
time.sleep(10)

# Creating a function to scrape the data from the URL/website:
def scrape():
    headers = ["Star_name","Distance","Mass", "Radius"]
    data = []  # Change this to data (not empty_data)

    # Parse the HTML content:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing the star data
    star_table = soup.find_all("table")
    table_rows = star_table[7]

    # Loop through table rows
    for row in table_rows.find_all("tr")[1:]:  # Skip the header row
        columns = row.find_all("td") 
        temp_list = []

        for column in columns:
            temp_list.append(column.get_text(strip=True))

        # Append data to the data list
        data.append(temp_list)

    # Write data into a CSV file
    with open("scrapper_2.csv", "w", newline="", encoding="utf-8") as f:
        csvwriter = csv.writer(f)  # Use 'f' instead of 'headers' here
        csvwriter.writerow(headers)
        csvwriter.writerows(data)

# Call the scrape function
scrape()
