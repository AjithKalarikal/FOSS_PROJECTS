import telebot

bot = telebot.TeleBot('745852645:AAGAL3TkK_Tw3vadxeOIGTbmucTOWXHdKiE')

@bot.message_handler(commands=['hello', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['fine', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Same here")

@bot.message_handler(commands=['Who_are_you', 'help'])
def send_welcome(message):
	bot.reply_to(message, "I am a test bot,serving its purpose")

@bot.message_handler(commands=['cool', 'help'])
def send_welcome(message):
	bot.reply_to(message, ":)")

@bot.message_handler(commands=['Jokes', 'help'])
def send_welcome(message):
	bot.reply_to(message, "I am not good with jokes,but let me try")

@bot.message_handler(commands=['k', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Q: What did one toilet say to the other toilet? A: You look flushed.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
