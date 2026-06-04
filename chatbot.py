def get_response(user_input):
    msg = user_input.lower().strip()
 
    # Greetings
    if any(word in msg for word in ["hello", "hi", "hey", "hiya", "howdy"]):
        return "Hey there! How can I help you today?"
 
    elif any(word in msg for word in ["how are you", "how r you", "how are u", "you doing", "you good"]):
        return "I'm doing great, thanks for asking! What about you?"
 
    elif any(word in msg for word in ["i'm good", "im good", "i am good", "doing well", "i'm fine", "im fine"]):
        return "That's awesome to hear! Is there anything I can help you with?"
 
    # Name
    elif any(word in msg for word in ["what's your name", "whats your name", "who are you", "your name"]):
        return "I'm ChatBot, your simple AI assistant. Nice to meet you!"
 
    # What can you do
    elif any(word in msg for word in ["what can you do", "help", "capabilities", "features"]):
        return ("I can chat with you, answer basic questions, tell you a joke, "
                "share the time, and keep you company. Try asking me something!")
 
    # Jokes
    elif any(word in msg for word in ["joke", "funny", "make me laugh", "tell me a joke"]):
        import random
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the developer go broke? Because he used up all his cache. 💸",
            "How many programmers does it take to change a light bulb? None — that's a hardware problem! 💡",
            "Why do Python programmers wear glasses? Because they can't C! 😄",
        ]
        return random.choice(jokes)
 
    # Time
    elif any(word in msg for word in ["time", "what time", "current time"]):
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
 
    # Date
    elif any(word in msg for word in ["date", "today", "what day", "what's today"]):
        from datetime import datetime
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."
 
    # Weather (simulated)
    elif any(word in msg for word in ["weather", "temperature", "forecast"]):
        return "I'm not connected to a weather service, but I hope it's sunny where you are! ☀️"
 
    # Age / creation
    elif any(word in msg for word in ["how old are you", "when were you created", "your age"]):
        return "I was created just recently as part of a Python project. So I'm pretty new! 😊"
 
    # Favorite things
    elif any(word in msg for word in ["favorite color", "favourite color"]):
        return "I'd say blue — it's calm and reliable, just like a good program!"
 
    elif any(word in msg for word in ["favorite food", "favourite food"]):
        return "Hmm, I'd probably go with pizza. Who doesn't love pizza? 🍕"
 
    # Thanks
    elif any(word in msg for word in ["thank you", "thanks", "thank u", "thx", "ty"]):
        return "You're welcome! Happy to help anytime. 😊"
 
    # Bye
    elif any(word in msg for word in ["bye", "goodbye", "see you", "see ya", "quit", "exit", "cya"]):
        return "Goodbye! It was nice chatting with you. Take care! 👋"
 
    # Compliments to bot
    elif any(word in msg for word in ["good bot", "nice bot", "you're great", "you are great", "awesome"]):
        return "Aww, thank you! You're pretty great yourself! 😄"
 
    # Insults (handle gracefully)
    elif any(word in msg for word in ["stupid", "dumb", "useless", "bad bot"]):
        return "I'm sorry to hear that! I'm still learning. Let me try to do better. 😅"
 
    # Fallback
    else:
        return ("Hmm, I'm not sure I understood that. Could you try rephrasing? "
                "You can ask me things like 'tell me a joke' or 'what time is it'.")
 
def main():
    print("=" * 50)
    print("       🤖  ChatBot  |  CodeAlpha Task 4")
    print("=" * 50)
    print("  Hi! I'm ChatBot. Type something to get started.")
    print("  (Type 'bye' or 'exit' to quit)\n")
 
    while True:
        try:
            user_input = input("  You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Bot: Goodbye! 👋")
            break
 
        if not user_input:
            print("  Bot: Please say something! I'm all ears. 👂\n")
            continue
 
        response = get_response(user_input)
        print(f"  Bot: {response}\n")
 
        # Exit if the bot said goodbye
        if any(word in user_input.lower() for word in ["bye", "goodbye", "see you", "see ya", "quit", "exit", "cya"]):
            break
if __name__ == "__main__":
    main()