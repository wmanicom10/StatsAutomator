def print_decade_count(years, option):
    decades = {"1990s": 0, "2000s": 0, "2010s": 0, "2020s": 0}

    for year in map(int, years):
        if 1990 <= year <= 1999:
            decades["1990s"] += 1
        elif 2000 <= year <= 2009:
            decades["2000s"] += 1
        elif 2010 <= year <= 2019:
            decades["2010s"] += 1
        elif 2020 <= year <= 2029:
            decades["2020s"] += 1

    if option == 1:
        print("Films in the list per decade")
        for decade, count in decades.items():
            print(f"{decade} - {count}")
        print()
    elif option == 4:
        print("Number Of Films Per Decade:")
        for decade, count in decades.items():
            if count:
                print(f"{decade} ({count})")
