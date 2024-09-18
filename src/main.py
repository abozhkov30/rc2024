import asyncio
from pprint import pprint
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import types
from settings import BOT_TOKEN
from crud_function import insert_in_users, update_profiles
import time


loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

# @dp.message(F.text == '/start')
# async def start_command(message: Message):
#     await message.answer("Привет! Добро пожаловать в наш бот.")

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {message.from_user.full_name})!")
    await insert_in_users(message.from_user.id, 
                          message.from_user.username, 
                          message.from_user.first_name, 
                          message.from_user.last_name, 
                          message.from_user.language_code)
    # pprint(message.from_user)



@dp.message()
async def handle_command(message: types.Message) -> None:
    """
    This handler receives messages with a range of command
    """
    if message.text.startswith('/activate'):
        if await update_profiles(message.from_user.id, True, time.time()):
            await message.answer("Вы добавлены в таблицу!")
    if message.text.startswith('/deactivate'):
        if await update_profiles(message.from_user.id, False, time.time()):
            await message.answer("Вы удалены из таблицы!")

        





# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)



async def main():
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    asyncio.run(main())
    # loop.run_until_complete(run_connect())