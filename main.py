import pandas as pd
from director_count import print_director_count
from franchise_count import print_franchise_count
from decade_count import print_decade_count
from year_count import print_year_count
from list_order import print_list_order
from list_count import print_list_count
from oscar_count import print_best_picture_count, print_best_animated_feature_count, print_best_picture_nominees
from billion_count import print_billion_count
from print_header import print_header

lists = pd.read_excel("spreadsheets/lists.xlsx", dtype=str)

print("Which list would you like?")
print("1. Top 100 All-Time Worldwide")
print("2. Top 50 2024")
print("3. Top 50 2025")
print("4. Letterboxd Five Million Watched Club")
option = input("Enter an option: ")

if option == "1":
    box_office_titles = list(lists["Box Office Title"].dropna())
    box_office_years = list(lists["Box Office Year"].dropna())
    print_header(1)
    print_director_count(lists)
    print_franchise_count(box_office_titles)
    print_decade_count(box_office_years, 1)
    print_year_count(box_office_years)
    print_list_order(1)
    print_list_order(2)
    print_list_count(lists, box_office_titles, box_office_years, 1)
    print_billion_count()
    print_best_picture_count(box_office_titles, box_office_years)
    print_best_animated_feature_count(box_office_titles, box_office_years)
    print_list_order(3)
    print_list_order(4)
elif option == "2":
    box_office_titles = list(lists["2024 Box Office Title"])
    box_office_years = list(lists["2024 Box Office Year"])
    print_header(2)
    print_list_count(lists, box_office_titles, box_office_years, 2)
    print_best_picture_nominees(box_office_titles, box_office_years)
elif option == "3":
    box_office_titles = list(lists["2025 Box Office Title"])
    box_office_years = list(lists["2025 Box Office Year"])
    print_header(3)
    print_list_count(lists, box_office_titles, box_office_years, 3)
elif option == "4":
    titles = list(lists["Five Million Title"].dropna())
    years = list(lists["Five Million Year"].dropna())
    print_header(4)
    print_decade_count(years, 4)
    # highest/lowest rated
    # print_list_order(5)
    # print_list_order(6)
    print_list_count(lists, titles, years, 2)
