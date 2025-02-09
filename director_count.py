from collections import Counter

def print_director_count(lists):
    box_office_directors = list(lists["Box Office Director"])
    box_office_directors_separated = []

    for i in range(100):
        if isinstance(box_office_directors[i], str):
            director = box_office_directors[i]
            if ',' in director:
                index = director.find(',')
                box_office_directors_separated.append(director[:index])
                box_office_directors_separated.append(director[index + 2:])
            else:
                box_office_directors_separated.append(director)

    director_counts = Counter(box_office_directors_separated)
    sorted_directors = sorted(
        director_counts.items(),
        key=lambda x: (-x[1], x[0].split()[-1])
    )

    print("Directors with 4+ films in the list")
    for i in range(len(sorted_directors)):
        if sorted_directors[i][1] > 3:
            print(sorted_directors[i][0] + " (" + str(sorted_directors[i][1]) + ")")
        else:
            break
    print("")
