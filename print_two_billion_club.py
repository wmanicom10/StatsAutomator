import pandas as pd
from decade_count import print_decade_count
from list_order import print_list_order
from list_count import print_list_count
from print_header import print_header
from director_count import print_director_count
from print_first_film import print_first_film
from print_fastest_film import print_fastest_film
from print_latest_additions import print_latest_additions

two_billion_club = pd.read_excel("spreadsheets/twobillionclub.xlsx", dtype=str)
lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_two_billion_club():
    titles = list(two_billion_club["Title"].dropna())
    years = list(two_billion_club["Year"].dropna())
    directors = list(two_billion_club["Director"].dropna())
    dates_added = list(two_billion_club["Date Added"].dropna())
    print_header(5)
    print_latest_additions(dates_added, titles, 2)
    print_first_film(two_billion_club, 2)
    print_fastest_film(two_billion_club, 2)
    print_director_count(directors, 4)
    print_decade_count(years, 2)
    print_list_count(lists, titles, years, 10)
    print_list_order(15, titles)
    print_list_order(16, titles)