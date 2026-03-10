from datetime import datetime

def print_header(option):
    if option == 1:
        print("\nAll Time Worldwide Box Office - Top 100\n")
        print("This is a list of the Top 100 All-Time Worldwide Box Office films, based on The Numbers. Updated weekly.\n")
    elif option == 2:
        print("\n2025 Worldwide Box Office - Top 50\n")
        print("This is a list of the Top 50 Worldwide Box Office films in 2025, based on The Numbers. Updated weekly.\n")
    elif option == 3:
        current_date = datetime.now()
        day = current_date.day
        formatted_date = f"{current_date.strftime('%B')} {day}, {current_date.year}"
        print("\nLetterboxd Five Million Watched Club\n")
        print("This is a list of the films seen by 5,000,000 individual Letterboxd members, as of " + formatted_date + ".\n")
        return
    elif option == 4:
        print("\n2026 Worldwide Box Office - Top 50\n")
        print("This is a list of the Top 50 Worldwide Box Office films in 2026, based on The Numbers. Updated weekly.\n")

    formatted_date = datetime.now().strftime("%m/%d/%y")
    print("Last Update - " + formatted_date + "\n")

    print("--------------------------------------------------------------------------------------------------------------------")

    print("STATS\n")
