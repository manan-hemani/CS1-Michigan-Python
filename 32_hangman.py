word = input("Please enter the phrase to guess: ").lower()
masked = ""
# masking the word as _____
for char in word:
    if char.isalpha():
        masked += "_"
    else:
        masked += char
chance = 6
missed_letter = None
missed_letter_temp = ""
print(f"Chances Remaining: {chance}")
print(f"Missed Letter: {missed_letter}\n")
print(masked)
# loop with chance and guessed condition
while chance != 0 and masked != word:
    guess = input("Your guess (letters only): ").lower()
    missed_letter = None
    if guess.isalpha() and len(guess) == 1:  # checking length and alphabet
        if guess in word:
            updated = ""
            # using loop to find the guessed word and fill the masked part
            for i in range(len(word)):
                if word[i] == guess:
                    updated += guess
                else:
                    updated += masked[i]
            masked = updated
        else:
            if guess not in word:
                missed_letter_temp += guess  # storing the guessed char in this variable
                missed_letter = guess
                chance -= 1
            else:
                print("You have already tried this letter or digit. Guess again!")
        print(f"Chances Remaining: {chance}")
        if missed_letter != None:
            print(f"Missed Letter: {missed_letter_temp}\n")
        else:
            print(f"Missed Letter: {missed_letter}\n")
        print(masked)
    else:
        print("Not a valid character. Please enter a letter")
