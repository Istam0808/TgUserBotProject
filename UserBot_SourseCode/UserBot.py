from pyrogram import Client , filters
from pyrogram.errors import FloodWait
from time import sleep
import random

app = Client("my_account")
api_id = "tour_api_id"
api_hash = "your ip hash"

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
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

app.run()

