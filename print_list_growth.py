def print_list_growth(dates_added):
    years = [int(date.split()[-1]) for date in dates_added]

    count_2025 = 0

    for year in years:
        if year == 2025:
            count_2025 += 1

    print("\nList Growth Each Year:")
    print("Films added in 2025: " + str(count_2025) + "*")