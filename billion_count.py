from bs4 import BeautifulSoup
import time
import cloudscraper

scraper = cloudscraper.create_scraper()

def fetch_with_retry(url, retries=3, backoff=10):
    for attempt in range(retries):
        response = scraper.get(url)
        if response.status_code == 200:
            return response
        elif response.status_code in (403, 429):
            if attempt < retries - 1:
                wait = backoff * (2 ** attempt)
                print(f"Rate limited ({response.status_code}). Waiting {wait}s before retry...")
                time.sleep(wait)
            else:
                print(f"Failed after {retries} attempts. Status code: {response.status_code}")
                return None
        else:
            print(f"Error {response.status_code}")
            return None

def print_billion_count(option):
    url = ""

    if option == 1:
        url += "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/detail/"
    elif option == 2:
        url += "https://letterboxd.com/will1011/list/2025-worldwide-box-office-top-50/detail/"
    elif option == 3:
        url += "https://letterboxd.com/will1011/list/2026-worldwide-box-office-top-50/detail/"

    response = fetch_with_retry(url)
    if response is None:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", {"class": "listitem js-listitem"})

    num_of_one_billion = num_of_two_billion = 0

    for div in divs:
        p_tag = div.find("p")
        if p_tag and p_tag.text.startswith("$"):
            box_office_value = int(p_tag.text[1:].replace(",", ""))
            num_of_one_billion += box_office_value >= 1_000_000_000
            num_of_two_billion += box_office_value >= 2_000_000_000

    if option == 1:
        print(f"Number of $1 billion films: {num_of_one_billion}")
        print(f"Number of $2 billion films: {num_of_two_billion}\n")
    if option == 2:
        print(f"Number of $1 billion films: {num_of_one_billion}\n")