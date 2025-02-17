from datetime import datetime

def add_ordinal_suffix(day):
    if 11 <= day <= 13:  # Special cases for 11th, 12th, and 13th
        return f"{day}th"
    last_digit = day % 10
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(last_digit, "th")
    return f"{day}{suffix}"

def print_header(option):
    if option == 1:
        print("List of the Top 100 All-Time Worldwide Box Office films, based on The Numbers\n")
    elif option == 2:
        print("List of the Top 50 2024 Worldwide Box Office films, based on The Numbers\n")
    elif option == 3:
        print("List of the Top 50 2025 Worldwide Box Office films, based on The Numbers\n")
    elif option == 4:
        current_date = datetime.now()
        day = current_date.day
        formatted_date = f"{current_date.strftime('%B')} {add_ordinal_suffix(day)}, {current_date.year}"
        print("This is a list of the films seen by 5,000,000 individual Letterboxd members, as of " + formatted_date + "\n")
        return

    formatted_date = datetime.now().strftime("%m/%d/%y")
    print("Last Update - " + formatted_date + "\n")

    print("--------------------------------------------------------------------------------------------------------------------")

    print("STATS\n")
