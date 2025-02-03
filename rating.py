from bs4 import BeautifulSoup
import requests


def print_list_order(option):
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

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        ul = soup.find("ul", class_="poster-list")

        if ul:
            items = ul.find_all("li")

            highest = items[0].find("div", class_="really-lazy-load")["data-target-link"]
            lowest = items[len(items) - 1].find("div", class_="really-lazy-load")["data-target-link"]

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
                if option == 1:
                    highest_title = highest_title[0:len(highest_title) - 7]
                    highest_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
                    highest_rating = highest_rating.split(" ")[0]
                    print(highest_title + " (" + highest_rating + ")\n")
                elif option == 2:
                    print(highest_title + "\n")

                soup = BeautifulSoup(lowest_html, "html.parser")
                lowest_title = soup.find("meta", {"property": "og:title"})["content"]
                print(lowest_text)
                if option == 1:
                    lowest_title = lowest_title[0:len(lowest_title) - 7]
                    lowest_rating = soup.find("meta", {"name": "twitter:data2"})["content"]
                    lowest_rating = lowest_rating.split(" ")[0]
                    print(lowest_title + " (" + lowest_rating + ")\n")
                elif option == 2:
                    print(lowest_title + "\n")
            else:
                print("not found")
        else:
            print(response.status_code)
            print(response.text)
