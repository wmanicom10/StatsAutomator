from bs4 import BeautifulSoup
import requests


def print_average_ratings():
    url = "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/by/rating/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        ul = soup.find("ul", class_="poster-list")

        if ul:
            items = ul.find_all("li")

            highest_rated = items[0].find("div", class_="really-lazy-load")["data-target-link"]
            lowest_rated = items[len(items) - 1].find("div", class_="really-lazy-load")["data-target-link"]

            highest_rated_url = f"https://letterboxd.com{highest_rated}"
            lowest_rated_url = f"https://letterboxd.com{lowest_rated}"

            highest_rated_response = requests.get(highest_rated_url)
            lowest_rated_response = requests.get(lowest_rated_url)

            if highest_rated_response.status_code == 200 and lowest_rated_response.status_code == 200:
                highest_rated_html = highest_rated_response.text
                lowest_rated_html = lowest_rated_response.text

                soup = BeautifulSoup(highest_rated_html, "html.parser")
                highest_average_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
                highest_average_rating = highest_average_rating.split(" ")[0]
                highest_rated_title = soup.find("meta", {"property": "og:title"})["content"]
                highest_rated_title = highest_rated_title[0:len(highest_rated_title) - 7]
                print("Highest rated film in the list")
                print(highest_rated_title + " (" + highest_average_rating + ")\n")

                soup = BeautifulSoup(lowest_rated_html, "html.parser")
                lowest_average_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
                lowest_average_rating = lowest_average_rating.split(" ")[0]
                lowest_rated_title = soup.find("meta", {"property": "og:title"})["content"]
                lowest_rated_title = lowest_rated_title[0:len(lowest_rated_title) - 7]
                print("Lowest rated film in the list")
                print(lowest_rated_title + " (" + lowest_average_rating + ")\n")

        else:
            print("not found")

    else:
        print(response.status_code)
