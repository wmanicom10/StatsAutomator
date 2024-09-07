
def print_decade(box_office_years):
    nineties = thousands = tens = twenties = 0

    for i in range(100):
        year = int(box_office_years[i])
        if 1990 <= year <= 1999:
            nineties += 1
        elif 2000 <= year <= 2009:
            thousands += 1
        elif 2010 <= year <= 2019:
            tens += 1
        elif 2020 <= year <= 2029:
            twenties += 1

    print("Films in the list per decade")
    print("1990s - " + str(nineties))
    print("2000s - " + str(thousands))
    print("2010s - " + str(tens))
    print("2020s - " + str(twenties) + "\n")
