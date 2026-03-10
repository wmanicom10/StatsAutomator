import pandas as pd
from list_count import print_list_count
from print_header import print_header
from actor_count import print_actor_count
from director_count import print_director_count
from list_order import print_list_order
from billion_count import print_billion_count

lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_top_50_2026():
    box_office_titles = list(lists["2026 Box Office Title"])
    box_office_years = list(lists["2026 Box Office Year"])
    print_header(4)
    print_actor_count(3)
    print_director_count(None, 3)
    print_list_order(11)
    print_list_count(lists, box_office_titles, box_office_years, 3)
    print_billion_count(3)
    print_list_order(12)
    print_list_order(13)
    print_list_order(14)