import telebot

TOKEN = "1679409193:AAF3ZodyYaSrW0wCivvMfsvME5yzEnIjavw"

bot = telebot.TeleBot(TOKEN)


user = bot.get_me()
print(user)

updates = bot.get_updates()
print(updates)
