import requests
from bs4 import BeautifulSoup


def print_num_of_billions():
    url = "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/detail/"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        divs = soup.find_all("div", {"class": "body-text -prose collapsible-text"})

        if divs:
            num_of_one_billion = 0
            num_of_two_billion = 0

            for div in divs:
                box_office_value = div.find("p").text.strip()
                box_office_value = int(box_office_value[1:].replace(",", ""))
                if box_office_value >= 1000000000:
                    num_of_one_billion += 1
                if box_office_value >= 2000000000:
                    num_of_two_billion += 1
            print("Number of $1 billion films: " + str(num_of_one_billion))
            print("Number of $2 billion films: " + str(num_of_two_billion) + "\n")
