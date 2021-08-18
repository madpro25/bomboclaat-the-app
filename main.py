import logging
import os
import sys
from bomboclaat.client import BomboClient
from dotenv import load_dotenv

# Basic logging of bot info
file_handler = logging.FileHandler("discord-bot.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)

stderr_handler = logging.StreamHandler()
stderr_handler.setLevel(logging.WARNING)

FORMAT = "[%(asctime)s] %(levelname)s:%(name)s: %(message)s"
handlers = [file_handler, stderr_handler]
logging.basicConfig(level=logging.DEBUG, handlers=handlers, format=FORMAT)

logger = logging.getLogger("bombobot")

if __name__ == "__main__":
    load_dotenv()
    BOT_TOKEN = os.getenv("BOMBO_BOT_TOKEN")
    if not BOT_TOKEN:
        logger.error("'BOMBO_BOT_TOKEN' environment variable not set")
        sys.exit(1)

    client = BomboClient()
    client.run(BOT_TOKEN)
