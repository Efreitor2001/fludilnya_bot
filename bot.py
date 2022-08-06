from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

bot = Bot('5490678266:AAGHhzuse7TRRojzitQir_qZVp-t3u4VWok')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['new_chat_members'])
async def del_new(message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=['text'])
async def delete_messages(message: types.Message):
    check = 0
    is_admin = await bot.get_chat_administrators(message.chat.id)
    wl = ['https://t.me/c/', 'github.com']  # withe list
    for i in range(len(is_admin)):
        if int(message.from_user.id) == int(is_admin[i]['user']['id']):
            check = 1
    for i in wl:
        if i in message.text:
            check = 1
    if check == 0:
        for entity in message.entities:
            if entity.type in ["url", "text_link"]:
                await message.delete()


print('run')
executor.start_polling(dp)
