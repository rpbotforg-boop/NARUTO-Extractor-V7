import asyncio
import logging
from pyrogram import Client, idle
from config import Config

# Logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")

# Bot client
bot = Client(
    "Master",
    bot_token="8225118430:AAEOFTRcVH3Au1LR0iFyasUb4U5CGATuoT4",
        api_id=22447622,
        api_hash="543b62d58d3e723e766ba57a984ab65d",
        sleep_threshold=120,
        plugins=dict(root="plugins"),
        workers=8
)

async def main():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"<--- @{bot_info.username} Started --->")

    await idle()

    await bot.stop()
    LOGGER.info("<--- Bot Stopped --->")

if __name__ == "__main__":
    asyncio.run(main())

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=PORT)
    
