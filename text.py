from datetime import datetime


def print_header(option):
    if option == 1:
        print("List of the Top 100 All-Time Worldwide Box Office films, based on The Numbers\n")
    elif option == 2:
        print("List of the Top 50 2024 Worldwide Box Office films, based on The Numbers\n")
    elif option == 3:
        print("List of the Top 50 2025 Worldwide Box Office films, based on The Numbers\n")

    formatted_date = datetime.now().strftime("%m/%d/%y")
    print("Last Update - " + formatted_date + "\n")

    print("--------------------------------------------------------------------------------------------------------------------")

    print("STATS\n")


def print_actor(option):
    if option == 1:
        print("Actors with 8+ films in the list")
        print("Warwick Davis (12)")
        print("Samuel L. Jackson (10)")
        print("Andy Serkis (9)")
        print("Benedict Cumberbatch (8)")
        print("Robert Downey Jr. (8)")
        print("Chris Pratt (8)")
        print("Alan Rickman (8)")
        print("Alan Tudyk (8)")
        print("Emma Watson (8)\n")
    elif option == 2:
        print("Actors with 3+ films in the list")
        print("Blake Lively (3)")
        print("Catherine O'Hara (3)")
        print("Kiernan Shipka (3)")
        print("Aaron Taylor-Johnson (3)\n")
    elif option == 3:
        print("Actors with 3+ films in the list\n")


def print_billion(option):
    if option == 1:
        print("Number of $1 billion films: 55")
        print("Number of $2 billion films: 6\n")
    elif option == 2:
        print("Number of $1 billion films: 3\n")


def print_length(option):
    if option == 1:
        print("Longest film in the list")
        print("The Lord of the Rings: The Return of the King - 3 hr 21 min\n")
        print("Shortest film in the list")
        print("The Secret Life of Pets - 1 hr 26 min\n")
    elif option == 2:
        print("Longest film in the list")
        print("Dune: Part Two - 2 hr 47 min\n")
        print("Shortest film in the list")
        print("Tarot - 1 hr 32 min\n")
    elif option == 3:
        print("Longest film in the list")
        print("Den of Thieves 2: Pantera - 2 hr 24 min\n")
        print("Shortest film in the list")
        print("Flight Risk - 1 hr 31 min\n")


def print_release(option):
    if option == 1:
        print("Oldest film in the list")
        print("Jurassic Park (1993)\n")
        print("Newest film in the list")
        print("Moana 2 (2024)")
    elif option == 2:
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
