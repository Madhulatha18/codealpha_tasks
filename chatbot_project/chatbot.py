import time
import random
import os
import sys

# Enable ANSI escape sequences on Windows
if os.name == 'nt':
    os.system("")

# Define color codes for attractive console output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Dictionary containing possible responses
RESPONSES = {
    "hello": ["hi"],
    "hi": ["Hello!", "Hey there!", "Hi! Nice to meet you."],
    "how are you": ["i am fine, thank you"],
    "what is your name": ["I am PyBot, your friendly neighborhood chatbot.", "You can call me PyBot."],
    "help": ["Here are some things you can say:\n- hello\n- hi\n- how are you\n- what is your name\n- help\n- bye"],
    "bye": ["good bye!"],
}

# Fallback responses for unknown inputs
UNKNOWN_RESPONSES = [
    "I'm not sure I understand that.",
    "Could you rephrase that?",
    "I'm still learning! Try saying 'help' to see what I can do.",
    "Interesting, tell me more."
]

def type_text(text, delay=0.03, color=Colors.ENDC):
    """Prints text with a typing effect."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.ENDC + '\n')

def print_banner():
    """Displays a welcome banner."""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}====================================================
           WELCOME TO PYBOT CONSOLE CHAT            
===================================================={Colors.ENDC}
"""
    print(banner)
    type_text("Initializing systems...", 0.05, Colors.BLUE)
    type_text("Ready! Type 'help' to see what I can do or 'bye' to exit.", 0.03, Colors.GREEN)
    print()

def get_bot_response(user_input):
    """Returns a response based on the user's input."""
    normalized_input = user_input.lower().strip()
    
    # Replace common punctuation with spaces to handle cases like "hello,how"
    for char in [",", ".", "?", "!", "-", "_", ";", ":", '"', "'"]:
        normalized_input = normalized_input.replace(char, " ")
        
    # Fix some common missing space typos like "areyou"
    normalized_input = normalized_input.replace("areyou", "are you")
    normalized_input = normalized_input.replace("howare", "how are")
    
    # Normalize spaces (removes multiple spaces)
    normalized_input = " ".join(normalized_input.split())
    
    # Check for the specific combined phrase
    if ("hello" in normalized_input or "hi" in normalized_input) and "how are you" in normalized_input and "bye" in normalized_input:
        return "hi i am fine, thank you, good bye!"
    
    # Keyword matching instead of exact match
    for keyword in sorted(RESPONSES.keys(), key=len, reverse=True):
        if keyword in normalized_input:
            return random.choice(RESPONSES[keyword])
    
    # Return a random fallback response if no match is found
    return random.choice(UNKNOWN_RESPONSES)

def save_chat_history(history):
    """Saves the chat history to a text file."""
    try:
        with open("chat_history.txt", "w", encoding="utf-8") as file:
            file.write("=== PyBot Chat History ===\n\n")
            for line in history:
                file.write(line + "\n")
        type_text("\n[System] Chat history successfully saved to 'chat_history.txt'", color=Colors.GREEN)
    except Exception as e:
        print(f"{Colors.FAIL}[Error] Could not save chat history: {e}{Colors.ENDC}")

def main():
    """Main function to run the chatbot."""
    print_banner()
    
    chat_history = []
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input(f"{Colors.BOLD}{Colors.WARNING}You:{Colors.ENDC} ").strip()
            
            # Error handling for empty input
            if not user_input:
                type_text("PyBot: Please say something! Don't be shy.", color=Colors.CYAN)
                continue
                
            # Add user message to history
            chat_history.append(f"You: {user_input}")
            
            # Check for exit command (exact match early exit)
            if user_input.lower() == 'bye':
                response = random.choice(RESPONSES["bye"])
                type_text(f"PyBot: {response}", color=Colors.CYAN)
                chat_history.append(f"PyBot: {response}")
                break
                
            # Generate and print bot response
            response = get_bot_response(user_input)
            
            # Simulate thinking delay
            time.sleep(0.5) 
            
            type_text(f"PyBot: {response}", color=Colors.CYAN)
            chat_history.append(f"PyBot: {response}")
            
            # Check for exit command anywhere in the input
            if 'bye' in user_input.lower():
                break
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print(f"\n{Colors.FAIL}Chat interrupted by user.{Colors.ENDC}")
            break
            
    # Option to save history
    if chat_history:
        print()
        save_prompt = input(f"{Colors.BLUE}Do you want to save the chat history? (yes/no): {Colors.ENDC}").strip().lower()
        if save_prompt in ['yes', 'y']:
            save_chat_history(chat_history)
            
    print(f"{Colors.CYAN}Thanks for chatting. See you next time!{Colors.ENDC}")

if __name__ == "__main__":
    main()
