import os
import telebot
token = "890911244:AAHbrUqqIwLrD8YYr3b_CFfqA_Qse5WHtKc"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")



bot.polling()
