from datetime import datetime

today = datetime(2026, 7, 3)

# Premiere to 5M
premiere_date = datetime(2001, 4, 22)
premiere_date_since = (today - premiere_date).days
print("Premiere to 5M - " + str(premiere_date_since + 1))

# Theatrical to 5M
theatrical_date = datetime(2001, 5, 18)
theatrical_date_since = (today - theatrical_date).days
print("Theatrical to 5M - " + str(theatrical_date_since + 1))

# 1M to 5M
one_million_date = datetime(2022, 3, 24)
one_million_date_since = (today - one_million_date).days
print("1M to 5M - " + str(one_million_date_since + 1))

# 2M to 5M
two_million_date = datetime(2023, 12, 16)
two_million_date_since = (today - two_million_date).days
print("2M to 5M - " + str(two_million_date_since + 1))

# 3M to 5M
three_million_date = datetime(2024, 12, 31)
three_million_date_since = (today - three_million_date).days
print("3M to 5M - " + str(three_million_date_since + 1))

# 4M to 5M
four_million_date = datetime(2025, 10, 24)
four_million_date_since = (today - four_million_date).days
print("4M to 5M - " + str(four_million_date_since + 1))