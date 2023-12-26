from telegram import Bot

def send_to_telegram_bot(data):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    chat_id = "YOUR_TELEGRAM_CHAT_ID"  # Replace with the actual chat ID

    # Prepare a message with quiz responses
    message = create_message(data)

    # Send the message to the Telegram bot
    bot.send_message(chat_id=chat_id, text=message)

def create_message(data):
    # Customize this function to format the quiz responses into a message
    message = "Quiz Responses:\n"
    for key, value in data.items():
        message += f"{key}: {value}\n"
    return message