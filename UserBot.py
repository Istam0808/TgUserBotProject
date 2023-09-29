from pyrogram import Client , filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
from time import sleep
import random


app = Client("my_account")
api_id = #your api id
api_hash = #"your api hash"


# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "◘"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом вашего телефона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Ваш телефон успешно взломан!")
    sleep(e.x)
    
    # sleep(3)
    # msg.edit("👽 Поиск секретных данных о вас ...")
    # perc = 0
 
    # while(perc < 100):
    #     try:
    #         text = "👽 Поиск секретных данных о вас ..." + str(perc) + "%"
    #         msg.edit(text)
 
    #         perc += random.randint(1, 5)
    #         sleep(0.15)
 
    #     except FloodWait as e:
    #         sleep(e.x)
 
    # msg.edit("🦖 Найдены данные о существовании вас на земле!")

@app.on_message(filters.command("hack1", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while(perc < 100):
        try:
            text = "Hacking in progress... " + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("Hacking complete!")
    sleep(1)

    msg.edit("Accessing confidential files...")
    sleep(2)

    msg.edit("Extracting sensitive information...")
    sleep(2)

    msg.edit("Override security protocols...")
    sleep(2)

    msg.edit("Stealing bank account details...")
    sleep(2)

    msg.edit("Access granted!")
    sleep(1)

    msg.edit("Mission successful! Target hacked.")
    sleep(1)

    msg.edit("Deleting all traces...")
    sleep(2)

    msg.edit("Hack complete!")
    sleep(1)
    sleep(e.x)


app.run()

#RUS:
#Если у вас не сработает код удалите этот код ↑
#и напишите этот код ↓
#Потом у вас выйдет в терминале регистрация
#Можете посмотреть на фотке Registracia

#ENG:
#If the code does not work for you, remove this code ↑
#and write this code↓
#Then you will see login in the terminal
#You can look at the photo Registracia

#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

# from pyrogram import Client
# api_id = 21114418
# api_hash = "8c00e7776168a841528f9c1e8bbbe9a7"
# app = Client("my_account", api_id=api_id, api_hash=api_hash)
# app.run()
