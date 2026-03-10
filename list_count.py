def print_list_count(lists, box_office_titles, box_office_years, option):
    if option != 4:
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
            "five_million": {
                "titles": list(lists["Five Million Title"]),
                "years": list(lists["Five Million Year"]),
                "count": 0
            },
            "six_million": {
                "titles": list(lists["Six Million Title"]),
                "years": list(lists["Six Million Year"]),
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
            },
            "box_office": {
                "titles": list(lists["Box Office Title"]),
                "years": list(lists["Box Office Year"]),
                "count": 0
            }
        }

        for i in range(len(box_office_titles)):
            for key, value in lists_dict.items():
                titles = value["titles"]
                years = value["years"]
                if len(titles) == len(years):
                    for j in range(len(titles)):
                        if box_office_titles[i] == titles[j] and box_office_years[i] == years[j]:
                            value["count"] += 1

        print("Number of films in the Letterboxd One Million Watched Club: " + str(lists_dict["one_million"]["count"]))
        print("Number of films in the Letterboxd Two Million Watched Club: " + str(lists_dict["two_million"]["count"]))
        print("Number of films in the Letterboxd Three Million Watched Club: " + str(lists_dict["three_million"]["count"]))
        print("Number of films in the Letterboxd Four Million Watched Club: " + str(lists_dict["four_million"]["count"]))
        print("Number of films in the Letterboxd Five Million Watched Club: " + str(lists_dict["five_million"]["count"]))
        print("Number of films in the Letterboxd Six Million Watched Club: " + str(lists_dict["six_million"]["count"]))
        if option == 2 or option == 3:
            print("Number of films in the Top 100 All-Time Worldwide Box Office List: " + str(lists_dict["box_office"]["count"]))
        print("Number of films in the IMDb Top 250: " + str(lists_dict["imdb"]["count"]))
        print("Number of films in the Letterboxd Top 500: " + str(lists_dict["letterboxd"]["count"]) + "\n")
    elif option == 4:
        lists_dict = {
            "letterboxd": {
                "titles": list(lists["Letterboxd Title"]),
                "years": list(lists["Letterboxd Year"]),
                "count": 0,
            },
            "imdb": {
                "titles": list(lists["IMDb Title"]),
                "years": list(lists["IMDb Year"]),
                "count": 0,
            },
            "box_office": {
                "titles": list(lists["Box Office Title"]),
                "years": list(lists["Box Office Year"]),
                "count": 0,
            }
        }

        for i in range(len(box_office_titles)):
            for key, value in lists_dict.items():
                titles = value["titles"]
                years = value["years"]
                if len(titles) == len(years):
                    for j in range(len(titles)):
                        if box_office_titles[i] == titles[j] and box_office_years[i] == years[j]:
                            value["count"] += 1

        print("Number of films in the Letterboxd Top 500: " + str(lists_dict["letterboxd"]["count"]))
        print("Number of films in the IMDb Top 250: " + str(lists_dict["imdb"]["count"]))
        print("Number of films in the All-Time Worldwide Box Office List: " + str(lists_dict["box_office"]["count"]))

