import requests
from bs4 import BeautifulSoup
import random

orig_page = "List_of_natural_phenomena"


def get_webpage_details(web_url):
    response = requests.get(
        url=web_url
    )
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # print webpage title and url
        webpage_title = soup.find(id="firstHeading")
        print(f"Title: {webpage_title.string}")
        print(f"url: {web_url}")
        return soup
    else:
        print(f"Could not find {web_url}")


def scrape_wiki_natural_phenomena(wiki_url):
    soup = get_webpage_details(wiki_url)

    # Get all the links
    all_links = soup.find(id="bodyContent").find_all("a")

    # reorder links
    random.shuffle(all_links)
    link_to_scrape = 0

    # only find other wiki pages
    for link in all_links:
        if link['href'].find("/wiki/") == -1:
            continue
        elif link['href'].find("/wiki/File:") == 0:
            continue

        link_to_scrape = link
        break
    return link_to_scrape


random_phenomena_link = scrape_wiki_natural_phenomena("https://en.wikipedia.org/wiki/" + orig_page)
new_url = "https://en.wikipedia.org" + random_phenomena_link['href']
soup = get_webpage_details(new_url)