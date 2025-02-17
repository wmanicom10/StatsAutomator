def print_fastest_film(fivemillionwatchedclub):
    premiere_days = list(fivemillionwatchedclub["Premiere to 5M"])
    fastest_film_days = int(100000)
    fastest_film_index = int(100000)
    for i in range(len(premiere_days)):
        if int(premiere_days[i]) < int(fastest_film_days):
            fastest_film_days = premiere_days[i]
            fastest_film_index = i

    titles = list(fivemillionwatchedclub["Title"])
    theatrical_days = list(fivemillionwatchedclub["Theatrical to 5M"])
    one_million_days = list(fivemillionwatchedclub["1M to 5M"])
    two_million_days = list(fivemillionwatchedclub["2M to 5M"])
    three_million_days = list(fivemillionwatchedclub["3M to 5M"])
    four_million_days = list(fivemillionwatchedclub["4M to 5M"])

    print("Fastest Film To Be Watched By 5 Million Members")
    print("#" + str(fastest_film_index + 1) + " " + titles[fastest_film_index] + " in " + premiere_days[fastest_film_index] + " days (Premiere)")
    print("#" + str(fastest_film_index + 1) + " " + titles[fastest_film_index] + " in " + theatrical_days[fastest_film_index] + " days (Theatrical Release)")
    print("#" + str(fastest_film_index + 1) + " " + titles[fastest_film_index] + " in " + one_million_days[fastest_film_index] + " days (from 1M to 5M)")
    print("#" + str(fastest_film_index + 1) + " " + titles[fastest_film_index] + " in " + two_million_days[fastest_film_index] + " days (from 2M to 5M)")
    print("#" + str(fastest_film_index + 1) + " " + titles[fastest_film_index] + " in " + three_million_days[fastest_film_index] + " days (from 3M to 5M)")
    print("#" + str(fastest_film_index + 1) + " " + titles[fastest_film_index] + " in " + four_million_days[fastest_film_index] + " days (from 4M to 5M)\n")