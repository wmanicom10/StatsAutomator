from datetime import datetime

def print_latest_additions(dates_added, titles, option):
    if option == 1:
        print("Latest Additions:")

        num_to_display = min(len(titles), 3)

        formatted_dates = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%B %d, %Y') for date in dates_added]

        for i in range(num_to_display):
            print("#" + str(len(titles) - i) + " " + titles[i] + " on " + formatted_dates[i])

    elif option == 2:
        print("Latest Addition")

        num_to_display = min(len(dates_added), 1)

        formatted_dates = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%B %d, %Y') for date in dates_added]

        for i in range(num_to_display):
            print("#" + str(len(titles) - i) + " " + titles[i] + " on " + formatted_dates[i] + "\n")