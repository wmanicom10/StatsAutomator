import pandas as pd

lists = pd.read_excel("oscars.xlsx", dtype=str)


def print_best_picture(box_office_titles, box_office_years):
    best_picture_titles = list(lists["Best Picture Name"])

    best_picture_counter = 0
    best_pictures = []

    for i in range(len(box_office_titles)):
        if box_office_titles[i] in best_picture_titles:
            if (box_office_titles[i], box_office_years[i]) not in best_pictures:
                best_pictures.append((box_office_titles[i], box_office_years[i]))
                best_picture_counter += 1

    best_pictures_sorted = sorted(best_pictures, key=lambda x: x[1])
    best_pictures_formatted = ', '.join(f"{title} ({year})" for title, year in best_pictures_sorted)

    print("Number of Best Picture Winners in the list: " + str(best_picture_counter))
    print(best_pictures_formatted + "\n")


def print_best_animated_feature(box_office_titles, box_office_years):
    best_animated_feature_titles = list(lists["Best Animated Feature Name"])

    best_animated_feature_counter = 0
    best_animated_features = []

    for i in range(100):
        if box_office_titles[i] in best_animated_feature_titles:
            if (box_office_titles[i], box_office_years[i]) not in best_animated_features:
                best_animated_features.append((box_office_titles[i], box_office_years[i]))
                best_animated_feature_counter += 1

    best_animated_features_sorted = sorted(best_animated_features, key=lambda x: x[1])
    best_animated_features_formatted = ', '.join(f"{title} ({year})" for title, year in best_animated_features_sorted)

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
    print(', '.join(best_pictures_sorted) + "\n")


def remove_articles(title):
    articles = ("A ", "An ", "The ")
    for article in articles:
        if title.startswith(article):
            return title[len(article):]
    return title

