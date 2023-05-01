import asyncio
from aiogram import Bot, Dispatcher, types

from utils.file_handler import get_data, update_data

bot = Bot(token='6095252808:AAFWCaBAHhg2TemwBblFHJp-Tye7Sf6CImY')
dp = Dispatcher(bot)


async def send_signal(text: str):
    IDs = get_data("subs")["subs_list"]
    if len(IDs) != 0:
        for chat_id in IDs:
            await bot.send_message(chat_id=chat_id, text=text)
    else:
        print("No IDs")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Подпишитесь на уведомления командой /sub")


@dp.message_handler(commands=["sub"])
async def subscribe(message: types.Message):
    data_subs = get_data("subs")
    subs_list = list(data_subs["subs_list"])
    if message.chat.id not in subs_list:
        subs_list.append(message.chat.id)
        data_subs["subs_list"] = subs_list
        update_data("subs", data_subs)
        await bot.send_message(chat_id=message.chat.id, text="Подписка на уведомления оформлена!")
    else: await bot.send_message(chat_id=message.chat.id, text="Вы уже подписаны.")


dp.register_message_handler(send_signal)


async def main():
    await dp.start_polling()


def start_bot():
    asyncio.run(main())
