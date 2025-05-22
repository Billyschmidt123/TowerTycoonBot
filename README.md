# 🏗️ Tower Tycoon Bot

A Telegram game bot where users tap to earn coins and build towers. After 30 minutes, users are offered a $5 upgrade for auto-builders, double coins, and offline income.

## 🚀 Features
- Tap to earn coins
- Unlockable upgrade after 300 coins
- Telegram Payments via Stripe
- Built with Python and aiogram

## 🛠️ How to Deploy on Render

1. [Create a Render.com account](https://render.com)
2. Fork or upload this repo to GitHub
3. Click the button below to deploy:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/TowerTycoonBot)

4. Add Environment Variables on Render:
   - `BOT_TOKEN`: Your Telegram Bot token
   - `PROVIDER_TOKEN`: Your Stripe provider token

## 🧪 Testing
Use `/start`, `/tap`, and `/buy` on your bot after setup.
