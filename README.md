# StatsAutomator

A Python tool that generates formatted stats for Letterboxd lists, designed to automate the process of updating list descriptions with current data.

## What It Does

For each list, the tool scrapes Letterboxd and cross-references spreadsheet data to produce a list description including stats like top-rated, most popular, longest/shortest films, and more.

## Supported Lists

1. **Top 100 All-Time Worldwide Box Office** — https://boxd.it/xEjVy
2. **Top 50 2025 Worldwide Box Office** — https://boxd.it/Nefn0
3. **Top 50 2026 Worldwide Box Office** — https://boxd.it/RG9tI
4. **Letterboxd Five Million Watched Club** - https://boxd.it/DY2Eu

## Project Structure

```
StatsAutomator/
├── app.py                              # Streamlit web GUI
├── main.py                             # CLI entry point
├── actor_count.py                      # Actor counts per list
├── billion_count.py                    # Scrapes $1B/$2B film counts
├── decade_count.py                     # Films per decade
├── director_count.py                   # Director film counts
├── franchise_count.py                  # Franchise film counts
├── get_days_since.py                   # Calculates days between milestone dates
├── list_count.py                       # Cross-references films against watched club lists
├── list_order.py                       # Scrapes highest/lowest rated, popular, longest, oldest
├── next_to_join.py                     # Scrapes next films close to 5M watches
├── oscar_count.py                      # Best Picture, Animated Feature, Director, Actor, Actress counts
├── print_fastest_film.py               # Fastest film to reach 5M watches
├── print_first_film.py                 # First film to reach 5M watches
├── print_five_million_watched_club.py  # Five Million Watched Club output
├── print_header.py                     # List header/description text
├── print_latest_additions.py           # Most recently added films
├── print_list_growth.py                # Films added per year
├── print_top_50_2025.py                # 2025 box office output
├── print_top_50_2026.py                # 2026 box office output
├── print_top_100_all_time_worldwide.py # All-time box office output
├── year_count.py                       # Films per year
└── spreadsheets/
    ├── fivemillionwatchedclub.xlsx     # Five Million Watched Club data
    ├── franchises.xlsx                 # Franchise data
    ├── lists.xlsx                      # Box office, watched club, IMDb, Letterboxd data
    └── oscars.xlsx                     # Oscar winners and nominees
```

## Spreadsheets

The `spreadsheets` folder contains the data files the project reads from. These need to be kept up to date manually.

| File                          | Description                                                                                                                                              |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fivemillionwatchedclub.xlsx` | Films in the Five Million Watched Club with film data, milestone dates (premiere, theatrical release, 1M, 2M, 3M, 4M watches) and date added to the list |                              |                                                                                                                                               |
| `franchises.xlsx`             | Franchise data from various franchises in the Top 100 Worldwide Box Office list                                                                          |
| `lists.xlsx`                  | Box office data, plus data for the Letterboxd watched clubs, IMDb Top 250, and Letterboxd Top 500                                                        |
| `oscars.xlsx`                 | Oscar winners and nominees for Best Picture, Best Animated Feature, Best Director, Best Actor, and Best Actress                                          |

## Getting Started

Install dependencies:
```bash
pip install pandas openpyxl requests beautifulsoup4 cloudscraper streamlit
```

## Running
 
### Web GUI
 
```bash
streamlit run app.py
```
 
This opens a browser window with a tab for each list. Click **Load Stats** on any tab to fetch and display the stats for that list.
 
### Command Line
 
```bash
python main.py
```
 
You'll be prompted to select a list:
```
Which list would you like?
1. Top 100 All-Time Worldwide
2. Top 50 2025
3. Top 50 2026
4. Letterboxd Five Million Watched Club
Enter an option:
```
 
The output is printed directly to the console.

## Notes

- Letterboxd's API is not publicly available for personal projects, so scraping is used instead
- `cloudscraper` is used to handle Cloudflare bot protection
- Requests include automatic retry logic with exponential backoff for 403/429 responses