from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import random 

router = Router()

@router.message(Command("d2"))
async def answer_d2(message: Message):
    await message.answer(str(random.randint(1, 2)))

@router.message(Command("d4"))
async def answer_d4(message: Message):
    await message.answer(str(random.randint(1, 4)))

@router.message(Command("d6"))
async def answer_d6(message: Message):
    await message.answer(str(random.randint(1, 6)))

@router.message(Command("d8"))
async def answer_d8(message: Message):
    await message.answer(str(random.randint(1, 8)))

@router.message(Command("d10"))
async def answer_d10(message: Message):
    await message.answer(str(random.randint(1, 10)))

@router.message(Command("d20"))
async def answer_d20(message: Message):
    await message.answer(str(random.randint(1, 20)))

@router.message(Command("d100"))
async def answer_d100(message: Message):
    await message.answer(str(random.randint(1, 100)))
