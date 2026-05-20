import random
import os

# ASCII art for Hangman stages
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

# Dictionary grouping words by difficulty
WORDS = {
    "1": ["cat", "dog", "sun", "bat", "pen", "cup", "hat", "car", "map"],  # Easy
    "2": ["apple", "grape", "orange", "bottle", "planet", "guitar", "laptop"], # Medium
    "3": ["elephant", "adventure", "technology", "universe", "mountain", "mystery", "xylophone"] # Hard
}

def clear_screen():
    """Clears the console screen for better user experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Displays the welcome screen and instructions."""
    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME       ")
    print("=" * 40)
    print("Try to guess the word before the man is hung!")
    print("You have a total of 6 incorrect guesses.")
    print()

def get_difficulty():
    """Prompts the user to select a difficulty level."""
    while True:
        print("Select Difficulty Level:")
        print("1. Easy (3-4 letters)")
        print("2. Medium (5-7 letters)")
        print("3. Hard (8+ letters)")
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.\n")

def display_game_state(word, guessed_letters, attempts_left):
    """Displays the current state of the game: hangman, word, and guessed letters."""
    print(HANGMAN_PICS[6 - attempts_left])
    print(f"\nAttempts Left: {attempts_left}")
    
    # Display the word with hidden letters
    word_display = ""
    for letter in word:
        if letter in guessed_letters:
            word_display += letter + " "
        else:
            word_display += "_ "
    print(f"\nWord: {word_display.strip()}")
    
    # Display guessed letters in alphabetical order
    guessed_str = ", ".join(sorted(guessed_letters)) if guessed_letters else "None"
    print(f"Guessed Letters: {guessed_str}\n")

def get_player_guess(guessed_letters):
    """Prompts the player for a guess and validates the input."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a valid alphabetic letter.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        else:
            return guess

def play_game(score):
    """Main game loop for a single round of Hangman."""
    clear_screen()
    display_welcome()
    
    difficulty = get_difficulty()
    word_list = WORDS[difficulty]
    secret_word = random.choice(word_list).lower()
    
    guessed_letters = set()
    attempts_left = 6
    
    clear_screen()
    
    while attempts_left > 0:
        display_game_state(secret_word, guessed_letters, attempts_left)
        
        # Check if player has won
        if all(letter in guessed_letters for letter in secret_word):
            print("=" * 40)
            print(f"🎉 CONGRATULATIONS! You won! 🎉")
            print(f"The word was: {secret_word}")
            print("=" * 40)
            
            # Bonus score logic
            points_earned = 10 + (attempts_left * 2) 
            score += points_earned
            print(f"You earned {points_earned} points this round!")
            return score
            
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)
        
        clear_screen()
        
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            print(f"Oops! '{guess}' is not in the word.\n")
            attempts_left -= 1
            
    # Game over logic
    display_game_state(secret_word, guessed_letters, attempts_left)
    print("=" * 40)
    print("💀 GAME OVER! The man has been hung. 💀")
    print(f"The word was: {secret_word}")
    print("=" * 40)
    
    return score

def main():
    """Entry point of the application, handles the game session and replays."""
    score = 0
    while True:
        score = play_game(score)
        print(f"\nTotal Score: {score}\n")
        
        # Ask to replay
        while True:
            replay = input("Do you want to play again? (y/n): ").strip().lower()
            if replay in ['y', 'n']:
                break
            print("Please enter 'y' for yes or 'n' for no.")
            
        if replay != 'y':
            print("\nThank you for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    main()
