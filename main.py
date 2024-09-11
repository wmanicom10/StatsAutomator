import pandas as pd
from director import print_director
from decade import print_decade
from franchise import print_franchise
from list import print_list
from oscar import print_best_picture, print_best_animated_feature
from year import print_year
import text as text

lists = pd.read_excel("lists.xlsx", dtype=str)

box_office_titles = list(lists["Box Office Title"])
box_office_years = list(lists["Box Office Year"])

text.print_header()
print_director(lists)
print_franchise(box_office_titles)
print_decade(box_office_years)
print_year(box_office_years)
text.print_rating()
print_list(lists, box_office_titles, box_office_years)
text.print_billion()
print_best_picture(box_office_titles, box_office_years)
print_best_animated_feature(box_office_titles, box_office_years)
text.print_length()
text.print_release()
