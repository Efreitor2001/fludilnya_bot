import asyncio
import datetime
from datetime import *
from create_bot import bot
from aiogram import types, Dispatcher


# @dp.message_handler(commands=['бан', 'ban'], commands_prefix='!')
async def ban(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    try:
        muteint = int(message.text.split()[1])
        mutetype = message.text.split()[2]
        comment = " ".join(message.text.split()[3:])
    except IndexError:
        await message.reply('Не хватает аргументов!\nПример:\n`!бан 1 ч причина`')
        return
    msg = await bot.send_poll(chat_id=message.chat.id,
                              question=f"Забанить {message.reply_to_message.from_user.first_name}?",
                              options=["Да", "Нет"])
    await asyncio.sleep(5)
    poll = await bot.stop_poll(chat_id=message.chat.id, message_id=msg.message_id)
    if int(poll['options'][0]["voter_count"]) > int(poll['options'][1]["voter_count"]) and \
            int(poll['options'][0]["voter_count"]) > 5:
        if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
            dt = datetime.now() + timedelta(hours=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(False), until_date=timestamp)
            await message.reply(
                f'| <b>Решение было принято:</b> {name1}\n| <b>Жертва:</b> <a href="tg://user?id='
                f'{message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n'
                f'| <b>Срок наказания:</b> {muteint} {mutetype} ⏰\n| <b>Причина:</b> {comment}',
                parse_mode='html')
        elif mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
            dt = datetime.now() + timedelta(minutes=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(False), until_date=timestamp)
            await message.reply(
                f'| <b>Решение было принято:</b> {name1}\n| <b>Жертва:</b> <a href="tg://user?id='
                f'{message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>'
                f'\n| <b>Срок наказания:</b> {muteint} {mutetype} ⏰\n| <b>Причина:</b> {comment}',
                parse_mode='html')
        elif mutetype == "д" or mutetype == "дней" or mutetype == "день":
            dt = datetime.now() + timedelta(days=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(False), until_date=timestamp)
            await message.reply(
                f'| <b>Решение было принято:</b> {name1}\n| <b>Жертва:</b> <a href="tg://user?id='
                f'{message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n'
                f'⏰| <b>Срок наказания:</b> {muteint} {mutetype}\n| <b>Причина:</b> {comment}',
                parse_mode='html')
    else:
        await bot.send_message(message.chat.id, f'<a href="tg://user?id='
                                                f'{message.reply_to_message.from_user.id}">'
                                                f'{message.reply_to_message.from_user.first_name}</a>, '
                                                f'<b>живи... Пока что...</b>', parse_mode='html')


# @dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!', is_chat_admin=True)
async def unban(message: types.Message):
    await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await bot.send_message(message.chat.id, 'Done')


def register_handlers_bot_commands(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['бан', 'ban'], commands_prefix='!')
    dp.register_message_handler(unban, commands=['разбан', 'unban'], commands_prefix='!', is_chat_admin=True)