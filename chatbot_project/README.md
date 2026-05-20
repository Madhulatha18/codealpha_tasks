# Python Console Chatbot

A beginner-friendly, rule-based console chatbot built with Python. This project demonstrates core programming concepts while providing a fun, interactive command-line interface.

## Features

- **Interactive Console Interface:** Features a welcoming banner and colored terminal text.
- **Typing Effect:** Simulates a human-like typing delay for a more engaging experience.
- **Rule-Based Responses:** Recognizes standard greetings and questions (`hello`, `hi`, `how are you`, `what is your name`, `help`, `bye`).
- **Randomized Replies:** Provides varied responses for the same input to make conversations feel more natural.
- **Error Handling:** Gracefully handles empty inputs and prompts the user to type something.
- **Chat History:** Keeps a record of the conversation during the session.
- **Export Option:** Allows the user to save the chat history to a `chat_history.txt` file upon exiting.

## Technologies Used

- Python 3.x
- Standard Libraries (`time`, `random`, `os`, `sys`)

## Concepts Used

- **Variables & Data Types:** Storing user inputs and chat history (strings, lists).
- **Dictionaries:** Mapping user inputs to potential bot responses.
- **Functions:** Modularizing code into logical blocks (`type_text`, `print_banner`, `get_bot_response`, `save_chat_history`, `main`).
- **Loops:** Using `while` loops to maintain the chat session and `for` loops for iterating over characters (typing effect).
- **Conditionals:** Using `if-elif-else` structures for matching user input and handling exit logic.
- **File I/O:** Writing the chat session history to a text file.
- **Error Handling:** `try-except` blocks to handle file saving errors or keyboard interruptions.

## How to Run the Project

1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the `chatbot_project` directory.
4. Run the script using the following command:
   ```bash
   python chatbot.py
   ```
5. Start chatting! Try typing `help` to see available commands, and `bye` when you're ready to exit.

## Project Structure

```text
chatbot_project/
│
├── chatbot.py           # The main chatbot Python script
├── chat_history.txt     # Generated automatically when saving a chat
└── README.md            # Project documentation (this file)
```
