from datetime import datetime

def generate_dates(year_min, year_max, day):
    dates = []
    for year in range(year_min, year_max + 1):
        for month in range(1, 13):
            dates.append((year, month, day))
    return dates

def check_weekday(date, weekday):
    return datetime(*date).weekday() == weekday

def check_all(three = False):
    year_min = int(input("Year min: "))
    year_max = int(input("Year max: "))
    monthday = int(input("Day of the month: "))
    weekday = int(input("Weekday (Mo = 0 - So = 6): "))
    dates = generate_dates(year_min, year_max, monthday)
    list = [day for day in dates if check_weekday(day, weekday)]
    for year in range(year_min, year_max + 1):
        days = [day for day in list if day[0] == year]
        if three and len(days) < 3:
            continue
        print(f"{year}: {len(days)}")
        for day in days:
            print(f"\t{day[2]}.{day[1]}.{day[0]}")
        print()

check_all(True)
