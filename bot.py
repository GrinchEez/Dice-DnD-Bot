import asyncio
from aiogram import Bot, Dispatcher
from handlers import dices, start, help, stats
import config
# Запуск бота
async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp.include_routers(dices.router, start.router, help.router, stats.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())