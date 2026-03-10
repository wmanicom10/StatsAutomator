import re
import time
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}

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

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        ul = soup.find("ul", class_="poster-list")

        if ul:
            items = ul.find_all("li")

            highest = items[0].find("div", class_="react-component")["data-item-link"]
            lowest = items[len(items) - 1].find("div", class_="react-component")["data-item-link"]

            highest_url = f"https://letterboxd.com{highest}"
            lowest_url = f"https://letterboxd.com{lowest}"

            highest_response = requests.get(highest_url)
            lowest_response = requests.get(lowest_url)

            if highest_response.status_code == 200 and lowest_response.status_code == 200:
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
                elif option == 3 or option == 9 or option == 13:
                    highest_length = soup.find("p", class_="text-link text-footer")
                    highest_length_text = highest_length.get_text(strip=True)
                    duration = re.search(r"\d+", highest_length_text)
                    if duration:
                        highest_duration = duration.group()
                    highest_title = highest_title[0:len(highest_title) - 7]
                    formatted_duration = format_runtime(int(highest_duration))
                    print(highest_title + " - " + formatted_duration + "\n")
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
                elif option == 3 or option == 9 or option == 13:
                    lowest_length = soup.find("p", class_="text-link text-footer")
                    lowest_length_text = lowest_length.get_text(strip=True)
                    duration = re.search(r"\d+", lowest_length_text)
                    if duration:
                        lowest_duration = duration.group()
                    lowest_title = lowest_title[0:len(lowest_title) - 7]
                    formatted_duration = format_runtime(int(lowest_duration))
                    print(lowest_title + " - " + formatted_duration + "\n")
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
                print(highest_response.status_code)
                print(lowest_response.status_code)
    else:
        print(response.status_code)

def format_runtime(minutes):
    hours, mins = divmod(int(minutes), 60)
    if hours > 0 and mins > 0:
        return f"{hours} hr {mins} min"
    elif hours > 0:
        return f"{hours} hr"
    else:
        return f"{mins} min"
