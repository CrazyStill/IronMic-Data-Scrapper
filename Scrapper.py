import requests
from bs4 import BeautifulSoup

def scrape_html_content():
    # URL of the website to scrape
    url = 'https://statsim.net/atc/combinedtime/'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Open a text file to write the HTML content
        with open('html.txt', 'w', encoding='utf-8') as file:
            # Write the HTML content of the page
            file.write("=== HTML Content ===\n")
            file.write(str(soup))
                
        print('HTML content has been successfully written to html.txt.')
    else:
        # Print an error message if the request was not successful
        print('Failed to retrieve data from the website.')

# Call the function to scrape HTML content only
scrape_html_content()
