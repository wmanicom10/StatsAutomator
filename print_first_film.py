def print_first_film(club, option):
    if option == 1:
        premiere_days = list(club["Premiere to 5M"])
        theatrical_days = list(club["Theatrical to 5M"])
        one_million_days = list(club["1M to 5M"])
        two_million_days = list(club["2M to 5M"])
        three_million_days = list(club["3M to 5M"])
        four_million_days = list(club["4M to 5M"])

        print("First Film To Be Watched By 5 Million Members:")
        print("#1 Barbie in " + premiere_days[len(premiere_days) - 1] + " days (Premiere)")
        print("#1 Barbie in " + theatrical_days[len(theatrical_days) - 1] + " days (Theatrical Release)")
        print("#1 Barbie in " + one_million_days[len(one_million_days) - 1] + " days (from 1M to 5M)")
        print("#1 Barbie in " + two_million_days[len(two_million_days) - 1] + " days (from 2M to 5M)")
        print("#1 Barbie in " + three_million_days[len(three_million_days) - 1] + " days (from 3M to 5M)")
        print("#1 Barbie in " + four_million_days[len(four_million_days) - 1] + " days (from 4M to 5M)\n")

    elif option == 2:
        print("First film to cross $2 Billion")
        print("#1 Avatar on January 31, 2010\n")