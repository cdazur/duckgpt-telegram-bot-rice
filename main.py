# main.py
import telebot
from config import TOKEN
from handlers import setup_handlers

def main():
    bot = telebot.TeleBot(TOKEN)

    user_messages = {}
    user_message_ids = {}

    setup_handlers(bot, user_messages, user_message_ids)

    # Print a message to the console when the bot starts
    print("Bot is running...")

    # Запуск бота
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()