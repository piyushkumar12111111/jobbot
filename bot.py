# import os

# import telebot

# BOT_TOKEN = os.environ.get('BOT_TOKEN')

# print(BOT_TOKEN)

# bot = telebot.TeleBot(BOT_TOKEN)


# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# bot.infinity_polling()


import telebot
import os
from scraper.job_scraper import get_latest_job_titles

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
API_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


# create a menu button for sending show latest job
# create a menu button for sending show latest job




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Type 'show latest job' to get the latest job title.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if 'show latest job' in message.text.lower():
        job_title = get_latest_job_titles()
        bot.reply_to(message, f"The latest job is: {job_title}")
    else:
        bot.reply_to(message, "I can only show the latest job title. Type 'show latest job' to get the latest job title.")

if __name__ == '__main__':
    bot.polling()
