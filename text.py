from datetime import datetime


def print_header():
    print("List of the Top 100 All-Time Worldwide Box Office films, based on The Numbers\n")

    formatted_date = datetime.now().strftime("%m/%d/%y")
    print("Last Update - " + formatted_date + "\n")

    print("--------------------------------------------------------------------------------------------------------------------")

    print("STATS\n")


def print_rating():
    print("Highest rated film in the list")
    print("The Lord of the Rings: The Return of the King (4.51)\n")
    print("Lowest rated film in the list")
    print("Transformers: Age of Extinction (2.04)\n")


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
