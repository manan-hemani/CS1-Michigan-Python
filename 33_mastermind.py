print("The key should be numbers only with non-repeating digits\n")
key = input("What is the key: ")
guess = ""
history = ""
turn = 0
while guess != key:
    exist = 0
    position = 0
    guess = input("Guess: ")
    if len(guess) == 4 and guess.isdigit():
        # Count 'position' 
        for i in range(4):
            if guess[i] == key[i]:
                position += 1
        # Count 'exist' 
        for digit in "0123456789":
            if digit in key and digit in guess:
                exist += 1
        result = f"{guess}: exist:{exist}, position:{position}"  # Save results
        history += result + "\n"
        print(history)  # Prints all attempts
        turn += 1
    else:
        if not guess.isdigit():
            print("****contains non-numbers, try again")
        else:
            print("****guess must have length of 4, try again")
print(f"\nYou guessed the key: {key}")
print(f"It took you {turn} guesses")
