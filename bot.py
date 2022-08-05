from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot('5439181005:AAGjlNaqXx5toLp7aDiSfBSl7OIbkI13KY0')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def delete_messages(message: types.Message):
    check = 0
    is_admin = await bot.get_chat_administrators(message.chat.id)
    wl = ['https://t.me/c/', 'https://github.com']
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
