from collections import Counter
import math

def print_year_count(box_office_years):
    clean_years = [year for year in box_office_years if not (isinstance(year, float) and math.isnan(year))]
    year_counts = Counter(clean_years)
    sorted_year_counts = sorted(year_counts.items(), key=lambda x: (-x[1], -int(x[0])))

    print("Years with 6+ films in the list")
    for year, count in sorted_year_counts:
        if count >= 6:
            print(f"{year} ({count})")
    print("")
