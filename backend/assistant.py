from datetime import datetime
from zoneinfo import ZoneInfo


def get_response(message: str) -> str:
    message = message.lower().strip()

    # Name
    if "what is your name" in message or "your name" in message:
        return "My name is Virtual Assistant."

    # Greetings
    elif (
        "hello" in message
        or "hi" in message
        or "hey" in message
        or "hii" in message
    ):
        return "Hey! How can I help you?"

    # How are you
    elif "how are you" in message:
        return "I'm doing great! How can I help you?"

    # Thanks
    elif "thank" in message:
        return "You're welcome!"

    # Good morning
    elif "good morning" in message:
        return "Good morning! How can I help you today?"

    # Current time
    elif "time" in message:
        current_time = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # Goodbye
    elif "quit" in message or "shutdown" in message or "goodbye" in message:
        return "Goodbye! Have a great day."

    # Unknown command
    else:
        return "Sorry, I don't understand that yet."