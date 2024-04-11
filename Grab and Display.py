import Scrapper
import Search
import Lines
import clean
import re
import xlwt
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

        # Create a new Excel workbook and add a sheet
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Airport Data')

        # Write headers
        sheet.write(0, 0, 'Airport Code')
        sheet.write(0, 1, 'Time')

        # Write data
        for row, (airport_code, time) in enumerate(data_array, start=1):
            sheet.write(row, 0, airport_code)
            sheet.write(row, 1, time)

        # Save the workbook
        workbook.save('timedata.xls')

# Call the functions
grab()
display()
