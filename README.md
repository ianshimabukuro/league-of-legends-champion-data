# League of Legends Champion Statistics Extractor

This Python script automates the extraction of champion statistics and images from the League of Legends Wiki page. It utilizes web scraping techniques with the Selenium library, Chrome WebDriver and bs4

## Features

- Scrapes the League of Legends Wiki page to extract champion statistics 
- Stores the extracted data in a CSV file for further analysis or processing.

## Requirements

- Python 3.x
- Selenium library
- Chrome WebDriver
- bs4

## Usage

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install the Selenium library by running the following command:
   ```python
   pip install selenium
   ```
3. Download the Chrome WebDriver compatible with your Chrome browser version and operating system. Place the WebDriver executable in your system's PATH or the same directory as the script. WebDriver download link: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Clone or download this repository to your local machine..
5. Run the script using the following command:
   ```python
   python champion_stats_extractor.py
   ```
6. The script will start extracting champion statistics 
7. Once the process is complete, the extracted data will be stored in a CSV file named `champion_stats.csv`.
> Feel free to modify the script according to your needs, such as adding additional data extraction or customization options.

