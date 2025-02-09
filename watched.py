import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re


def get_watched_number(url_string):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    service = Service("/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f"https://letterboxd.com{url_string}"
    driver.get(url)

    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    li = soup.find("li", class_="stat filmstat-watches")

    a_tag = li.find("a")

    watched_by = a_tag['data-original-title']

    match = re.search(r'\d{1,3}(?:,\d{3})*', watched_by)
    if match:
        watched_by_number = match.group().replace(",", "")

    driver.quit()
    return watched_by_number


url = "https://letterboxd.com/victorvdb/list/letterboxd-500-most-watched-movies-of-all/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    ul = soup.find("ul", class_="poster-list")

    if ul:
        items = ul.find_all("li")

        for item in items:
            title = item.find("img")['alt']

            url_string = item.find("div", class_="really-lazy-load")["data-target-link"]
            watched_number = int(get_watched_number(url_string))

            if watched_number >= 4000000:
                print(title + " - " + str(watched_number))
            else:
                break

