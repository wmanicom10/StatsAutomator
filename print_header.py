from datetime import datetime

def print_header(option):
    if option == 1:
        print("List of the Top 100 All-Time Worldwide Box Office films, based on The Numbers\n")
    elif option == 2:
        print("List of the Top 50 2024 Worldwide Box Office films, based on The Numbers\n")
    elif option == 3:
        print("List of the Top 50 2025 Worldwide Box Office films, based on The Numbers\n")
    elif option == 4:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%B %-d, %Y")
        print("This is a list of the films seen by 5,000,000 individual Letterboxd members, as of " + formatted_date + "\n")
        print("STATS:\n")
        return

    formatted_date = datetime.now().strftime("%m/%d/%y")
    print("Last Update - " + formatted_date + "\n")

    print("--------------------------------------------------------------------------------------------------------------------")

    print("STATS\n")
