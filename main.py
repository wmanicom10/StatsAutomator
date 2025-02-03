import pandas as pd
from director import print_director
from franchise import print_franchise
from decade import print_decade
from text import print_length
from year import print_year
from rating import print_list_order
from list import print_list
from oscar import print_best_picture, print_best_animated_feature, print_best_picture_nominees
import text as text

lists = pd.read_excel("lists.xlsx", dtype=str)

print("Which list would you like?")
print("1. Top 100 All-Time Worldwide")
print("2. Top 50 2024")
option = input("Enter an option: ")

if option == "1":
    box_office_titles = list(lists["Box Office Title"])
    box_office_years = list(lists["Box Office Year"])
    text.print_header(1)
    print_director(lists)
    text.print_actor(1)
    print_franchise(box_office_titles)
    print_decade(box_office_years)
    print_year(box_office_years)
    print_list_order(1)
    print_list_order(2)
    print_list(lists, box_office_titles, box_office_years)
    text.print_billion(1)
    print_best_picture(box_office_titles, box_office_years)
    print_best_animated_feature(box_office_titles, box_office_years)
    text.print_length(1)
    text.print_release(1)
elif option == "2":
    box_office_titles = list(lists["2024 Box Office Title"])
    box_office_years = list(lists["2024 Box Office Year"])
    text.print_header(2)
    text.print_actor(2)
    text.print_rating()
    print_list(lists, box_office_titles, box_office_years)
    text.print_billion(2)
    print_best_picture_nominees(box_office_titles, box_office_years)
    text.print_length(2)
    text.print_release(2)

