import Scrapper
import Search

def Main():
    Scrapper.scrape_html_content()
    Search.retrieve_html_lines()
    
    print()

Main()