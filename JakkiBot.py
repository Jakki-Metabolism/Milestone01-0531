import telebot
from telebot import types

TOKEN = '1865792707:AAFenT5wu6D5iMFvApvjXGiRMHQJ5ti7WSs'
bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True, interval=0, timeout=200)

user = bot.get_me()

@bot.message_handler(commands=['start'])
def send_welcome(msg):
	bot.reply_to(msg, """
Hi! Welcome to FitNote, your health manage helper!
What can I help you?
""")
	bot.send_chat_action(msg.message_id, 'upload_photo')

@bot.message_handler(content_types=['photo'])
def send_to_photo(message):
	bot.reply_to(message, "Do you want to record your input?")
bot.polling()


