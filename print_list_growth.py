from datetime import datetime

def print_list_growth(dates_added):
    count_2025 = sum(1 for date in dates_added if datetime.strptime(date, '%Y-%m-%d %H:%M:%S').year == 2025)
    count_2026 = sum(1 for date in dates_added if datetime.strptime(date, '%Y-%m-%d %H:%M:%S').year == 2026)

    print("\nList Growth Each Year:")
    print("Films added in 2025: " + str(count_2025))
    print("Films added in 2026: " + str(count_2026) + "*\n")