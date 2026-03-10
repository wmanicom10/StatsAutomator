import pandas as pd

def print_franchise_count(box_office_titles):
    franchises = pd.read_excel("spreadsheets/franchises.xlsx", dtype=str)
    franchise_columns = franchises.columns.tolist()
    franchise_counts = {franchise: 0 for franchise in franchise_columns}

    for movie in box_office_titles:
        for franchise in franchise_columns:
            if movie in franchises[franchise].values:
                franchise_counts[franchise] += 1

    franchise_counts['Disney'] = franchise_counts['Disney'] - 6
    franchise_counts['Disney Live Action Remakes'] = franchise_counts['Disney Live Action Remakes'] - 1

    sorted_franchise_counts = dict(
        sorted(franchise_counts.items(), key=lambda item: (-item[1], item[0]))
    )

    print("Franchises with 5+ films in the list")
    for franchise, count in sorted_franchise_counts.items():
        if count >= 5:
            print(f"{franchise} ({count})")
    print("")
