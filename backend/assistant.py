import datetime


def get_response(message: str) -> str:
    message = message.lower().strip()

    if "what is your name" in message:
        return "My name is Virtual Assistant."

    elif "hello" in message or "hi" in message or "hey" in message:
        return "Hey! How can I help you?"

    elif "how are you" in message:
        return "I'm doing great! How can I help you?"

    elif "thank" in message:
        return "You're welcome!"

    elif "good morning" in message:
        return "Good morning! How can I help you today?"

    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "quit" in message or "shutdown" in message:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that yet."