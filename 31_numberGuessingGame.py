import random

# random secret_num number generator using sample()
unique_digits = "0123456789"
secret_num = "".join(
    random.sample(unique_digits, 5)
)  # gives output in list so used join()

print(
    "Welcome to the Secret Number Guessing Game.\nPlease read the following information."
)
max_guesses = 10
guess_count = 0
print(f"Player: You have {max_guesses} guesses to find the 5-digit secret number.")
print("Type 'quit' anytime to exit.\n")
while guess_count < max_guesses:
    guess = input(f"Guess #{guess_count + 1}: ").strip()

    if guess.lower() == "quit":
        print(
            f"You quit after {guess_count} guess(es). You lost. The secret number was {secret_num}."
        )
        break
    if not guess.isdigit() or len(guess) != 5:
        print("Invalid guess. It must be exactly 5 digits. Try again.")
        continue
    guess_count += 1
    correct_digits = 0
    for digit in set(guess):
        if digit in secret_num:
            correct_digits += 1
    correct_positions = 0
    for i in range(5):
        if guess[i] == secret_num[i]:
            correct_positions += 1
    print(
        f"Guess #{guess_count}: {guess} - Correct digits: {correct_digits} - Correct positions: {correct_positions}\n"
    )
    if guess == secret_num:
        print(f"Congratulations! You guessed the number in {guess_count} attempt(s).")
        break
else:
    print(
        f"You've used all {max_guesses} guesses. You lost. The secret_num number was {secret_num}."
    )
