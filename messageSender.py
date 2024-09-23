import asyncio

import json
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart,Command


from flask import Flask,request


from messages import *
from privateData import botToken

data = {
    "name":"Захар Головіцький",
    "date":"17.09.2024",
    "start":"14:00",
    "end":"19:40",
    "approximatePrice":1350,
    "adres":"Осіння 39",
    "numberPhone": "096387827",
    "code":"1943",
    "customerName":"Софія Меднова"
}

app = Flask("__GreenLineForWorkerBot__")

dp = Dispatcher()

bot = Bot(token=botToken, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


# -> ApiBots actions
@dp.message(Command(commands=["nearestTask"]))
async def nearestTaskHandler(message: Message) -> None:
    try:
        await bot.send_message(message.chat.id,checkClosestTask(data))
    except TypeError:
        await message.answer("Щось пішло не так")



@app.route("/send_new_order",methods=["POST"])
async def sendNewOrderToCleanerMessage():
    data = request.json
    userName = "@" + data.get("username")
    message = "You're welcome!"

    if not userName or not message:
        pass

    try:
        await bot.send_message(NewOrderMessage(data))
        return json.dumps({
            "status":"200",
            "response":f"Message was sended to {userName}"
        })
    except Exception as e:
        return json.dumps({
            "status":"500"
        })



@dp.message(Command(commands=["changeAccount"]))
async def changeAccountMessage(data):
    codeToReset = 986482

    try:
        await bot.send_message(changeAccountMessage(codeToReset))

    except Exception as e:
        return json.dumps({
            "status":"500"
        })

# -> Raw bots actions
@dp.message(CommandStart())
async def startMessage(message:Message):
    try:
        await bot.send_message(message.chat.id,"Welcome")
    except Exception as e:
        pass



async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
    app.run(host="127.0.0.1",port=5000)
    

    