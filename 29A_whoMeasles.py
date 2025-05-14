try:
    infile = open("measles.txt", "r")
except FileNotFoundError:
    print("Error: Unable to open 'measles.txt'. Program will exit.")
outfile_name = input("Enter name of output file: ")
try:
    outfile = open(outfile_name, "w")
except Exception as e:
    print(f"Error opening output file: {e}")
    infile.close()
year_input = input("Enter a year (or prefix, or 'all'): ").strip()
count = 0
for line in infile:
    # based on txt file provide counted length and sliced it accordingly
    year = line[88:92].strip()
    if year.startswith(year_input) or year_input == "" or year_input.lower() == "all":
        outfile.write(line)
        count += 1
print(f"{count} line(s) copied to '{outfile_name}'.")
infile.close()
outfile.close()
