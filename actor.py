import requests
from bs4 import BeautifulSoup


def print_actor():
    url = "https://letterboxd.com/will1011/list/all-time-worldwide-box-office-top-100/stats/"
    response = requests.get(url)


print_actor()
