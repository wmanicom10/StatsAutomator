from datetime import datetime

today = datetime.now()

# Premiere to 5M
premiere_date = datetime(2023, 7, 9)
premiere_date_since = (today - premiere_date).days
print("Premiere to 5M - " + str(premiere_date_since))

# Theatrical to 5M
theatrical_date = datetime(2023, 7, 19)
theatrical_date_since = (today - theatrical_date).days
print("Theatrical to 5M - " + str(theatrical_date_since))

# 1M to 5M
one_million_date = datetime(2023, 7, 30)
one_million_date_since = (today - one_million_date).days
print("1M to 5M - " + str(one_million_date_since))

# 2M to 5M
two_million_date = datetime(2023, 10, 20)
two_million_date_since = (today - two_million_date).days
print("2M to 5M - " + str(two_million_date_since))

# 3M to 5M
three_million_date = datetime(2024, 2, 9)
three_million_date_since = (today - three_million_date).days
print("3M to 5M - " + str(three_million_date_since))

# 4M to 5M
four_million_date = datetime(2024, 8, 24)
four_million_date_since = (today - four_million_date).days
print("4M to 5M - " + str(four_million_date_since))