from bs4 import BeautifulSoup
import cloudscraper
import time

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

def print_next_to_join(num_movies):
    url = "https://letterboxd.com/victorvdb/list/letterboxd-500-most-watched-movies-of-all/"

    response = fetch_with_retry(url)
    if response is None:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    ul = soup.find("ul", class_="poster-list")

    if ul:
        items = ul.find_all("li")

        first_to_join = items[num_movies].find("div", class_="react-component")["data-item-name"]
        second_to_join = items[num_movies+1].find("div", class_="react-component")["data-item-name"]
        third_to_join = items[num_movies+2].find("div", class_="react-component")["data-item-name"]

        print("\nNext Films to Join:")
        print(first_to_join + ", " + second_to_join + ", " + third_to_join + "\n")