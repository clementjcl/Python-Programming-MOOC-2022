from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date = datetime(year, month, day)
eve_new_millennium = datetime(2000, 1, 1)

old_eve = eve_new_millennium - date

if (old_eve.days - 1) >= 0:
    print(f"You were {old_eve.days - 1} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
