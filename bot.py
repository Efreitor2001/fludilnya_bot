from aiogram.utils import executor
from create_bot import dp, bot
from handlers import bot_handlers, bot_commands
import asyncio
import aioschedule


async def rules():
    await bot.send_message(-1001520980874, 'test')


async def doit():
    aioschedule.every().day.at("01:41").do(rules)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def create(dp):
    asyncio.create_task(doit())


bot_commands.register_handlers_bot_commands(dp)
bot_handlers.register_handlers_bot_handlers(dp)

print('run')
executor.start_polling(dp, on_startup=create)
