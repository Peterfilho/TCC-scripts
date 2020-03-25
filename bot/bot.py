import os
import telebot
import re
import requests
import json
import datetime
import urllib
import time

token = "890911244:AAHbrUqqIwLrD8YYr3b_CFfqA_Qse5WHtKc"

bot = telebot.TeleBot(token)

admin = "332154421"

url='https://lh3.googleusercontent.com/VVgn8cTK-Z4bymtautdtalgmgo0dzl4EUlhGmtrB6qLK5VDKaCzQddMUvDSKI3LwgNr-R0KPYWOyRDOD83L1KRnCsT8vXhClKAo8DTLrm2F55vwJ_o12urplCRwo-y3T0g4rIsmshQvCamzOvhVP3BNYfokI8fKXFUvAXRHZiLHrft_KF50O2Zgg3EX-AqxtxeTWRjx8J9ab58PkQvDwXmjSKM14BnFGXw3bzkGDqGGkhnymZrKcj9UM97tJce_DgrO_2nJsYlgEKibaSXGRUADF2VFN3zI9R4ri7yJTQA7L8ZTUXrK-1HfphJ9LQgqF3j8s6DIkcEynNa1FwckG8AS9Re79q1n44jFCxsbZMB9a-BDnnRUc9AJZJJxGjqhryZeTvutsVny-ggqkd8j8lsZYk9btlPCJox496Bo6B8SCK9fYrku5-86_4AruTnwhowQm2kS3OfG-rcWhvl5g5C-sLiKmPPJ2lLMzQq-igQjR6G4lOJtFZhbZBhtSAbctadt6utXOOZA7OTjphF3A70CwVMEqsJxq1QGa2clVp5SHZ4DN_0wOdAk9LyiVbQcjHyyzaw434n8xATG8aBhuUkxVN0T9VuQe3DaX-l148dEfg1Ah11zjv4ErrVlwymgYYtXcyBpem-D5hHnGRI8JL7LxiVWa25LuvmWJZreDZN_s87DBmxMgDA8ksKRu=w956-h637-no'
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(url).read())
f.close()

@bot.message_handler(commands=['mapa'])
def send_photo(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = open('out.jpg', 'rb')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    img.close()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")

#register user
@bot.message_handler(func=lambda m: True)
def reply(session):
    search = session.text
    if re.findall("^[Cc]adastrar", session.text.lower()):
        if session.from_user.id != 332154421:
            bot.reply_to(session, "❌ 🙅‍♂️ Ei cara, calma ai em Esse tipo de comando"
            "Só ADM pode fazer, você não tem autorização para isso :/")
            return
        search = search.split(": ")
        valores = search[1].split(", ")

        print("Valores: {}".format(valores))

        name = valores[0]
        role = valores[3]
        department = valores[2]
        ra = valores[1]
        ra = int(ra)

        bot.reply_to(session,"✅ Usuário cadastrado com sucesso!\n"
        "Nome: {}\n R.A: {}\n Setor: {}\n Cargo: {}"
        .format(name, ra, department, role))

        url = 'http://192.168.0.20:5000/api/v1/resources/users'
        headers = {'Content-Type': 'application/json'}
        PARAMETERS = {'name':name,
    	    'department':department,
    	    'role':role,
    	    'ra': ra}

        #print(PARAMETERS)

        r = requests.post(url = url, headers=headers, data=json.dumps(PARAMETERS))

        #print(r)
        #print(json.dumps(PARAMETERS))
        data = r.json()
        print(data)
        #bot.reply_to(session, "✅ Usuário cadastrado com sucesso!\n{}".format(data))

    elif re.findall("^[Ll]ocalizar", session.text.lower()):

        search = search.split(" ")
        ra = search[1]
#        print(ra)
        r = requests.get("http://192.168.0.20:5000/api/v1/resources/positions?ra={}".format(ra))
        data = r.json()
        if r.content == b'[]\n':
            bot.reply_to(session, "🤷‍♂️ Não encontrei nada!\nVerifique se o RA que buscou é válido")
            return
        event = data[-1]

        formated_hour = datetime.datetime.strptime(event['date'], "%Y-%m-%d %H:%M").strftime("%H:%M")
        formated_date = datetime.datetime.strptime(event['date'], "%Y-%m-%d %H:%M").strftime("%d/%m/%Y")

        bot.reply_to(session,"🕵️‍♂️ Encontrei o seguinte:\n\n👤 Usuário: {}\n🔖 R.A: {}\n \n🏭 Setor: {}\n🗺 Ultimo local: {}\n🕰 Ultima atualização: {} {}"
        .format(event['name'],event['user_id'],event['department'], event['locale'], formated_date, formated_hour))

    elif re.findall("test", session.text.lower()):
        bot.reply_to(session, "lol")

bot.polling()
