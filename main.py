import os
from bomboclaat.client import BomboClient
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    BOT_TOKEN = os.getenv("BOMBO_BOT_TOKEN")
    if not BOT_TOKEN:
        raise Exception("BOMBO_BOT_TOKEN not set")

    client = BomboClient()
    client.run(BOT_TOKEN)
