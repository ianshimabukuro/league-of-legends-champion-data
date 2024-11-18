from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import urllib.request
import csv

def extract_champion_stats() -> None:
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
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) >= 19:
            # Extract the champion name and image URL
            name_cell = cells[0].text.strip()
            
    
            # Extract other desired attributes
            hp = cells[1].text.strip()
            mp = cells[5].text.strip()
            ad = cells[9].text.strip()
            attack_speed = cells[11].text.strip()
            armor = cells[13].text.strip()
            magic_resistance = cells[15].text.strip()
            attack_range = cells[18].text.strip()

            # Add the extracted data to the list
            data.append([name_cell, hp, mp, ad, attack_speed, armor, magic_resistance, attack_range])

    # Define the CSV file path
    csv_file = 'champion_stats.csv'

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Champion', 'HP', 'MP', 'AD', 'Attack Speed', 'Armor', 'Magic Resistance', 'Attack Range'])
        writer.writerows(data)

    # Close the browser
    driver.quit()
    print("succesful")


if __name__ == '__main__':
    extract_champion_stats()
