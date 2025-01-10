from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def message_start(message: Message):
    await message.answer("Привет я D&D бот. Я могу помочь тебе с броском кубика и характеристиками персанажа.\n /help")