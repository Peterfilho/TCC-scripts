import os
import telebot
import re
import requests
import json
import datetime

token = "890911244:AAHbrUqqIwLrD8YYr3b_CFfqA_Qse5WHtKc"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")

#register user
@bot.message_handler(func=lambda m: True)
def reply(session):
    search = session.text
    if re.findall("^[Cc]adastrar", session.text.lower()):
        search = search.split(":")
        valores = search[1].split(",")

        print("Valores: {}".format(valores))

        name = valores[0]
        role = valores[3]
        department = valores[2]
        ra = valores[1]
        #ra = int(ra)

        #bot.reply_to(session,"Nome: {}\n R.A: {}\n Setor: {}\n Cargo: {}"
        #.format(name, ra, department, role))

        url = 'http://127.0.0.1:5000/api/v1/resources/users'
        headers = {'Content-Type': 'application/json'}
        PARAMETERS = {'name':name,
    	    'department':department,
    	    'role':role,
    	    'ra': ra}

        print(PARAMETERS)

        r = requests.post(url = url, json=PARAMETERS)
        print(r)
        print("dumps")
        print(json.dumps(PARAMETERS))
        #data = r.json()
        #bot.reply_to(session, "{}".format(data))


    elif re.findall("^[Ll]ocalizar", session.text.lower()):

        search = search.split(" ")
        ra = search[1]

        r = requests.get("http://localhost:5000/api/v1/resources/positions?id={}".format(ra))
        data = r.json()

        if r.content == b'[]\n':
            bot.reply_to(session, "🤷‍♂️ Não encontrei nada!\nVerifique se o RA que buscou é válido")
            return
        event = data[-1]

        formated_hour = datetime.datetime.strptime(event['date'], "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S")
        formated_date = datetime.datetime.strptime(event['date'], "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")

        bot.reply_to(session,"🕵️‍♂️ Encontrei o seguinte:\n\n👤 Usuário: {}\n🔖 R.A: {}\n \n🏭 Setor: {}\n🗺 Ultimo local: {}\n🕰 Ultima atualização: {} {}"
        .format(event['name'],event['user_id'],event['department'], event['locale'], formated_date, formated_hour))

    elif re.findall("test", session.text.lower()):
        bot.reply_to(session, "lol")

bot.polling()
