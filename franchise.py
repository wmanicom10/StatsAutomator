import pandas as pd


def print_franchise(box_office_titles):
    franchises = pd.read_excel("franchises.xlsx", dtype=str)
    franchise_columns = ["MCU", "Star Wars", "Jurassic Park", "Pixar", "Fast and Furious", "Harry Potter",
                         "Despicable Me",
                         "DCEU", "Lord of the Rings", "Transformers", "James Bond", "Pirates of the Caribbean",
                         "Ice Age"]
    franchise_counts = {franchise: 0 for franchise in franchise_columns}

    for movie in box_office_titles:
        for franchise in franchise_columns:
            if movie in franchises[franchise].values:
                franchise_counts[franchise] += 1

    sorted_franchise_counts = dict(
        sorted(franchise_counts.items(), key=lambda item: (-item[1], item[0]))
    )

    print("Franchises with 3+ films in the list")
    for franchise, count in sorted_franchise_counts.items():
        if count >= 3:
            print(f"{franchise} ({count})")
    print("")
