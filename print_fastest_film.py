import math

def print_fastest_film(club, option):
    if option == 1:
        titles = list(club["Title"])
        premiere_days = list(club["Premiere to 5M"])
        theatrical_days = list(club["Theatrical to 5M"])
        one_million_days = list(club["1M to 5M"])
        two_million_days = list(club["2M to 5M"])
        three_million_days = list(club["3M to 5M"])
        four_million_days = list(club["4M to 5M"])

        # Find fastest for each category
        categories = [
            ("Premiere", premiere_days),
            ("Theatrical Release", theatrical_days),
            ("from 1M to 5M", one_million_days),
            ("from 2M to 5M", two_million_days),
            ("from 3M to 5M", three_million_days),
            ("from 4M to 5M", four_million_days)
        ]

        print("Fastest Film To Be Watched By 5 Million Members")

        for category_name, days_list in categories:
            fastest_days = int(100000)
            fastest_index = 0

            for i in range(len(days_list)):
                try:
                    days_list[i] = int(float(days_list[i]))
                except (ValueError, TypeError):
                    days_list[i] = 999999
                    continue

                if math.isnan(days_list[i]):
                    days_list[i] = 999999

                if int(days_list[i]) < fastest_days:
                    fastest_days = int(days_list[i])
                    fastest_index = i

            print(
                f"#{len(premiere_days) - fastest_index} {titles[fastest_index]} in {days_list[fastest_index]} days ({category_name})")

        print()

    elif option == 2:
        titles = list(club["Title"])
        theatrical_days = list(club["Theatrical to $2B"])

        categories = [
            ("Theatrical Release", theatrical_days)
        ]

        print("Fastest films to cross $2 Billion")

        for category_name, days_list in categories:
            for i in range(len(days_list)):
                try:
                    val = int(float(days_list[i]))
                    if math.isnan(float(days_list[i])):
                        val = 999999
                except (ValueError, TypeError):
                    val = 999999
                days_list[i] = val

            sorted_indices = sorted(range(len(days_list)), key=lambda i: days_list[i])[:5]

            for rank, idx in enumerate(sorted_indices, start=1):
                original_rank = len(titles) - idx
                print(f"{rank}. #{original_rank} {titles[idx]} in {days_list[idx]} days")

        print()