import pandas as pd
from list_count import print_list_count
from oscar_count import print_best_picture_nominees
from print_header import print_header

lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_top_50_2024():
    box_office_titles = list(lists["2024 Box Office Title"])
    box_office_years = list(lists["2024 Box Office Year"])
    print_header(2)
    print_list_count(lists, box_office_titles, box_office_years, 2)
    print_best_picture_nominees(box_office_titles, box_office_years)