import telebot

API_TOKEN = '8503670881:AAGrEu8HNQKx3L4UOV0mf7b07jy5hm1GyBk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    print("Received /start")
    bot.reply_to(message, 'မင်္ဂလာပါ 👋\nBot အလုပ်လုပ်နေပါပြီ')

print("Bot is running...")
bot.infinity_polling()

