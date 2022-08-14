from aiogram import types, Dispatcher
from create_bot import bot


def bad_words(message):
    check = False
    bw = ['блядь', 'бляха-муха', 'бля', 'бля буду', 'блядство', 'блядун', 'бляди', 'блядское', 'блядская', 'блядские',
          'блядский', 'блядища', 'блядовать', 'выблядок', 'ебёныть', 'ёбнулся', 'ёб', 'ебать', 'ебанутый',
          'ебать-копать', 'ебать', 'ебаться', 'ёбырь', 'ебальник', 'ебало', 'ебло', 'ёбнуть', 'ебануть', 'ёбнутый',
          'выебнулся', 'наебнуться', 'выебнуться', 'долбоёб', 'заеблись', 'заебатый', 'настоебенить', 'настоебать',
          'ебаквакнуться', 'наебать', 'ебысь', 'еблысь', 'наёбка', 'подъебать', 'подъёб', 'подъёбка',
          'поебать', 'поебень', 'поеботина', 'коноебля', 'коноёбиться', 'ебля', 'уёбище', 'бомбоуёбище', 'уёбывать',
          'съёбывать', 'изъебнуться', 'изъёб', 'невъебенно', 'заебатый', 'заебательский', 'разъебай', 'разъёба',
          'поёбка', 'еблан', 'ебанат', 'туебень', 'ёбово', 'еботятина', 'ебливый', 'ебучий', 'злоебучий', 'косоёбиться',
          'шароёбиться', 'пиздец', 'пизда', 'спизжены', 'пизды', 'пизд', 'опиздол', 'пиздо', 'хуёвый', 'хуёво', 'хуета',
          'нехуй', 'хуйня', 'хуетень', 'хуёвина', 'хуётина', 'хули', 'хуячить', 'хуярить', 'хуярыжить', 'охуенный',
          'охуительный', 'охуевательный', 'охуенный', 'охуеть', 'ни хуя', 'нихуя', 'не хуя', 'нехуя', 'по хую', 'похую',
          'по хуй', 'похуй', 'хуяк',
          'похуист', 'похуизм', 'на хуй', 'нахуй', 'хуила', 'хуебяка', 'хуйнуть', 'семихуй', 'полухуй', 'хуемполбия',
          'хуесос']
    for i in bw:
        if i in message.text.lower():
            check = True
    return check


# @dp.message_handler(content_types=['new_chat_members'])
async def del_new(message):
    await bot.delete_message(message.chat.id, message.message_id)


# @dp.message_handler(content_types=['any'])
async def delete_messages(message: types.Message):
    if bad_words(message) is True:
        await message.reply(f'<b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>, '
                            f'у нас не матерятся!</b>', parse_mode='html')
        await message.delete()
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEFjwABYvjHWC8yVvt-gQcTL8wytAVmRnMAAjosAAL8eDlLFcEUfmcSuwkpBA')
    check = 0
    is_admin = await bot.get_chat_administrators(message.chat.id)
    wl = ['https://t.me/c/', 'github.com']
    for i in range(len(is_admin)):
        if int(message.from_user.id) == int(is_admin[i]['user']['id']):
            check = 0
    if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document' or \
            message.content_type == 'audio' or message.content_type == 'album':
        for i in wl:
            if i in message.caption:
                check = 1
    else:
        for i in wl:
            if i in message.text:
                check = 1
    if check == 0:
        count = 0
        if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document' or \
                message.content_type == 'audio' or message.content_type == 'album':
            for caption_entity in message.caption_entities:
                if caption_entity.type in ["url", "text_link", "hlink"] and count == 0:
                    for i in range(len(is_admin)):
                        if not is_admin[i]['user']['is_bot'] and int(
                                is_admin[i]['user']['id']) != 1387606641:
                            try:
                                await bot.send_message(is_admin[i]['user']['id'],
                                                       f'<b>Сообщение: </b>{message.caption}\n\n'
                                                       f'<b>Отправитель: </b><a href="tg://user?id='
                                                       f'{message.from_user.id}">'
                                                       f'{message.from_user.full_name}</a>'
                                                       f'\n\n<b>Ссылка на сообщение: </b>{message.url}',
                                                       parse_mode="html")
                                count += 1
                            except:
                                i += 1
        else:
            for entity in message.entities:
                if entity.type in ["url", "text_link", "hlink"] and count == 0:
                    for i in range(len(is_admin)):
                        if not is_admin[i]['user']['is_bot'] and int(is_admin[i]['user']['id']) != 1387606641:
                            try:
                                await bot.send_message(is_admin[i]['user']['id'],
                                                       f'<b>Сообщение: </b>{message.text}\n\n'
                                                       f'<b>Отправитель: </b><a href="tg://user?id='
                                                       f'{message.from_user.id}">'
                                                       f'{message.from_user.full_name}</a>'
                                                       f'\n\n<b>Ссылка на сообщение: </b>{message.url}',
                                                       parse_mode="html")
                                count += 1
                            except:
                                i += 1
    ck1 = 0
    ck2 = 0
    check1 = ['gitignore', 'git ignore', 'гитигнор', 'гит игнор']
    check2 = ['пришлите', 'скиньте', 'дайте', 'скинь']
    s = message.text.lower()
    for i in check1:
        if i in s:
            ck1 = 1
    for j in check2:
        if j in s:
            ck2 = 1
    if ck1 == 1 and ck2 == 1:
        await message.reply(f'Лови https://t.me/c/1745662062/9222')


def register_handlers_bot_handlers(dp: Dispatcher):
    dp.register_message_handler(del_new, content_types=['new_chat_members'])
    dp.register_message_handler(delete_messages, content_types=['any'])
