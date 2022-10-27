from datetime import datetime, timedelta

file_name = input("Filename: ")
starting_date_str = input("Starting date: ")
starting_date = datetime.strptime(starting_date_str, "%d.%m.%Y")

days_long = int(input("How many days: ")) - 1
print("Please type in screen time in minutes on each day (TV computer mobile)")

last_day = starting_date + timedelta(days=days_long)

dic = {}
all_minutes = ""
for single_day in (starting_date + timedelta(n) for n in range(days_long + 1)):
    minutes_day = input(f"Screen time {single_day.day}.{single_day.month}.{single_day.year}: ")
    dic[f"{single_day.day}.{single_day.month}.{single_day.year}"] = minutes_day.split()


total_minutes = 0
for key, value in dic.items():
    total_minutes += int(value[0]) + int(value[1]) + int(value[2])

average_min = total_minutes / (days_long + 1)

print(dic)
with open(file_name, "w") as contents:
    contents.write(f"Time period: {datetime.strftime(starting_date, '%d.%m.%Y')}-{datetime.strftime(last_day, '%d.%m.%Y')}\n")
    contents.write(f"Total minutes: {total_minutes}\n")
    contents.write(f"Average minutes: {average_min}\n")
    for key, value in dic.items():
        format_key = datetime.strptime(key, "%d.%m.%Y")
        contents.write(f"{datetime.strftime(format_key, '%d.%m.%Y')}: {value[0]}/{value[1]}/{value[2]}\n")
print(f"Data stored in file {file_name}")

   
