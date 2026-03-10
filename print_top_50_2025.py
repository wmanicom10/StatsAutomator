import pandas as pd
from list_count import print_list_count
from print_header import print_header
from actor_count import print_actor_count
from list_order import print_list_order
from billion_count import print_billion_count
from oscar_count import print_best_picture_nominees

lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_top_50_2025():
    box_office_titles = list(lists["2025 Box Office Title"])
    box_office_years = list(lists["2025 Box Office Year"])
    print_header(2)
    print_actor_count(2)
    print_list_count(lists, box_office_titles, box_office_years, 3)
    print_best_picture_nominees(box_office_titles, box_office_years)
    print_billion_count(2)
    print_list_order(7)
    print_list_order(8)
    print_list_order(9)
    print_list_order(10)