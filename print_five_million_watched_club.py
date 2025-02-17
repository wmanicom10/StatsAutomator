import pandas as pd
from decade_count import print_decade_count
from list_order import print_list_order
from list_count import print_list_count
from oscar_count import print_best_picture_count, print_best_director_count
from print_latest_additions import print_latest_additions
from print_header import print_header
from print_first_film import print_first_film
from print_fastest_film import print_fastest_film
from print_list_growth import print_list_growth

five_million_watched_club = pd.read_excel("spreadsheets/fivemillionwatchedclub.xlsx", dtype=str)
lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_five_million_watched_club():
    titles = list(five_million_watched_club["Title"].dropna())
    years = list(five_million_watched_club["Year"].dropna())
    dates_added = list(five_million_watched_club["Date Added"].dropna())

    print_header(4)
    print_latest_additions(dates_added, titles)
    print("\nNext Films to Join:")
    print("Fight Club (1999), Interstellar (2014), Joker (2019)\n")
    print("STATS:\n")
    print_first_film(five_million_watched_club)
    print_fastest_film(five_million_watched_club)
    print_decade_count(years, 4)
    print_list_order(5)
    print_list_order(6)
    print_list_count(lists, titles, years, 4)
    print("Number Of Films Directed By Women: 1")
    print("Number Of Films Not In English: 0")
    print_best_picture_count(titles, years, 4)
    print_best_director_count(titles, years)
    print_list_growth(dates_added)