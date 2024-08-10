import os
import asyncio
import logging
from config import Config
from pyrogram import Client, idle
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ]
)

AUTH_USERS = [int(chat) for chat in Config.AUTH_USERS.split(",") if chat != ""]


def main():
    LOGGER.info("Starting bot initialization")
    bot = Client(
        "macc",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=20,
        plugins=dict(root="plugins"),
        workers=50,
    )

    async def run_bot():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"Bot @{bot_info.username} started")
        await idle()

    # Bind the bot to the port provided by the environment
    port = int(os.environ.get(PORT, 8080))
    os.environ["FLASK_RUN_PORT"] = str(port)
    
    try:
        asyncio.get_event_loop().run_until_complete(run_bot())
        LOGGER.info("Bot running...")
    except Exception as e:
        LOGGER.error("An error occurred:", exc_info=True)

    LOGGER.info("Bot stopped")

if __name__ == "__main__":
    LOGGER.info("Bot script started")
    try:
        main()
    except Exception as e:
        LOGGER.error("An error occurred during initialization:", exc_info=True)

