import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

def print_next_to_join():
    titles = []
    watched_numbers = []

    url = "https://letterboxd.com/victorvdb/list/letterboxd-500-most-watched-movies-of-all/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ul = soup.find("ul", class_="poster-list")

        if ul:
            items = ul.find_all("li")

            for item in items:
                title = item.find("img")['alt']
                titles.append(title)

                url_string = item.find("div", class_="really-lazy-load")["data-target-link"]
                watched_number = int(get_watched_number(url_string))

                if 4250000 <= watched_number < 5000000 and len(titles):
                    watched_numbers.append(watched_number)
                else:
                    break

    combined = list(zip(titles, watched_numbers))
    combined.sort()
    watched_numbers_sorted, titles_sorted = zip(*combined)
    watched_numbers_sorted = list(watched_numbers_sorted)
    titles_sorted = list(titles_sorted)
    print(titles_sorted[:3])
    print(watched_numbers_sorted[:3])

print_next_to_join()