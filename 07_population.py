year=input("How many Years: ")
year_int=int(year)
years_to_seconds=365*24*3600
current_population=307357870
birth_count=int(years_to_seconds/7)
death_count=int(years_to_seconds/13)
immigrant_count=int(years_to_seconds/35)
total_changes=year_int*(birth_count-death_count+immigrant_count)
total=year_int*total_changes+current_population
print(f"New population in {year} years will change by {total_changes} to be {total}")