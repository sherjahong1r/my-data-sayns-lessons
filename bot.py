# import logging

# from aiogram import Bot, Dispatcher, executor, types

# API_TOKEN = '8587860656:AAFU5H9M3htzPhOhrF4xCEzT7XgENbEKni8'

# # Configure logging 
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welkome(message: types.Message):
#     """
#     This handler will be called when user sends '/start' or '/help' command

#     """
#     await message.reply("Wikipediya Botiga Xush Kelibsiz!")
    
# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chad.id, message.text)
    
#     await message.answer(message.text)
    
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


           


    
# import logging
# import asyncio
# import nest_asyncio
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message

# API_TOKEN = "8587860656:AAFU5H9M3htzPhOhrF4xCEzT7XgENbEKni8"
# logging.basicConfig(level=logging.INFO)

# bot = Bot(API_TOKEN)
# dp = Dispatcher()
# router = Router()
# dp.include_router(router)

# @router.message(F.text == "/start")
# async def send_welcome(message: Message):
#     await message.answer("Vikipediya Botiga Xush Kelibsiz!")

# @router.message(F.text == "/help")
# async def send_help(message: Message):
#     await message.answer("Bu yordam bo‘limi")

# @router.message()
# async def echo(message: Message):
#     await message.answer(message.text)

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     nest_asyncio.apply()
#     asyncio.get_event_loop().run_until_complete(main())


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    