"""Data Science Essentials: Web Crawling."""

import re
import time
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pickle

# Problem 1
def scrape_books(start_page = "index.html"):
    """ Crawl through http://books.toscrape.com and extract fiction data"""
    
    # Initialize variables, including a regex for finding the 'next' link.
    base_url="http://books.toscrape.com/catalogue/category/books/fiction_10/"
    titles = []
    page = base_url + start_page                # Complete page URL.
    next_page_finder = re.compile(r"next")      # We need this button.
    
    current = None

    for _ in range(2):
        while current == None:                   # Try downloading until it works.
            # Download the page source and PAUSE before continuing.  
            page_source = requests.get(page).text
            time.sleep(1)           # PAUSE before continuing.
            soup = BeautifulSoup(page_source, "html.parser")
            current = soup.find_all(class_="product_pod")
            
        # Navigate to the correct tag and extract title.
        for book in current:
            titles.append(book.h3.a["title"])
    
        # ind the URL for the page with the next data
        if "page-2" not in page:
            # Find the URL for the page with the next data.
            new_page = soup.find(string=next_page_finder).parent["href"]    
            page = base_url + new_page      # New complete page URL.
            current = None
    return titles

# Problem 2
def bank_data():
    """Crawl through the Federal Reserve site and extract bank data."""
    # Compile regular expressions for finding certain tags.
    link_finder = re.compile(r"December 31, (?!2003)")
    chase_bank_finder = re.compile(r"^JPMORGAN CHASE BK")

    # Get the base page and find the URLs to all other relevant pages.
    base_url="https://www.federalreserve.gov/releases/lbr/"
    base_page_source = requests.get(base_url).text
    base_soup = BeautifulSoup(base_page_source, "html.parser")
    link_tags = base_soup.find_all(name='a', href=True, string=link_finder)
    pages = [base_url + tag.attrs["href"] for tag in link_tags]

    # Crawl through the individual pages and record the data.
    chase_assets = []
    for page in pages:
        time.sleep(1)               # PAUSE, then request the page.
        soup = BeautifulSoup(requests.get(page).text, "html.parser")

        # Find the tag corresponding to the banks' consolidated assets.
        temp_tag = soup.find(name="td", string=chase_bank_finder)

        for _ in range(10):
            temp_tag = temp_tag.next_sibling
            
        # Extract the data, removing commas.
        chase_assets.append(int(chase_temp_tag.string.replace(',', '')))

    return chase_assets
    raise NotImplementedError("Problem 4 Incomplete")

# Problem 3
def prob3():
    '''The Basketball Reference website at 
    https://www.basketball-reference.com} hosts data on NBA athletes, 
    including which player led different categories.
    For the past ten years, identify which player had the most season points.
    Return a list of triples, ("season year", "player name", points scored).
    '''
    raise NotImplementedError("Problem 3 Incomplete")

# Problem 4
def prob4():
    """
    Sort the Top 10 movies of the week by Total Grossing, taken from 
    https://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht.

    Returns:
        titles (list): Top 10 movies of the week sorted by total grossing
    """
    raise NotImplementedError("Problem 4 Incomplete")

# Problem 5
def prob5(search_query):
    """Use Selenium to enter the given search query into the search bar of
    https://arxiv.org and press Enter. The resulting page has up to 25 links
    to the PDFs of technical papers that match the query. Gather these URLs,
    then continue to the next page (if there are more results) and continue
    gathering links until obtaining at most 100 URLs. Return the list of URLs.

    Returns:
        (list): Up to 100 URLs that lead directly to PDFs on arXiv.
    """
    raise NotImplementedError("Problem 5 Incomplete")
