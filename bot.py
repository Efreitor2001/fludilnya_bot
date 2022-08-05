from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot('5439181005:AAGjlNaqXx5toLp7aDiSfBSl7OIbkI13KY0')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def delete_messages(message: types.Message):
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            await message.delete()


print('run')
executor.start_polling(dp)
