import pandas as pd
from decade_count import print_decade_count
from list_order import print_list_order
from list_count import print_list_count
from oscar_count import print_best_picture_count, print_best_director_count, print_best_actor_count, print_best_actress_count, print_best_animated_feature_count
from print_latest_additions import print_latest_additions
from next_to_join import print_next_to_join
from print_header import print_header
from director_count import print_director_count
from print_first_film import print_first_film
from print_fastest_film import print_fastest_film
from print_list_growth import print_list_growth

five_million_watched_club = pd.read_excel("spreadsheets/fivemillionwatchedclub.xlsx", dtype=str)
lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_five_million_watched_club():
    titles = list(five_million_watched_club["Title"].dropna())
    years = list(five_million_watched_club["Year"].dropna())
    directors = list(five_million_watched_club["Director"].dropna())
    dates_added = list(five_million_watched_club["Date Added"].dropna())
    print_header(3)
    print_latest_additions(dates_added, titles)
    print_next_to_join(len(titles))
    print("STATS:\n")
    print_first_film(five_million_watched_club)
    print_fastest_film(five_million_watched_club)
    print_director_count(directors, 2)
    print_decade_count(years, 2)
    print_list_order(5, titles)
    print_list_order(6, titles)
    print_list_count(lists, titles, years, 4)
    print("Number Of Films Directed By Women: 1")
    print("Number Of Films Not In English: 1")
    print_best_picture_count(titles, years, 4)
    print_best_director_count(titles, years)
    print_best_actor_count(titles, years)
    print_best_actress_count(titles, years)
    print_best_animated_feature_count(titles, years, 2)
    print_list_growth(dates_added)
    print("Other Clubs\nOne Million Watched Club\nTwo Million Watched Club\nThree Million Watched Club\nFour Million Watched Club\nSix Million Watched Club")