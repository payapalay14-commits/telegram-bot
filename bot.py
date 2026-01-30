import telebot

API_TOKEN = '8503670881:AAGrEu8HNQKx3L4UOV0mf7b07jy5hm1GyBk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    print("Received /start")
    bot.reply_to(message, 'မင်္ဂလာပါ https://t.me/jackgyi111')

print("Bot is running...")
bot.infinity_polling()
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'မင်္ဂလာပါ https://t.me/jackgyi111')

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'အကူအညီ https://t.me/jackgyi111')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
