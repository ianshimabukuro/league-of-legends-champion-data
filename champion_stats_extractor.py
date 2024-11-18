from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import csv

def extract_champion_stats_selenium() -> None:
    # Set up Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode, remove if you want to see the browser
    driver = webdriver.Chrome(options=options)

    # Open the webpage
    url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics'
    driver.get(url)

    # Find the table containing the champion statistics
    table = driver.find_element(By.TAG_NAME, 'table')

    # Initialize a list to store the extracted data
    data = []
    # Iterate over each row of the table and extract the desired data
    rows = table.find_elements(By.TAG_NAME, 'tr')
    headers = rows[0].find_elements(By.TAG_NAME, 'th')
    header_names = [header.text.strip() for header in headers]

    
    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) >= len(header_names):
            # Extract the champion name and image URL
            row_data = []
            for cell in cells:
                row_data.append(cell.text.strip())
            data.append(row_data)

    # Define the CSV file path
    csv_file = 'champion_stats.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(header_names)
        # Write the champion data rows
        writer.writerows(data)

    # Close the browser
    driver.quit()
    print("succesful")

    
def extract_champion_stats() -> None:
    # Define the URL of the webpage
    url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics'
    
    # Send a GET request to fetch the page content
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table containing champion statistics
    table = soup.find('table')
    
    if not table:
        print("Table not found.")
        return
    
    # Extract the table rows (skip the header row)
    rows = table.find_all('tr')[1:]  # Skip the first row (header)
    
    # Initialize a list to store the extracted data
    data = []
    
    for row in rows:
        # Extract the columns (cells) of the row
        cells = row.find_all('td')
        
        # Only proceed if the row has enough cells (ensuring we are in the right rows)
        if len(cells) >= 19:
            # Extract the cells and store them as a list
            row_data = [cell.text.strip() for cell in cells]
            
            # Add the extracted row data to the list
            data.append(row_data)

    # Define the CSV file path
    csv_file = 'champion_stats.csv'

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row (using the column names in the first row of the table)
        header_cells = table.find_all('th')
        headers = [header.text.strip() for header in header_cells]
        writer.writerow(headers)  # Write headers
        
        # Write the extracted data
        writer.writerows(data)  # Write the extracted rows
    
    print("Extraction successful")

if __name__ == '__main__':
    extract_champion_stats()
    
