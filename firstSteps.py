from pyrogram import Client, filters

app = Client("my_account")

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")

app.run()



#ENG
# The given code is a simple example of a Pyrogram client that replies "Hello from Pyrogram!" to any incoming private message.
# Explanation:
# - The code imports the necessary modules (Client and filters) from the Pyrogram library.
# - It creates an instance of the Client class with the name "my_account".
# - It defines a decorator @app.on_message(filters.private) which tells the client to execute the following function whenever a private message is received.
# - Inside the function, it sends a reply message "Hello from Pyrogram!"
# - Finally, it runs the Pyrogram client by calling app.run(). This line of code starts the client and listens for incoming messages


#RUS
# Данный код представляет собой простой пример клиента Pyrogram, который отвечает "Hello from Pyrogram!" на любое входящее личное сообщение.
# Объяснение:
# - Код импортирует необходимые модули (Client и filters) из библиотеки Pyrogram.
# - Создается экземпляр класса Client с именем "my_account".
# - Определяется декоратор @app.on_message(filters.private), который говорит клиенту выполнить следующую функцию при получении личного сообщения.
# - Внутри функции отправляется ответное сообщение "Hello from Pyrogram!"
# - Наконец, клиент Pyrogram запускается вызовом app.run(). Эта строка кода запускает клиент и слушает входящие сообщения.

