import pandas as pd
from director import print_director
from franchise import print_franchise
from decade import print_decade
from year import print_year
from list_order import print_list_order
from list import print_list
from oscar import print_best_picture, print_best_animated_feature, print_best_picture_nominees
from billion import print_num_of_billions
import text as text

lists = pd.read_excel("lists.xlsx", dtype=str)

print("Which list would you like?")
print("1. Top 100 All-Time Worldwide")
print("2. Top 50 2024")
print("3. Top 50 2025")
print("4. Letterboxd Five Million Watched Club")
option = input("Enter an option: ")

if option == "1":
    box_office_titles = list(lists["Box Office Title"].dropna())
    box_office_years = list(lists["Box Office Year"].dropna())
    text.print_header(1)
    print_director(lists)
    text.print_actor(1)
    print_franchise(box_office_titles)
    print_decade(box_office_years, 1)
    print_year(box_office_years)
    print_list_order(1)
    print_list_order(2)
    print_list(lists, box_office_titles, box_office_years, 1)
    print_num_of_billions()
    print_best_picture(box_office_titles, box_office_years)
    print_best_animated_feature(box_office_titles, box_office_years)
    print_list_order(3)
    print_list_order(4)
elif option == "2":
    box_office_titles = list(lists["2024 Box Office Title"])
    box_office_years = list(lists["2024 Box Office Year"])
    text.print_header(2)
    text.print_actor(2)
    text.print_rating(2)
    print_list(lists, box_office_titles, box_office_years)
    text.print_billion()
    print_best_picture_nominees(box_office_titles, box_office_years)
    text.print_length(2)
    text.print_release(2)
elif option == "3":
    box_office_titles = list(lists["2025 Box Office Title"])
    box_office_years = list(lists["2025 Box Office Year"])
    text.print_header(3)
    text.print_actor(3)
    text.print_rating(3)
    print_list(lists, box_office_titles, box_office_years)
    text.print_length(3)
    text.print_release(3)
elif option == "4":
    titles = list(lists["Five Million Title"].dropna())
    years = list(lists["Five Million Year"].dropna())
    text.print_header(4)
    print_decade(years, 4)
    # highest/lowest rated
    # print_list_order(5)
    # print_list_order(6)
    print_list(lists, titles, years, 2)
