import pandas as pd

lists = pd.read_excel("spreadsheets/oscars.xlsx", dtype=str)

def print_best_picture_count(box_office_titles, box_office_years, option):
    best_picture_titles = list(lists["Best Picture Name"])

    best_picture_counter = 0
    best_pictures = []

    for i in range(len(box_office_titles)):
        if box_office_titles[i] in best_picture_titles:
            if (box_office_titles[i], box_office_years[i]) not in best_pictures:
                best_pictures.append((box_office_titles[i], box_office_years[i]))
                best_picture_counter += 1

    best_pictures_sorted = sorted(best_pictures, key=lambda x: x[1])
    best_pictures_formatted = ', '.join(f"{title} ({int(year) + 1})" for title, year in best_pictures_sorted)

    print("Number of Best Picture Winners in the list: " + str(best_picture_counter))
    if option == 1:
        print(best_pictures_formatted + "\n")
    elif option == 4:
        print(best_pictures_formatted)


def print_best_animated_feature_count(box_office_titles, box_office_years):
    best_animated_feature_titles = list(lists["Best Animated Feature Name"])

    best_animated_feature_counter = 0
    best_animated_features = []

    for i in range(100):
        if box_office_titles[i] in best_animated_feature_titles:
            if (box_office_titles[i], box_office_years[i]) not in best_animated_features:
                best_animated_features.append((box_office_titles[i], box_office_years[i]))
                best_animated_feature_counter += 1

    best_animated_features_sorted = sorted(best_animated_features, key=lambda x: x[1])
    best_animated_features_formatted = ', '.join(f"{title} ({int(year) + 1})" for title, year in best_animated_features_sorted)

    print("Number of Best Animated Feature Winners in the list: " + str(best_animated_feature_counter))
    print(best_animated_features_formatted + "\n")


def print_best_picture_nominees(box_office_titles, box_office_years):
    best_picture_nominees_titles = list(lists["Best Picture Nominated Name"])

    best_picture_nominees = []

    for i in range(50):
        if box_office_titles[i] in best_picture_nominees_titles:
            if (box_office_titles[i], box_office_years[i]) not in best_picture_nominees:
                best_picture_nominees.append(box_office_titles[i])

    best_pictures_sorted = sorted(best_picture_nominees, key=lambda x: remove_articles(x[0]))

    print("Best Picture Nominees in the list: ")
    print(', '.join(best_pictures_sorted))


def remove_articles(title):
    articles = ("A ", "An ", "The ")
    for article in articles:
        if title.startswith(article):
            return title[len(article):]
    return title

def print_best_director_count(titles, years):
    best_director_titles = list(lists["Best Director Title"])
    best_director_names = list(lists["Best Director Name"])

    best_director_counter = 0
    best_director = []

    for i in range(len(titles)):
        if titles[i] in best_director_titles:
            index = best_director_titles.index(titles[i])
            best_director_name = best_director_names[index]
            if (titles[i], years[i]) not in best_director:
                best_director.append((titles[i], years[i], best_director_name))
                best_director_counter += 1

    best_director_sorted = sorted(best_director, key=lambda x: x[1])
    best_director_formatted = ', '.join(f"{name} ({title}, {int(year) + 1})" for title, year, name in best_director_sorted)

    print("Number of Best Directors Winners: " + str(best_director_counter))
    print(best_director_formatted)
