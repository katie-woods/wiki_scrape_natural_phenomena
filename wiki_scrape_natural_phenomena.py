import requests
from bs4 import BeautifulSoup
import random

orig_page = "List_of_natural_phenomena"


def scrape_wiki_natural_phenomena(wiki_url):
    response = requests.get(
        url=wiki_url
    )
    print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    webpage_title = soup.find(id="firstHeading")
    print(f"Scraping {webpage_title.string}")

    # Get all the links
    all_links = soup.find(id="bodyContent").find_all("a")

    # reorder links
    random.shuffle(all_links)
    link_to_scrape = 0

    # only find other wiki pages
    for link in all_links:
        if link['href'].find("/wiki/") == -1:
            continue

        link_to_scrape = link
        break
    return link_to_scrape


random_phenomena_link = scrape_wiki_natural_phenomena("https://en.wikipedia.org/wiki/" + orig_page)
new_url = "https://en.wikipedia.org" + random_phenomena_link['href']
print(new_url)
