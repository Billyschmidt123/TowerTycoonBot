import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")  # From Stripe

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Simulated in-memory user data
user_data = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {"coins": 0, "upgrade": False}
    await message.answer("🏗️ Welcome to *Tower Tycoon*! Tap /tap to earn coins!", parse_mode="Markdown")

@dp.message_handler(commands=['tap'])
async def tap(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["coins"] += 10
    coins = user_data[user_id]["coins"]
    await message.answer(f"💰 You earned 10 coins! Total: {coins}")

    # Trigger upgrade offer at 300 taps
    if coins >= 300 and not user_data[user_id]["upgrade"]:
        await message.answer(
            "🔥 You've unlocked the *Architect Blueprint*! Get:\n"
            "- ⚡ Auto-Builder\n- 🏗️ Golden Floors\n- 💸 Double Coins\n\n"
            "🎁 Only $5 to unlock forever!\nPress /buy to upgrade.",
            parse_mode="Markdown"
        )

@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    prices = [LabeledPrice(label="Golden Architect Upgrade", amount=500 * 100)]  # Amount in cents
    await bot.send_invoice(
        message.chat.id,
        title="Tower Tycoon Premium",
        description="Unlock Auto Builder, Offline Income, Double Coins!",
        provider_token=PROVIDER_TOKEN,
        currency="USD",
        prices=prices,
        start_parameter="tower_tycoon_upgrade",
        payload="premium_upgrade"
    )

@dp.pre_checkout_query_handler(lambda q: True)
async def pre_checkout(pre_checkout_q: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["upgrade"] = True
    await message.answer("🎉 Upgrade successful! Auto-tapping unlocked, and income doubled!")
