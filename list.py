import pandas as pd


def print_list(box_office_titles, box_office_years):
    lists = pd.read_excel("lists.xlsx", dtype=str)

    lists_dict = {
        "one_million": {
            "titles": list(lists["One Million Title"]),
            "years": list(lists["One Million Year"]),
            "count": 0
        },
        "two_million": {
            "titles": list(lists["Two Million Title"]),
            "years": list(lists["Two Million Year"]),
            "count": 0
        },
        "three_million": {
            "titles": list(lists["Three Million Title"]),
            "years": list(lists["Three Million Year"]),
            "count": 0
        },
        "four_million": {
            "titles": list(lists["Four Million Title"]),
            "years": list(lists["Four Million Year"]),
            "count": 0
        },
        "imdb": {
            "titles": list(lists["IMDb Title"]),
            "years": list(lists["IMDb Year"]),
            "count": 0
        },
        "letterboxd": {
            "titles": list(lists["Letterboxd Title"]),
            "years": list(lists["Letterboxd Year"]),
            "count": 0
        }
    }

    # Process the box office lists
    for i in range(len(box_office_titles)):
        for key, value in lists_dict.items():
            titles = value["titles"]
            years = value["years"]
            if len(titles) == len(years):
                for j in range(len(titles)):
                    if box_office_titles[i] == titles[j] and box_office_years[i] == years[j]:
                        value["count"] += 1

    # Printing number of films in each list
    print("Number of films in the Letterboxd One Million Watched Club: " + str(lists_dict["one_million"]["count"]))
    print("Number of films in the Letterboxd Two Million Watched Club: " + str(lists_dict["two_million"]["count"]))
    print("Number of films in the Letterboxd Three Million Watched Club: " + str(lists_dict["three_million"]["count"]))
    print("Number of films in the Letterboxd Four Million Watched Club: " + str(lists_dict["four_million"]["count"]))
    print("Number of films in the IMDb Top 250: " + str(lists_dict["imdb"]["count"]))
    print("Number of films in the Letterboxd Top 250: " + str(lists_dict["letterboxd"]["count"]) + "\n")
