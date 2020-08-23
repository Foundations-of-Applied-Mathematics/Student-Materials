"""Volume 3: Web Scraping.
<Name>
<Class>
<Date>
"""

# Problem 1
def prob1():
    """Use the requests library to get the HTML source for the website 
    http://www.example.com.
    Save the source as a file called example.html.
    If the file already exists, do not scrape the website or overwrite the file.
    """
    raise NotImplementedError("Problem 1 Incomplete")
    
# Problem 2
def prob2(code):
    """Return a list of the names of the tags in the given HTML code.
    Parameters:
        code (str): A string of html code
    Returns:
        (list): Names of all tags in the given code"""
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3(filename="example.html"):
    """Read the specified file and load it into BeautifulSoup. Return the
    text of the first <a> tag and whether or not it has an href
    attribute.
    Parameters:
        filename (str): Filename to open
    Returns:
        (str): text of first <a> tag
        (bool): whether or not the tag has an 'href' attribute
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4(filename="san_diego_weather.html"):
    """Read the specified file and load it into BeautifulSoup. Return a list
    of the following tags:

    1. The tag containing the date 'Thursday, January 1, 2015'.
    2. The tags which contain the links 'Previous Day' and 'Next Day'.
    3. The tag which contains the number associated with the Actual Max
        Temperature.

    Returns:
        (list) A list of bs4.element.Tag objects (NOT text).
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5(filename="large_banks_index.html"):
    """Read the specified file and load it into BeautifulSoup. Return a list
    of the tags containing the links to bank data from September 30, 2003 to
    December 31, 2014, where the dates are in reverse chronological order.

    Returns:
        (list): A list of bs4.element.Tag objects (NOT text).
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6(filename="large_banks_data.html"):
    """Read the specified file and load it into BeautifulSoup. Create a single
    figure with two subplots:

    1. A sorted bar chart of the seven banks with the most domestic branches.
    2. A sorted bar chart of the seven banks with the most foreign branches.

    In the case of a tie, sort the banks alphabetically by name.
    """
    raise NotImplementedError("Problem 6 Incomplete")
