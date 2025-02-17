def print_latest_additions(dates_added, titles):
    print("Latest Additions:")

    num_to_display = min(len(titles), 3)

    for i in range(num_to_display):
        print("#" + str(len(titles) - i) + " " + titles[len(titles) - 1 - i] + " on " + dates_added[len(titles) - 1 - i])