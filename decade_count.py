def print_decade_count(years, option):
    decades = {"1980s": 0, "1990s": 0, "2000s": 0, "2010s": 0, "2020s": 0}

    for year in map(int, years):
        if 1980 <= year <= 1989:
            decades["1980s"] += 1
        elif 1990 <= year <= 1999:
            decades["1990s"] += 1
        elif 2000 <= year <= 2009:
            decades["2000s"] += 1
        elif 2010 <= year <= 2019:
            decades["2010s"] += 1
        elif 2020 <= year <= 2029:
            decades["2020s"] += 1

    if option == 1:
        print("Number of films per decade")
        entries = [f"{decade} ({count})" for decade, count in decades.items() if count > 0]
        print(", ".join(entries))
        print()
    elif option == 2:
        print("Number Of Films Per Decade:")
        decade_output = [f"{decade} ({count})" for decade, count in decades.items() if count]
        print(", ".join(decade_output))
        print("")