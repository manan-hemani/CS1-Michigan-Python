while True:
    file_name = input("Enter the name of the input file: ")
    try:
        file = open(file_name, "r")
        break
    except FileNotFoundError:
        print("File not found. Try again.")
year_input = input("Enter the year: ").strip()
print("Income levels:")
print("1: Low income")
print("2: Lower middle income")
print("3: Upper middle income")
print("4: High income")
income_code = ""
while True:
    choice = input("Enter income level (1-4): ").strip()
    if choice == "1":
        income_code = "WB_LI"
        break
    elif choice == "2":
        income_code = "WB_LMI"
        break
    elif choice == "3":
        income_code = "WB_UMI"
        break
    elif choice == "4":
        income_code = "WB_HI"
        break
    else:
        print("Invalid choice. Try again.")
count = 0
total_percent = 0
min_percent = 101
max_percent = -1
min_country = ""
max_country = ""
for line in file:
    #based on txt file provide counted length and sliced it accordingly
    country = line[0:50].strip()
    income = line[50:59].strip()
    percent_str = line[60:62].strip()
    year = line[88:92].strip()
    print(country, "---", income, "---", percent_str, "---", year)
    if year == year_input and income == income_code:
        try:
            percent = int(percent_str)
        except:
            continue
        total_percent += percent
        count += 1
        if percent < min_percent:
            min_percent = percent
            min_country = country
        if percent > max_percent:
            max_percent = percent
            max_country = country
file.close()
if count == 0:
    print("No matching records found.")
else:
    average = total_percent / count
    print(f"\nRecords found: {count}")
    print(f"Average vaccinated percent: {average:.1f}%")
    print(f"Lowest: {min_percent}% ({min_country})")
    print(f"Highest: {max_percent}% ({max_country})")
