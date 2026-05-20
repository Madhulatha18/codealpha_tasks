# Console Hangman Game

A polished, text-based Hangman game implemented in Python as an internship project.

## Project Overview
This project is a classic Hangman game playable in the terminal/console. The player attempts to guess a hidden word letter by letter, with a limited number of incorrect guesses allowed. The game features different difficulty levels, input validation, and an interactive ASCII-art display, completely built utilizing built-in Python standard libraries.

## Features
- **Difficulty Levels**: Choose between Easy, Medium, and Hard, each with a tailored list of words to offer scalable challenge.
- **ASCII Art**: Visual representation of the hangman state that updates gracefully with each incorrect guess.
- **Input Validation**: Ensures the user enters valid, single alphabetical characters and prevents duplicate guesses to avoid frustrating mistakes.
- **Score Tracking**: Tracks the player's score across multiple rounds (including a bonus based on remaining attempts).
- **Replayability**: Option to seamlessly play again after a match concludes without restarting the script.
- **Dynamic Display**: Shows remaining attempts, guessed letters, and the current progress on the word interactively.

## Python Concepts Used
- **Standard Libraries**: Used `random` for unpredictable word selection and `os` for screen clearing functionality.
- **Data Structures**: Used Lists (for words and ASCII art), Sets (for optimal tracking of guessed letters), and Dictionaries (for organizing word difficulties).
- **Control Flow**: Implemented `while` and `for` loops, and structured `if-elif-else` conditionals for solid game logic.
- **Functions**: Code is modularized into dedicated well-commented functions (`display_welcome`, `get_player_guess`, `play_game`, `main`, etc.) for readability, isolation, and maintenance.
- **String Manipulation**: Extensive use of string methods (`.lower()`, `.strip()`, `.isalpha()`) and formatted strings (f-strings) for dynamic output creation.

## Instructions to Run

1. Ensure you have Python installed on your system (Python 3.x recommended).
2. Open your terminal or command prompt.
3. Navigate to the directory containing the project files (`hangman_project`).
4. Run the script using the following command:
   ```bash
   python hangman.py
   ```
5. Follow the on-screen prompts to select a difficulty, input your guesses, and enjoy!
