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


def print_actor(option):
    if option == 1:
        print("Actors with 9+ films in the list")
        print("Warwick Davis (12)")
        print("Samuel L. Jackson (10)")
        print("Andy Serkis (9)\n")
    elif option == 2:
        print("Actors with 3+ films in the list")
        print("Blake Lively (3)")
        print("Catherine O'Hara (3)")
        print("Kiernan Shipka (3)")
        print("Aaron Taylor-Johnson (3)\n")
    elif option == 3:
        print("Actors with 3+ films in the list\n")


def print_billion():
    print("Number of $1 billion films: 3\n")


def print_length(option):
    if option == 2:
        print("Longest film in the list")
        print("Dune: Part Two - 2 hr 47 min\n")
        print("Shortest film in the list")
        print("Kung Fu Panda 4 - 1 hr 34 min\n")
    elif option == 3:
        print("Longest film in the list")
        print("Den of Thieves 2: Pantera - 2 hr 24 min\n")
        print("Shortest film in the list")
        print("Flight Risk - 1 hr 31 min\n")


def print_release(option):
    if option == 2:
        print("Oldest film in the list")
        print("Night Swim\n")
        print("Newest film in the list")
        print("Sonic the Hedgehog 3")
    elif option == 3:
        print("Oldest film in the list")
        print("Den of Thieves 2: Pantera\n")
        print("Newest film in the list")
        print("Flight Risk")


def print_rating(option):
    if option == 2:
        print("Highest rated film in the list")
        print("Dune: Part Two (4.41)\n")
        print("Lowest rated film in the list")
        print("Madame Web (1.48)\n")
    elif option == 3:
        print("Highest rated film in the list")
        print("One of Them Days (3.62)\n")
        print("Lowest rated film in the list")
        print("Flight Risk (2.21)\n")
