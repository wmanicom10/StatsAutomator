import pandas as pd
from list_count import print_list_count
from print_header import print_header

lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

def print_top_50_2025():
    box_office_titles = list(lists["2025 Box Office Title"])
    box_office_years = list(lists["2025 Box Office Year"])
    print_header(3)
    print_list_count(lists, box_office_titles, box_office_years, 3)