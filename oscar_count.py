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

    if best_picture_counter == 0:
        return
    if option == 1:
        print("Number of Best Picture Winners in the list: " + str(best_picture_counter))
        best_pictures_sorted = sorted(best_pictures, key=lambda x: x[1])
        best_pictures_formatted = ', '.join(f"{title} ({int(year) + 1})" for title, year in best_pictures_sorted)
        print(best_pictures_formatted + "\n")
    elif option == 4:
        print("Number of Best Picture Winners: " + str(best_picture_counter))
        best_pictures_sorted = [(f'#{len(box_office_titles) - box_office_titles.index(title)}', title, year) for i, (title, year) in enumerate(best_pictures)]
        best_pictures_sorted = sorted(best_pictures_sorted, key=lambda x: int(x[0][1:]))
        best_pictures_formatted = ', '.join(f"{index} {title} ({int(year) + 1})" for index, title, year in best_pictures_sorted)
        print(best_pictures_formatted)

def print_best_animated_feature_count(box_office_titles, box_office_years, option):
    best_animated_feature_titles = list(lists["Best Animated Feature Name"])

    best_animated_feature_counter = 0
    best_animated_features = []

    for i in range(len(box_office_titles)):
        if box_office_titles[i] in best_animated_feature_titles:
            if (box_office_titles[i], box_office_years[i]) not in best_animated_features:
                best_animated_features.append((box_office_titles[i], box_office_years[i]))
                best_animated_feature_counter += 1

    if option == 1:
        best_animated_features_sorted = sorted(best_animated_features, key=lambda x: x[1])
        best_animated_features_formatted = ', '.join(f"{title} ({int(year) + 1})" for title, year in best_animated_features_sorted)

        print("Number of Best Animated Feature Winners in the list: " + str(best_animated_feature_counter))
        print(best_animated_features_formatted + "\n")
    if option == 2:
        print("Number of Best Animated Feature Winners: " + str(best_animated_feature_counter))
        best_animated_features_sorted = [(f'#{len(box_office_titles) - box_office_titles.index(title)}', title, year) for i, (title, year) in enumerate(best_animated_features)]
        best_animated_features_sorted = sorted(best_animated_features_sorted, key=lambda x: int(x[0][1:]))
        best_animated_features_formatted = ', '.join(f"{index} {title} ({int(year) + 1})" for index, title, year in best_animated_features_sorted)
        print(best_animated_features_formatted)

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

def print_best_director_count(titles, years):
    best_director_titles = list(lists["Best Director Title"])
    best_director_names = list(lists["Best Director Name"])

    best_director_counter = 0
    best_directors = []

    for i in range(len(titles)):
        if titles[i] in best_director_titles:
            index = best_director_titles.index(titles[i])
            best_director_name = best_director_names[index]
            if (titles[i], years[i]) not in best_directors:
                best_directors.append((titles[i], years[i], best_director_name))
                best_director_counter += 1

    print("Number of Best Directors Winners: " + str(best_director_counter))

    if best_director_counter == 0:
        return

    best_directors_sorted = [(f'#{len(titles) - titles.index(title)}', title, year, director) for i, (title, year, director) in enumerate(best_directors)]
    best_directors_sorted = sorted(best_directors_sorted, key=lambda x: int(x[0][1:]))
    best_directors_formatted = ', '.join(f"{director} ({index} {title}, {int(year)+1})" for index, title, year, director in best_directors_sorted)
    print(best_directors_formatted)

def print_best_actor_count(titles, years):
    best_actor_titles = list(lists["Best Actor Title"])
    best_actor_names = list(lists["Best Actor Name"])

    best_actor_counter = 0
    best_actors = []

    for i in range(len(titles)):
        if titles[i] in best_actor_titles:
            index = best_actor_titles.index(titles[i])
            best_actor_name = best_actor_names[index]
            if (titles[i], years[i]) not in best_actors:
                best_actors.append((titles[i], years[i], best_actor_name))
                best_actor_counter += 1

    print("Number of Best Actors Winners: " + str(best_actor_counter))

    if best_actor_counter == 0:
        return

    best_actors_sorted = [(f'#{len(titles) - titles.index(title)}', title, year, actor) for i, (title, year, actor) in enumerate(best_actors)]
    best_actors_sorted = sorted(best_actors_sorted, key=lambda x: int(x[0][1:]))
    best_actors_formatted = ', '.join(f"{actor} ({index} {title}, {int(year)+1})" for index, title, year, actor in best_actors_sorted)
    print(best_actors_formatted)

def print_best_actress_count(titles, years):
    best_actress_titles = list(lists["Best Actress Title"])
    best_actress_names = list(lists["Best Actress Name"])

    best_actress_counter = 0
    best_actresses = []

    for i in range(len(titles)):
        if titles[i] in best_actress_titles:
            index = best_actress_titles.index(titles[i])
            best_actor_name = best_actress_names[index]
            if (titles[i], years[i]) not in best_actresses:
                best_actresses.append((titles[i], years[i], best_actor_name))
                best_actress_counter += 1

    print("Number of Best Actress Winners: " + str(best_actress_counter))

    if best_actress_counter == 0:
        return

    best_actresses_sorted = [(f'#{len(titles) - titles.index(title)}', title, year, actress) for i, (title, year, actress) in enumerate(best_actresses)]
    best_actresses_sorted = sorted(best_actresses_sorted, key=lambda x: int(x[0][1:]))
    best_actresses_formatted = ', '.join(f"{actress} ({index} {title}, {int(year)+1})" for index, title, year, actress in best_actresses_sorted)
    print(best_actresses_formatted)