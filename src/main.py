import discord

import json
import logging


with open('config.json', 'r') as cfgfile:
    conf = json.load(cfgfile)

logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s:%(message)s", level=logging.WARNING, filename='lemon.log', filemode='a')
logger = logging.getLogger('lemon')


intents = discord.Intents.all()
intents.polls = False
intents.presences = False
intents.typing = False
intents.invites = False


bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    logger.info(f"Logged on as {bot.user}")

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    logger.debug(f"Message from {message.author}: {message.content}")

    if message.content.startswith(".hello"):
        await message.channel.send("Hello.")
    

if __name__ == "__main__":
    bot.run(conf["token"])
