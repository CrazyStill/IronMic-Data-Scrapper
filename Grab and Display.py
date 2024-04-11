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



grab()
display()