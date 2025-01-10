from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def message_help(message: Message):
    await message.answer("Мои команды:\n /d2\n /d4\n /d6\n /d8\n /d10\n /d20\n /d100\n /stats")
