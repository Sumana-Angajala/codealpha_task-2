# Task 2: Advanced Rule-Based Chatbot
import datetime
import random
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Some jokes for fun
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems.",
    "I told my computer I needed a break, and now it won’t stop sending me KitKats."
]

# Boxed message function
def box_message(speaker, message, color):
    line = f"{speaker}: {message}"
    border = "-" * (len(line) + 4)
    print(color + border)
    print(color + f"| {line} |")
    print(color + border)

def chatbot():
    name = None  # to remember user’s name
    
    # Greeting Banner
    print(Back.MAGENTA + Fore.WHITE + " " * 55)
    print(Back.MAGENTA + Fore.WHITE + "🤖  Welcome to Smart Chatbot  🤖".center(55))
    print(Back.MAGENTA + Fore.WHITE + " " * 55 + Style.RESET_ALL)
    print(Fore.YELLOW + "Type 'bye' anytime to exit.\n")

    while True:
        user_input = input(Fore.CYAN + "You: ").lower().strip()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            hour = datetime.datetime.now().hour
            if hour < 12:
                box_message("Chatbot", "Good morning! 🌅", Fore.GREEN)
            elif 12 <= hour < 18:
                box_message("Chatbot", "Good afternoon! ☀️", Fore.GREEN)
            else:
                box_message("Chatbot", "Good evening! 🌙", Fore.GREEN)

        # How are you
        elif user_input in ["how are you", "how are you doing"]:
            box_message("Chatbot", "I'm doing great, thanks! How about you?", Fore.GREEN)

        # Feeling good
        elif user_input in ["i am fine", "i'm fine", "good", "great"]:
            box_message("Chatbot", "Glad to hear that! 😃", Fore.GREEN)

        # Name memory
        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip().title()
            box_message("Chatbot", f"Nice to meet you, {name}! 🎉", Fore.GREEN)

        elif user_input in ["what is my name", "do you know my name"]:
            if name:
                box_message("Chatbot", f"Of course! Your name is {name} 😎", Fore.GREEN)
            else:
                box_message("Chatbot", "Oops, I don't know your name yet. Tell me by saying 'my name is ...'", Fore.RED)

        # Bot info
        elif user_input in ["what is your name", "who are you"]:
            box_message("Chatbot", "I'm a simple chatbot created to chat with you!", Fore.GREEN)

        # Time & Date
        elif user_input in ["what time is it", "time", "date"]:
            now = datetime.datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
            box_message("Chatbot", f"The current time is {now}", Fore.GREEN)

        # Jokes
        elif user_input in ["tell me a joke", "joke"]:
            joke = random.choice(jokes)
            box_message("Chatbot", joke, Fore.GREEN)

        # Thanks
        elif user_input in ["thank you", "thanks", "thx"]:
            box_message("Chatbot", "You're welcome! 🙏", Fore.GREEN)

        # Exit
        elif user_input in ["bye", "goodbye", "see you"]:
            box_message("Chatbot", "Goodbye! Have a wonderful day! 🌸", Fore.GREEN)
            break

        # Unknown
        else:
            box_message("Chatbot", "Sorry, I didn't get that. Can you try again?", Fore.RED)


# Run chatbot
chatbot()
