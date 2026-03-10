from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}

def print_next_to_join(num_movies):
    url = "https://letterboxd.com/victorvdb/list/letterboxd-500-most-watched-movies-of-all/"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        ul = soup.find("ul", class_="poster-list")

        if ul:
            items = ul.find_all("li")

            first_to_join = items[num_movies].find("div", class_="react-component")["data-item-name"]
            second_to_join = items[num_movies+1].find("div", class_="react-component")["data-item-name"]
            third_to_join = items[num_movies+2].find("div", class_="react-component")["data-item-name"]

            print("\nNext Films to Join:")
            print(first_to_join + ", " + second_to_join + ", " + third_to_join + "\n")

    else:
        print(response.status_code)