import telebot
from telebot import types
import os
from get_pokemon import get_pokemon
from pokemon_list import poke_list
from bs4 import BeautifulSoup
import requests

from flask import Flask, request

bot = telebot.TeleBot('2058514815:AAEPeocLS5CF1LzUoeiCjxxEI7JDhSYzd5k')
server = Flask(__name__)

pokemon = 'pikachu'
sticker = 'CAACAgEAAxkBAAEDHAlhbckn72lTlBfsd49itypAuFNDdgACOgEAAhQjcEeWhnjKXhqA9iEE'
info = get_pokemon(pokemon, 0).get_link()


@bot.message_handler(commands=['start'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Pikachu')
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEDHS1hbt1NelOTfhs9rc5Y_6T64LZBYAACOAsAAnbsIFCZN7LBNGOMkCEE')
    msg = bot.send_message(message.chat.id,
                           text='To use this bot, please digit a Pokemon Unite character as the example bellow.\n\n Try to spell it correctly.',
                           reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def step1(message):
    global pokemon, sticker
    try:
        if message.text.lower() in "".join(poke_list):
            if str(message.text).lower() in "pikachu":
                pokemon = "pikachu"
                sticker = 'CAACAgEAAxkBAAEDHAlhbckn72lTlBfsd49itypAuFNDdgACOgEAAhQjcEeWhnjKXhqA9iEE'
            if str(message.text.lower()) in "venusaur":
                pokemon = "venusaur"
                sticker = 'CAACAgEAAxkBAAEDHPhhbtggTrBcAAG_jmyB9ilZRU_I3XgAAvoBAAJWfXlHNNf6uJXl_-UhBA'
            if str(message.text.lower()) in "charizard":
                pokemon = "charizard"
                sticker = 'CAACAgEAAxkBAAEDHPphbtg1LI7nULndW0ioFQlLMAex-AAC3QEAAsymeEc_JRqkP3GE1yEE'
            if str(message.text.lower()) in "blastoise":
                pokemon = "blastoise"
                sticker = 'CAACAgEAAxkBAAEDHP5hbthTH_iGqGRB3nPIWIuPn7QusgAC_QEAAsTjeUf5y6qbPdLO6CEE'
            if str(message.text.lower()) in "alolan-ninetales":
                pokemon = "alolan-ninetales"
                sticker = 'CAACAgEAAxkBAAEDHQABYW7YXv7LiAkilyYoEseuTdZiXQgAAmsBAALQJnhHhqm_siJjKR8hBA'
            if str(message.text.lower()) in "wigglytuff":
                pokemon = "greninja"
                sticker = 'CAACAgEAAxkBAAEDHQRhbtkGwqlidWI5tWI8PAABnZpqFwcAAnQBAAJJlHhHjP42QnoO6RkhBA'
            if str(message.text.lower()) in "machamp":
                pokemon = "wigglytuff"
                sticker = 'CAACAgEAAxkBAAEDHQZhbtkTChg2FZbRxwE6kq4Xw0ohugACJAEAAjXeeUc88yybbrUaMiEE'
            if str(message.text.lower()) in "slowbro":
                pokemon = "slowbro"
                sticker = 'CAACAgEAAxkBAAEDHQhhbtkenXl7wXS5nst8LKGnqgfc9gACsQEAAsvveEfsgSh0RLs5eiEE'
            if str(message.text.lower()) in "gengar":
                pokemon = "gengar"
                sticker = 'CAACAgEAAxkBAAEDHQphbtkz0PqezqidQiHpPpOSvIvBzAACIwEAAg-geEcimAafTNmglSEE'
            if str(message.text.lower()) in "mr. mime":
                pokemon = "mr-mime"
                sticker = 'CAACAgEAAxkBAAEDHQJhbtjdMkx19R1fWPWZ28HSNT6PxQACegEAAq_jeEfVTKtaIU5X1SEE'
            if str(message.text.lower()) in "snorlax":
                pokemon = "snorlax"
                sticker = 'CAACAgEAAxkBAAEDHQxhbtlB3kkXy1B3lSeKLZLpqb4UIQACiwEAAlT_cUfKUv_LPMgIfSEE'
            if str(message.text.lower()) in "blissey":
                pokemon = "blissey"
                sticker = 'CAACAgEAAxkBAAEDHRBhbtlOb2xqPVTBzksqiFpiKwxtVwACdAIAAvEqcEcxRETlLue6xSEE'
            if str(message.text.lower()) in "gardevoir":
                pokemon = "gardevoir"
                sticker = 'CAACAgEAAxkBAAEDHRJhbtllxYketrhn3QABBigE2uCIEPIAAlABAALJDnhHKadrFpGAA1EhBA'
            if str(message.text.lower()) in "garchomp":
                pokemon = "garchomp"
                sticker = 'CAACAgEAAxkBAAEDHRRhbtlzA-ob5espsGDvonUt4uWARAACbwEAAmazeEdn4jdE7p3mVSEE'
            if str(message.text.lower()) in "lucario":
                pokemon = "lucario"
                sticker = 'CAACAgEAAxkBAAEDHRZhbtmNWkkrTKHRqurSA8_CNPQFCAACbAEAAmS5eEeQ0pJl3-Ia7iEE'
            if str(message.text.lower()) in "mamoswine":
                pokemon = "mamoswine"
                sticker = 'CAACAgEAAxkBAAEDHRhhbtmmMe8VwZAbkXtfzriEgnR1OwACWgIAAhl3eEdmBg9Xdf88VyEE'
            if str(message.text.lower()) in "absol":
                pokemon = "absol"
                sticker = 'CAACAgEAAxkBAAEDHRphbtmx0u7REvqDb3cf55pcwhH-KAACfQEAAtBBeEfVpCaz74dOCCEE'
            if str(message.text.lower()) in "crustle":
                pokemon = "crustle"
                sticker = 'CAACAgEAAxkBAAEDHRxhbtnCLTwB-4V5ZWT1q7XucR1p3QAChAEAAr-deUfG_SUrubb-ySEE'
            if str(message.text.lower()) in "greninja":
                pokemon = "greninja"
                sticker = 'CAACAgEAAxkBAAEDHR5hbtnSKSykveykn2CJaYo1EVuhSgACdAEAAkmUeEeM_jZCeg7pGSEE'
            if str(message.text.lower()) in "talonflame":
                pokemon = "talonflame"
                sticker = 'CAACAgEAAxkBAAEDHQ5hbtlMc1dmDQLhVbxs4KakowRdBAACqgEAAuZbeUe3-ksJ3seIuyEE'
            if str(message.text.lower()) in "sylveon":
                pokemon = "sylveon"
                sticker = 'CAACAgEAAxkBAAEDHSBhbtnlcfdErjrpwYk84-ioC2-hfgACdAEAAmSieUfXds2a1y5o8SEE'
            if str(message.text.lower()) in "zeraora":
                pokemon = "zeraora"
                sticker = 'CAACAgEAAxkBAAEDHSJhbtoRbHPLlMs9dnIt56oRM6_nYAACrgEAApfMeUdjUaZrX94ZOCEE'
            if str(message.text.lower()) in "cinderace":
                pokemon = "venusaur"
                sticker = 'CAACAgEAAxkBAAEDHSRhbtobIrvb-lV915BwEjW18dznPwAC-gEAAlZ9eUc01_q4leX_5SEE'
            if str(message.text.lower()) in "eldegoss":
                pokemon = "eldegoss"
                sticker = 'CAACAgQAAxkBAAEDHS5hbt1PrdaqGoTqCGe91VAuheCHSwAC5QwAAlJ_IVCaqeyRc8oSYCEE'
            if str(message.text.lower()) in "cramorant":
                pokemon = "cramorant"
                sticker = 'CAACAgEAAxkBAAEDHTFhbt1iO-wgCiQBZkOkfCIH5CLXDAACXwMAAmQ0eEeFIIW8Fx3MGyEE'

            menu1 = telebot.types.InlineKeyboardMarkup()
            but_1 = telebot.types.InlineKeyboardButton(text=get_pokemon(pokemon, 0).get_name(), callback_data='build1')
            but_2 = telebot.types.InlineKeyboardButton(text=get_pokemon(pokemon, 1).get_name(), callback_data='build2')
            but_3 = telebot.types.InlineKeyboardButton(text=get_pokemon(pokemon, 2).get_name(), callback_data='build3')
            but_4 = telebot.types.InlineKeyboardButton(text=get_pokemon(pokemon, 3).get_name(), callback_data='build4')
            but_5 = telebot.types.InlineKeyboardButton(text=get_pokemon(pokemon, 4).get_name(), callback_data='build5')
            but_6 = telebot.types.InlineKeyboardButton(text=get_pokemon(pokemon, 5).get_name(), callback_data='build6')

            menu1.row(but_1)
            menu1.row(but_2)
            menu1.row(but_3)
            menu1.row(but_4)
            menu1.row(but_5)
            menu1.row(but_6)

            bot.send_sticker(message.chat.id, sticker)
            msg = bot.send_message(message.chat.id, text="Select your build:", reply_markup=menu1)

        else:
            bot.send_message(message.chat.id, text='Search did not bring any results. Please, try again')
    except:
        pass


@bot.callback_query_handler(func=lambda call: True)
def step3(call):
    global info

    menu2 = telebot.types.InlineKeyboardMarkup()
    but_1 = telebot.types.InlineKeyboardButton(text='Info', callback_data='info')

    menu2.row(but_1)

    if call.data == 'build1':
        msg = bot.send_message(call.message.chat.id, get_pokemon(pokemon, 0).get_result(), reply_markup=menu2)
        info = get_pokemon(pokemon, 0).get_link()

    if call.data == 'build2':
        msg = bot.send_message(call.message.chat.id, get_pokemon(pokemon, 1).get_result(), reply_markup=menu2)
        info = get_pokemon(pokemon, 1).get_link()

    if call.data == 'build3':
        msg = bot.send_message(call.message.chat.id, get_pokemon(pokemon, 2).get_result(), reply_markup=menu2)
        info = get_pokemon(pokemon, 2).get_link()

    if call.data == 'build4':
        msg = bot.send_message(call.message.chat.id, get_pokemon(pokemon, 3).get_result(), reply_markup=menu2)
        info = get_pokemon(pokemon, 3).get_link()

    if call.data == 'build5':
        msg = bot.send_message(call.message.chat.id, get_pokemon(pokemon, 4).get_result(), reply_markup=menu2)
        info = get_pokemon(pokemon, 4).get_link()

    if call.data == 'build6':
        msg = bot.send_message(call.message.chat.id, get_pokemon(pokemon, 5).get_result(), reply_markup=menu2)
        info = get_pokemon(pokemon, 5).get_link()

    if call.data == 'info':
        msg = bot.send_message(call.message.chat.id, info)

@server.route('/' + '2058514815:AAEPeocLS5CF1LzUoeiCjxxEI7JDhSYzd5k', methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://intense-sands-77024.herokuapp.com/' + '2058514815:AAEPeocLS5CF1LzUoeiCjxxEI7JDhSYzd5k')
    return "!", 200

print('bot ON')

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))











