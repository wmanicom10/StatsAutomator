import pandas as pd
import time
from franchise_count import print_franchise_count
from director_count import print_director_count
from actor_count import print_actor_count
from decade_count import print_decade_count
from year_count import print_year_count
from list_order import print_list_order
from list_count import print_list_count
from oscar_count import print_best_picture_count, print_best_animated_feature_count
from billion_count import print_billion_count
from print_header import print_header

lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_top_100_all_time_worldwide():
    box_office_titles = list(lists["Box Office Title"].dropna())
    box_office_years = list(lists["Box Office Year"].dropna())
    print_header(1)
    print_director_count(lists, 1)
    print_actor_count(1)
    print_franchise_count(box_office_titles)
    print_decade_count(box_office_years, 1)
    print_year_count(box_office_years)
    print_list_order(1)
    print_list_order(2)
    print_list_count(lists, box_office_titles, box_office_years, 1)
    print_billion_count(1)
    print_best_picture_count(box_office_titles, box_office_years, 1)
    print_best_animated_feature_count(box_office_titles, box_office_years, 1)
    time.sleep(65)
    print_list_order(3)
    print_list_order(4)