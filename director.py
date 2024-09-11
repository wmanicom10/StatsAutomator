import pandas as pd
from collections import Counter


def extract_last_name(full_name):
    return full_name.split()[-1]


def print_director(lists):
    box_office_directors = list(lists["Box Office Director"])
    box_office_directors_separated = []

    for i in range(100):
        if isinstance(box_office_directors[i], str):
            director = box_office_directors[i]
            if ',' in director:
                index = director.find(',')
                box_office_directors_separated.append(director[:index])
                box_office_directors_separated.append(director[index + 2:])
            else:
                box_office_directors_separated.append(director)

    director_counts = Counter(box_office_directors_separated)
    sorted_directors = sorted(
        director_counts.items(),
        key=lambda x: (-x[1], extract_last_name(x[0]))
    )

    print("Directors with 3+ films in the list")
    for i in range(len(sorted_directors)):
        if sorted_directors[i][1] > 2:
            print(sorted_directors[i][0] + " (" + str(sorted_directors[i][1]) + ")")
        else:
            break
    print("")
