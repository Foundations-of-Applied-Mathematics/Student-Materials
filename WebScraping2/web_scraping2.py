"""Volume 3: Web Scraping 2.
<Name>
<Class>
<Date>
"""

import re
import time
import requests
from bs4 import BeautifulSoup


# Problem 1
def wunder_temp(day="/history/airport/KSAN/2012/7/1/DailyHistory.html"):
    """Crawl through Weather Underground and extract temperature data."""
    # Initialize variables, including a regex for finding the 'Next Day' link.
    actual_mean_temp = []
    next_day_finder = re.compile(r"Next Day")
    base_url = "https://www.wunderground.com"       # Web page base URL.
    page = base_url + day                           # Complete page URL.
    current = None

    for _ in range(4):
        while current is None:  # Try downloading until it works.
            # Download the page source and PAUSE before continuing.
            page_source = requests.get(page).text
            time.sleep(1)           # PAUSE before continuing.
            soup = BeautifulSoup(page_source, "html.parser")
            current = soup.find(string="Mean Temperature")

        # Navigate to the relevant tag, then extract the temperature data.
        temp_tag = current.parent.parent.next_sibling.next_sibling.span.span
        actual_mean_temp.append(int(temp_tag.string))

        # Find the URL for the page with the next day's data.
        new_day = soup.find(string=next_day_finder).parent["href"]
        page = base_url + new_day                   # New complete page URL.
        current = None

    return actual_mean_temp


# Problem 2
def bank_data():
    """Crawl through the Federal Reserve site and extract bank data."""
    # Compile regular expressions for finding certain tags.
    link_finder = re.compile(r"2004$")
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

        # Find the tag corresponding to Chase Banks's consolidated assets.
        temp_tag = soup.find(name="td", string=chase_bank_finder)
        for _ in range(10):
            temp_tag = temp_tag.next_sibling
        # Extract the data, removing commas.
        chase_assets.append(int(temp_tag.string.replace(',', '')))

    return chase_assets


# Problem 3
def prob3():
    """ESPN hosts data on NBA athletes at
    http://www.espn.go.com/nba/statistics. Each player has their own page with
    detailed performance statistics. For each of the five offensive leaders in
    points and each of the five defensive leaders in rebounds, extract the
    player’s career minutes per game (MPG) and career points per game (PPG).
    Make a scatter plot of MPG against PPG for these ten players.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4(search_query):
    """Use Selenium to enter the given search query into the search bar of
    https://arxiv.org and press Enter. The resulting page has up to 25 links
    to the PDFs of technical papers that match the query. Gather these URLs,
    then continue to the next page (if there are more results) and continue
    gathering links until obtaining at most 100 URLs. Return the list of URLs.

    Returns:
        (list): Up to 100 URLs that lead directly to PDFs on arXiv.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5():
    """For each of the (at least) 600 problems in the archive at
    https://projecteuler.net/archives, record the problem ID and the number of
    people who have solved it. Return a list of IDs, sorted from largest to
    smallest by the number of people who have solved them. That is, the first
    entry in the list should be the ID of the most solved problem, and the
    last entry in the list should be the ID of the least solved problem.

    Returns:
        (list): problem IDs (as strings), from most solved to least solved.
    """
    raise NotImplementedError("Problem 4 Incomplete")
