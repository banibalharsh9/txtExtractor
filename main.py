import os
import asyncio
import logging
from config import Config
from pyrogram import Client, idle
import tgcrypto  # Ensure this is necessary for your bot; otherwise, you can remove it.
from pyromod import listen
from logging.handlers import RotatingFileHandler
import http.server
import socketserver
from threading import Thread

# Configure logging
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

# Define authorized users
AUTH_USERS = [int(chat) for chat in Config.AUTH_USERS.split(",") if chat != ""]

# Simple HTTP server to keep the platform happy with port binding
def start_server():
    port = int(os.environ.get("PORT", 8080))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        LOGGER.info(f"Serving on port {port}")
        httpd.serve_forever()

# Main function to initialize and start the bot
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
        await idle()  # Keeps the bot running

    try:
        # Start the HTTP server in a separate thread
        server_thread = Thread(target=start_server)
        server_thread.start()

        # Start the bot asynchronously
        asyncio.get_event_loop().run_until_complete(run_bot())
        LOGGER.info("Bot running...")
    except Exception as e:
        LOGGER.error("An error occurred during bot execution:", exc_info=True)
    finally:
        LOGGER.info("Bot stopped")

if __name__ == "__main__":
    LOGGER.info("Bot script started")
    try:
        main()
    except Exception as e:
        LOGGER.error("An error occurred during initialization:", exc_info=True)
