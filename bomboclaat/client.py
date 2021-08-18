import logging
import discord

logger = logging.getLogger(__name__)


class BomboClient(discord.Client):
    async def on_ready(self):
        logger.warning(f"We have logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")
