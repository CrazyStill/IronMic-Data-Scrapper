import Scrapper
import Search
import Lines
import clean
import re
from bs4 import BeautifulSoup

def grab():
    Lines.main()
    Scrapper.scrape_html_content()
    Search.retrive_data_start()
    
def display():
    clean.main()
    # Open the file for reading
    with open("clean.txt", "r") as file:
        lines = file.readlines()

        # Initialize an empty array to store the data
        data_array = []

        # Loop through the lines of the file
        for i in range(0, len(lines), 2):
            # Extract the first 7 characters from the first line
            airport_code = lines[i][:7].strip()
            # Get the time from the next line
            time = lines[i+1].strip()
            # Append the data to the array
            data_array.append((airport_code, time))

        # Print the data
        for airport_code, time in data_array:
            print(f"Airport Code: {airport_code}, Time: {time}")

# Call the functions
grab()
display()
