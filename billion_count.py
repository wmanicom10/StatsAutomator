import requests
from bs4 import BeautifulSoup

def print_billion_count():
    url = "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/detail/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", {"class": "body-text -prose collapsible-text"})

    num_of_one_billion = num_of_two_billion = 0

    for div in divs:
        p_tag = div.find("p")
        if p_tag and p_tag.text.startswith("$"):
            box_office_value = int(p_tag.text[1:].replace(",", ""))
            num_of_one_billion += box_office_value >= 1_000_000_000
            num_of_two_billion += box_office_value >= 2_000_000_000

    print(f"Number of $1 billion films: {num_of_one_billion}")
    print(f"Number of $2 billion films: {num_of_two_billion}\n")
