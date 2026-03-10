from print_top_100_all_time_worldwide import print_top_100_all_time_worldwide
from print_top_50_2025 import print_top_50_2025
from print_top_50_2026 import print_top_50_2026
from print_five_million_watched_club import print_five_million_watched_club

print("Which list would you like?")
print("1. Top 100 All-Time Worldwide")
print("2. Top 50 2025")
print("3. Top 50 2026")
print("4. Letterboxd Five Million Watched Club")
option = input("Enter an option: ")

# Top 100 All-Time Worldwide Box Office
if option == "1":
    print_top_100_all_time_worldwide()

# Top 50 2025 Box Office
elif option == "2":
    print_top_50_2025()

# Top 50 2026 Box Office
elif option == "3":
    print_top_50_2026()

# Letterboxd Five Million Watched Club
elif option == "4":
    print_five_million_watched_club()