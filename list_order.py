import re
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

def get_runtime_from_url(url):
    response = fetch_with_retry(url)
    if response is None:
        return None, None
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("meta", {"property": "og:title"})["content"]
    title = title[0:len(title) - 7]
    length = soup.find("p", class_="text-link text-footer")
    if length:
        length_text = length.get_text(strip=True)
        duration = re.search(r"\d+", length_text)
        if duration:
            return title, int(duration.group())
    return title, None

def print_list_order(option, titles=None):
    url = ""
    highest_text = ""
    lowest_text = ""
    if option == 1:
        url += "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/by/rating/"
        highest_text += "Highest rated film in the list"
        lowest_text += "Lowest rated film in the list"
    elif option == 2:
        url += "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/by/popular/"
        highest_text += "Most popular film in the list"
        lowest_text += "Least popular film in the list"
    elif option == 3:
        url += "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/by/longest/"
        highest_text += "Longest film in the list"
        lowest_text += "Shortest film in the list"
    elif option == 4:
        url += "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/by/release-earliest/"
        highest_text += "Oldest film in the list"
        lowest_text += "Newest film in the list"
    elif option == 5:
        url += "https://letterboxd.com/will1011/list/letterboxd-five-million-watched-club/by/rating/"
        highest_text += "Highest Rated Film"
        lowest_text += "Lowest Rated Film"
    elif option == 6:
        url += "https://letterboxd.com/will1011/list/letterboxd-five-million-watched-club/by/release-earliest/"
        highest_text += "Oldest Film"
        lowest_text += "Newest Film"
    elif option == 7:
        url += "https://letterboxd.com/will1011/list/2025-worldwide-box-office-top-50/by/rating/"
        highest_text += "Highest rated film in the list"
        lowest_text += "Lowest rated film in the list"
    elif option == 8:
        url += "https://letterboxd.com/will1011/list/2025-worldwide-box-office-top-50/by/popular/"
        highest_text += "Most popular film in the list"
        lowest_text += "Least popular film in the list"
    elif option == 9:
        url += "https://letterboxd.com/will1011/list/2025-worldwide-box-office-top-50/by/longest/"
        highest_text += "Longest film in the list"
        lowest_text += "Shortest film in the list"
    elif option == 10:
        url += "https://letterboxd.com/will1011/list/2025-worldwide-box-office-top-50/by/release-earliest/"
        highest_text += "Oldest film in the list"
        lowest_text += "Newest film in the list"
    elif option == 11:
        url += "https://letterboxd.com/will1011/list/2026-worldwide-box-office-top-50/by/rating/"
        highest_text += "Highest rated film in the list"
        lowest_text += "Lowest rated film in the list"
    elif option == 12:
        url += "https://letterboxd.com/will1011/list/2026-worldwide-box-office-top-50/by/popular/"
        highest_text += "Most popular film in the list"
        lowest_text += "Least popular film in the list"
    elif option == 13:
        url += "https://letterboxd.com/will1011/list/2026-worldwide-box-office-top-50/by/longest/"
        highest_text += "Longest film in the list"
        lowest_text += "Shortest film in the list"
    elif option == 14:
        url += "https://letterboxd.com/will1011/list/2026-worldwide-box-office-top-50/by/release-earliest/"
        highest_text += "Oldest film in the list"
        lowest_text += "Newest film in the list"

    response = fetch_with_retry(url)
    if response is None:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    ul = soup.find("ul", class_="poster-list")

    if ul:
        items = ul.find_all("li")
        all_item_links = [item.find("div", class_="react-component")["data-item-link"] for item in items]

        highest_url = f"https://letterboxd.com{all_item_links[0]}"
        lowest_url = f"https://letterboxd.com{all_item_links[-1]}"

        # Handle longest/shortest with tie detection
        if option in (3, 9, 13):
            highest_title, highest_duration = get_runtime_from_url(highest_url)
            lowest_title, lowest_duration = get_runtime_from_url(lowest_url)

            if highest_duration is None or lowest_duration is None:
                return

            # Find all films tied for longest (list is sorted, scan from top until runtime changes)
            longest_titles = [highest_title]
            for link in all_item_links[1:]:
                item_title, item_duration = get_runtime_from_url(f"https://letterboxd.com{link}")
                if item_duration == highest_duration:
                    longest_titles.append(item_title)
                else:
                    break

            # Find all films tied for shortest (scan from bottom until runtime changes)
            shortest_titles = [lowest_title]
            for link in reversed(all_item_links[:-1]):
                item_title, item_duration = get_runtime_from_url(f"https://letterboxd.com{link}")
                if item_duration == lowest_duration:
                    shortest_titles.append(item_title)
                else:
                    break

            print(highest_text)
            if len(longest_titles) > 1:
                print(", ".join(longest_titles) + " - " + format_runtime(highest_duration) + "\n")
            else:
                print(highest_title + " - " + format_runtime(highest_duration) + "\n")

            print(lowest_text)
            if len(shortest_titles) > 1:
                print(", ".join(shortest_titles) + " - " + format_runtime(lowest_duration) + "\n")
            else:
                print(lowest_title + " - " + format_runtime(lowest_duration) + "\n")

            return

        highest_response = fetch_with_retry(highest_url)
        lowest_response = fetch_with_retry(lowest_url)

        if highest_response is None or lowest_response is None:
            return

        highest_html = highest_response.text
        lowest_html = lowest_response.text

        soup = BeautifulSoup(highest_html, "html.parser")

        highest_title = soup.find("meta", {"property": "og:title"})["content"]
        print(highest_text)
        if option == 1 or option == 7 or option == 11:
            highest_title = highest_title[0:len(highest_title) - 7]
            highest_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
            highest_rating = highest_rating.split(" ")[0]
            print(highest_title + " (" + highest_rating + ")\n")
        elif option == 2 or option == 4 or option == 8 or option == 10 or option == 12 or option == 14:
            print(highest_title + "\n")
        elif option == 5:
            highest_title = highest_title[0:len(highest_title) - 7]
            highest_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
            highest_rating = highest_rating.split(" ")[0]
            highest_title_index = len(titles) - titles.index(highest_title)
            print("#" + str(highest_title_index) + " " + highest_title + " (" + highest_rating + ")\n")
        elif option == 6:
            highest_title_index = len(titles) - titles.index(highest_title[0:len(highest_title) - 7])
            print("#" + str(highest_title_index) + " " + highest_title + "\n")

        soup = BeautifulSoup(lowest_html, "html.parser")

        lowest_title = soup.find("meta", {"property": "og:title"})["content"]
        print(lowest_text)
        if option == 1 or option == 7 or option == 11:
            lowest_title = lowest_title[0:len(lowest_title) - 7]
            lowest_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
            lowest_rating = lowest_rating.split(" ")[0]
            print(lowest_title + " (" + lowest_rating + ")\n")
        elif option == 2 or option == 4 or option == 8 or option == 10 or option == 12 or option == 14:
            print(lowest_title + "\n")
        elif option == 5:
            lowest_title = lowest_title[0:len(lowest_title) - 7]
            lowest_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
            lowest_rating = lowest_rating.split(" ")[0]
            lowest_title_index = len(titles) - titles.index(lowest_title)
            print("#" + str(lowest_title_index) + " " + lowest_title + " (" + lowest_rating + ")\n")
        elif option == 6:
            lowest_title_index = len(titles) - titles.index(lowest_title[0:len(lowest_title) - 7])
            print("#" + str(lowest_title_index) + " " + lowest_title + "\n")
    else:
        print("Could not find poster list on page")

def format_runtime(minutes):
    hours, mins = divmod(int(minutes), 60)
    if hours > 0 and mins > 0:
        return f"{hours} hr {mins} min"
    elif hours > 0:
        return f"{hours} hr"
    else:
        return f"{mins} min"