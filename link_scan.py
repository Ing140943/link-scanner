import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


def get_links_url(url: str):
    """Find all links_url on page at the given url.

       Returns:
          a list of all unique hyperlinks_url on the page,
          without page fragments or query parameters.
     """
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(url)
    links_url = []
    elements = browser.find_elements_by_tag_name('a')
    for elem in elements:
        href = str(elem.get_attribute("href"))
        question_tag = href.find('?')
        square_tag = href.find('#')
        begin_url = href.startswith('h')
        if len(href) >= 1 and begin_url:                    # startswith return boolean 
            if (question_tag == -1 and square_tag == -1):   # .find return the position of element that we looking for
                if (href not in links_url):
                    links_url.append(href)
            elif (question_tag > -1 and square_tag > -1):
                find_min = min(square_tag, question_tag)
                if (href[:find_min] not in links_url):
                    links_url.append(href[:find_min])
            elif (question_tag > -1):
                if (href[:question_tag] not in links_url):
                    links_url.append(href[:question_tag])
            elif (square_tag > -1):
                if (href[:square_tag] not in links_url):
                    links_url.append(href[:square_tag])
    return links_url


def is_valid_url(url: str):
    """Test if a url is reachable (valid) or not."""
    try:
        urllib.request.urlopen(url)
    except Exception:
        return False
    return True


def invalid_urls(urllist: list):
    """Returns a new list containing only the invalid URLs."""
    invalid_urls = []
    for url in urllist:
        if (not is_valid_url(url)):
            invalid_urls.append(url)
    return invalid_urls


if __name__ == "__main__":
    """Main"""
    if len(sys.argv) == 2:
        url = sys.argv[1]
        if is_valid_url(url):
            links_url = get_links_url(url)
            invalid_urls = invalid_urls(links_url)
            print("")
            for link in links_url:
                print(link)
            print("Bad Links_url:")
            for bad_link in invalid_urls:
                print(bad_link)
        else:
            print("Invalid URL.")
    else:
        print("Usage: python link_scan.py url")
        print("")
        print("Test all hyperlinks_url on the given url.")
