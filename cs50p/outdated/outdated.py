months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
        date_input = input("Date: ").strip()

        try:
            month, day, year = date_input.split("/")
            month, day, year = int(month), int(day), int(year)
            if (int(month) >= 1 and int(month) <=12) and (int(day) >= 1 and int(day) <= 31):
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
        except ValueError:
            pass

        try:
            alt_month, alt_day, alt_year = date_input.split(" ", 2)
            if not alt_day.endswith(","):
                 continue
            alt_day = alt_day.replace(",", "")
            if alt_month in months:
                month = months.index(alt_month) + 1
                day = int(alt_day)
                year = int(alt_year)
                if 1 <= day <= 31:
                     print(f"{year:04d}-{month:02d}-{day:02d}")
                     break
        except ValueError:
            pass
