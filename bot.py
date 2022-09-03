from aiogram.utils import executor
from create_bot import dp, bot
from handlers import bot_handlers, bot_commands
import asyncio
import aioschedule


async def rules():
    await bot.send_message(-1001520980874, '📝 *#ПРАВИЛА ФЛУДИЛЬНИ*:\n'
                                           '\n🤳 *Фото экрана - бан на сутки. Только скриншоты.*\n'
                                           '\n *❓Правильно формулируйте свой вопрос:*\n'
                                           '\n- Какую задачу я решаю'
                                           ' \n- Объяснить, что именно я делаю'
                                           '\n- Какие данные я использую сейчас'
                                           '\n- Откуда эти данные'
                                           '\n- Какой результат я ожидаю'
                                           '\n- Что я получаю'
                                           '\n- Почему / Как исправить? / Что я делаю не так?\n'
                                           '\n*#️⃣ Желательно, чтобы Ваш вопрос не потерялся во флуде, '
                                           'оставляйте хештег #вопрос.*\n'
                                           '\n*🚫ЗАПРЕЩЕНЫ:*'
                                           '\n- реклама'
                                           '\n- оскорбления'
                                           '\n- мат'
                                           '\n- расизм, сексизм, темы 18+\n'
                                           '\n❗️Если кто-то по вашему мнению нарушает правила, '
                                           'отправляйте в ответ на сообщение `!бан причина бана`',
                           parse_mode='markdown')
    await bot.send_message(-1001520980874, '<b>Поддержать бота:</b>\n'
                                           'https://www.donationalerts.com/askme/ELC2001', parse_mode='html')


async def doit():
    aioschedule.every().day.at("19:16").do(rules)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def create(dp):
    asyncio.create_task(doit())


bot_commands.register_handlers_bot_commands(dp)
bot_handlers.register_handlers_bot_handlers(dp)

print('run')
executor.start_polling(dp, on_startup=create, skip_updates=True)
