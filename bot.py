from aiogram.utils import executor
from create_bot import dp
from handlers import bot_handlers, bot_commands

bot_commands.register_handlers_bot_commands(dp)
bot_handlers.register_handlers_bot_handlers(dp)

print('run')
executor.start_polling(dp)
