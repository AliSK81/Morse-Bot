from aiogram import Bot, Dispatcher, executor, types
from Responses import *
from Constants import API_KEY

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("یه پیام به زبان انگلیسی یا morsor بفرست یا فروارد کن.")


@dp.message_handler()
async def chat(message: types.Message):
    try:

        answer = morsor(message.text)

        await message.reply(
            text=f'`{answer}`',
            parse_mode=types.ParseMode.MARKDOWN
        )

    except Exception as ex:
        # await message.answer("error. use /help")
        pass


if __name__ == '__main__':
    executor.start_polling(dp)
