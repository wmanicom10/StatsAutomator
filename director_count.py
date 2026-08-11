from collections import Counter

def print_director_count(lists, option):
    if option == 1:
        box_office_directors = list(lists["Box Office Director"])
        box_office_directors_separated = []

        for i in range(100):
            if isinstance(box_office_directors[i], str):
                director = box_office_directors[i]
                if ',' in director:
                    names = [name.strip() for name in director.split(',')]
                    box_office_directors_separated.extend(names)
                else:
                    box_office_directors_separated.append(director)

        director_counts = Counter(box_office_directors_separated)
        sorted_directors = sorted(
            director_counts.items(),
            key=lambda x: (-x[1], x[0].split()[-1])
        )

        print("Directors with 3+ films in the list")
        qualifying = []
        for i in range(len(sorted_directors)):
            if sorted_directors[i][1] >= 3:
                qualifying.append(sorted_directors[i][0] + " (" + str(sorted_directors[i][1]) + ")")
            else:
                break
        print(", ".join(qualifying))
        print("")

    if option == 2:
        five_million_directors = lists
        five_million_directors_separated = []

        for i in range(len(five_million_directors)):
            if isinstance(five_million_directors[i], str):
                director = five_million_directors[i]
                if ',' in director:
                    names = [name.strip() for name in director.split(',')]
                    five_million_directors_separated.extend(names)
                else:
                    five_million_directors_separated.append(director)

        director_counts = Counter(five_million_directors_separated)
        sorted_directors = sorted(
            director_counts.items(),
            key=lambda x: (-x[1], x[0].split()[-1], x[0].split()[0])
        )

        directors_output = [sorted_directors[i][0] + " (" + str(sorted_directors[i][1]) + ")" for i in
                            range(len(sorted_directors)) if sorted_directors[i][1] >= 2]
        print("Directors with 2+ films in the list")
        print(", ".join(directors_output))
        print("")

    if option == 3:
        print("Directors with 2+ films in the list")
        print("")

    if option == 4:
        two_billion_directors = lists
        two_billion_directors_separated = []

        for i in range(len(two_billion_directors)):
            if isinstance(two_billion_directors[i], str):
                director = two_billion_directors[i]
                if ',' in director:
                    names = [name.strip() for name in director.split(',')]
                    two_billion_directors_separated.extend(names)
                else:
                    two_billion_directors_separated.append(director)

        director_counts = Counter(two_billion_directors_separated)
        sorted_directors = sorted(
            director_counts.items(),
            key=lambda x: (-x[1], x[0].split()[-1], x[0].split()[0])
        )

        directors_output = [sorted_directors[i][0] + " (" + str(sorted_directors[i][1]) + ")" for i in
                            range(len(sorted_directors)) if sorted_directors[i][1] >= 2]
        print("Directors with 2+ films in the list")
        print(", ".join(directors_output))
        print("")