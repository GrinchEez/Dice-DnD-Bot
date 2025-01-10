from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import random, array

router = Router()
@router.message(Command("stats"))
async def message_stats(message: Message):
    stats6 = [0,0,0,0,0,0]
    for i in range(6):
        RandArr = [0,0,0,0]
        for j in range(4):
            RandArr[j] = random.randint(1,6)
        stats6[i] = sum(RandArr) - min(RandArr)
    await message.answer(f"{stats6}")