from datetime import datetime


def print_header():
    print("List of the Top 100 All-Time Worldwide Box Office films, based on The Numbers\n")

    formatted_date = datetime.now().strftime("%m/%d/%y")
    print("Last Update - " + formatted_date + "\n")

    print("--------------------------------------------------------------------------------------------------------------------")

    print("STATS\n")


def print_actor():
    print("Actors with 8+ films in the list")
    print("Warwick Davis (12)")
    print("Samuel L. Jackson (10)")
    print("Andy Serkis (9)")
    print("Benedict Cumberbatch (8)")
    print("Robert Downey Jr. (8)")
    print("Chris Pratt (8)")
    print("Alan Rickman (8)")
    print("Emma Watson (8)\n")


def print_popular():
    print("Most popular film in the list")
    print("Barbie (2023)\n")
    print("Most obscure film in the list")
    print("Hi, Mom (2021)\n")


def print_billion():
    print("Number of $1 billion films: 54\n")


def print_length():
    print("Longest film in the list")
    print("The Lord of the Rings: The Return of the King - 3 hr 21 min\n")
    print("Shortest film in the list")
    print("The Secret Life of Pets - 1 hr 26 min\n")


def print_release():
    print("Oldest film in the list")
    print("Jurassic Park (1993)\n")
    print("Newest film in the list")
    print("Deadpool & Wolverine (2024)")
