import asyncio
import datetime
from datetime import *
from create_bot import bot
from aiogram import types, Dispatcher


# @dp.message_handler(commands=['бан', 'ban'], commands_prefix='!')
async def ban(message):
    check = 0
    is_admin = await bot.get_chat_administrators(message.chat.id)
    for i in range(len(is_admin)):
        if int(message.reply_to_message.from_user.id) == int(is_admin[i]['user']['id']):
            check = 1
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        del_mes = await message.reply("Эта команда должна быть ответом на сообщение!")
        await asyncio.sleep(5)
        await del_mes.delete()

        return
    try:
        comment = " ".join(message.text.split()[1:])
    except IndexError:
        await message.reply('Не хватает аргументов!\nПример:\n`!бан причина`')
        return
    if check == 1:
        del_mes = await message.reply('<b>Это выше моих полномочий, Десу</b>', parse_mode='html')
        await asyncio.sleep(5)
        await del_mes.delete()

    elif message.reply_to_message.from_user.id != message.from_user.id:
        msg = await bot.send_poll(chat_id=message.chat.id,
                                  question=f"Забанить {message.reply_to_message.from_user.first_name}?",
                                  options=["Да", "Нет"])
        await asyncio.sleep(5)
        poll = await bot.stop_poll(chat_id=message.chat.id, message_id=msg.message_id)
        if int(poll['options'][0]["voter_count"]) > int(poll['options'][1]["voter_count"]) and \
                int(poll['options'][0]["voter_count"]) > 4:
            dt = datetime.now() + timedelta(hours=2)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(False), until_date=timestamp)
            del_mes = await message.reply(
                f'| <b>Решение было принято:</b> {name1}\n| <b>Жертва:</b> <a href="tg://user?id='
                f'{message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>'
                f'\n| <b>Срок наказания:</b> 2 часа ⏰\n| <b>Причина:</b> {comment}',
                parse_mode='html')
            await asyncio.sleep(5)
            await del_mes.delete()
            await msg.message_id.delete()
        else:
            del_mes = await bot.send_message(message.chat.id, f'<a href="tg://user?id='
                                                              f'{message.reply_to_message.from_user.id}">'
                                                              f'{message.reply_to_message.from_user.first_name}</a>, '
                                                              f'<b>живи... Пока что...</b>', parse_mode='html')
            await asyncio.sleep(5)
            await del_mes.delete()
    else:
        dt = datetime.now() + timedelta(hours=2)
        timestamp = dt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                       types.ChatPermissions(False), until_date=timestamp)
        del_mes = await bot.send_message(message.chat.id, f'<b>Суицидник </b><a href="tg://user?id='
                                                          f'{message.reply_to_message.from_user.id}">'
                                                          f'{message.reply_to_message.from_user.first_name}</a>, '
                                                          f'<b>получает 2 часа блокировки!!!</b>', parse_mode='html')
        await asyncio.sleep(5)
        await del_mes.delete()


# @dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!', is_chat_admin=True)
async def unban(message: types.Message):
    await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    del_mes = await bot.send_message(message.chat.id, 'Done')
    await asyncio.sleep(5)
    await del_mes.delete()


def register_handlers_bot_commands(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['бан', 'ban'], commands_prefix='!')
    dp.register_message_handler(unban, commands=['разбан', 'unban'], commands_prefix='!', is_chat_admin=True)
