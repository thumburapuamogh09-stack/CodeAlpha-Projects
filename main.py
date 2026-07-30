import random

WORDS = ["apple", "python", "tiger", "planet", "school"]
MAX_ATTEMPTS = 6


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    print("=" * 40)
    print("        HANGMAN GAME")
    print("=" * 40)

    secret_word = random.choice(WORDS)
    guessed_letters = set()
    attempts = MAX_ATTEMPTS

    while attempts > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print(f"Attempts Left: {attempts}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("Letter already guessed.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect!")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed '{secret_word}'.")
            return

    print(f"\nGame Over! The word was '{secret_word}'.")


if __name__ == "__main__":
    play_game()