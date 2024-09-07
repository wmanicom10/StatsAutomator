import pandas as pd
from header import print_header
from director import print_director
from decade import print_decade
from franchise import print_franchise
from rating import print_rating
from list import print_list
from oscar import print_best_picture, print_best_animated_feature
from length import print_length
from release import print_release
from year import print_year

lists = pd.read_excel("lists.xlsx", dtype=str)

box_office_titles = list(lists["Box Office Title"])
box_office_years = list(lists["Box Office Year"])

print_header()
print_director()
print_franchise(box_office_titles)
print_decade(box_office_years)
print_year(box_office_years)
print_rating()
print_list(box_office_titles, box_office_years)
print_best_picture(box_office_titles, box_office_years)
print_best_animated_feature(box_office_titles, box_office_years)
print_length()
print_release()
