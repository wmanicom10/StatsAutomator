
def print_decade(years, option):
    nineties = thousands = tens = twenties = 0

    for i in range(len(years)):
        year = int(years[i])
        if 1990 <= year <= 1999:
            nineties += 1
        elif 2000 <= year <= 2009:
            thousands += 1
        elif 2010 <= year <= 2019:
            tens += 1
        elif 2020 <= year <= 2029:
            twenties += 1

    if option == 1:
        print("Films in the list per decade")
        print("1990s - " + str(nineties))
        print("2000s - " + str(thousands))
        print("2010s - " + str(tens))
        print("2020s - " + str(twenties) + "\n")
    elif option == 4:
        print("Number Of Films Per Decade:")
        if nineties != 0:
            print("1990s (" + str(nineties) + ")")
        if thousands != 0:
            print("2000s (" + str(thousands) + ")")
        if tens != 0:
            print("2010s (" + str(tens) + ")")
        if twenties != 0:
            print("2020s (" + str(twenties) + ")")
