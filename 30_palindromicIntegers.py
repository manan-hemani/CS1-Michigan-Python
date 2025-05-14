start = int(input("Give me the first integer: "))
end = int(input("Give me th second integer: "))
palindrome = 0
non_lychrel = 0
lycherl = 0
for num in range(start, end + 1):
    s = str(num)
    if s == s[::-1]:
        palindrome += 1
        continue
    # 196 Algorithm
    iteration = 0
    temp = num
    found_palindrome = False
    while iteration < 60:
        reversed_temp = int(str(temp)[::-1])
        temp = temp + reversed_temp
        iteration += 1
        if str(temp) == str(temp)[::-1]:
            non_lychrel += 1
            found_palindrome = True
            break
    if not found_palindrome:
        lycherl += 1
        print(f"{num} looks like a lychrel number")
print()
print("*" * 20)
print(f"In the range {start} to {end}")
print(f"Palindrome Number Count: {palindrome}")
print(f"Non-Lychrel Number Count: {non_lychrel}")
print(f"Lychrel Counts: {lycherl}")
