import discord

import json
import logging


with open('config.json', 'r') as cfgfile:
    conf = json.load(cfgfile)

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BotClient(discord.Client):
    async def on_ready(self):
        logger.info(f"Logged on as {self.user}")
    async def on_message(self, message: discord.Message):
        logger.debug(f"Message from {message.author}: {message.content}")
    

intents = discord.Intents.all()
intents.polls = False
intents.presences = False
intents.typing = False
intents.invites = False

if __name__ == "__main__":
    bot = BotClient(intents=intents)
    bot.run(conf["token"])
