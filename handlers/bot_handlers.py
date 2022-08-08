from aiogram import types, Dispatcher
from create_bot import bot


# @dp.message_handler(content_types=['new_chat_members'])
async def del_new(message):
    await bot.delete_message(message.chat.id, message.message_id)


# @dp.message_handler(content_types=['any'])
async def delete_messages(message: types.Message):
    check = 0
    is_admin = await bot.get_chat_administrators(message.chat.id)
    wl = ['https://t.me/c/', 'github.com']
    for i in range(len(is_admin)):
        if int(message.from_user.id) == int(is_admin[i]['user']['id']):
            check = 1
    if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document':
        for i in wl:
            if i in message.caption:
                check = 1
    else:
        for i in wl:
            if i in message.text:
                check = 1
    if check == 0:
        if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document':
            for caption_entity in message.caption_entities:
                if caption_entity.type in ["url", "text_link", "hlink"]:
                    await message.delete()
        else:
            for entity in message.entities:
                if entity.type in ["url", "text_link", "hlink"]:
                    await message.delete()


def register_handlers_bot_handlers(dp: Dispatcher):
    dp.register_message_handler(del_new, content_types=['new_chat_members'])
    dp.register_message_handler(delete_messages, content_types=['any'])