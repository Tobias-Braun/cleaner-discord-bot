import os
import discord
import asyncio
import json
import re
import os


TOKEN = os.environ["DISCORD_CLEANER_BOT_TOKEN"]

client = discord.Client()

channels_to_clean = ["general", "lululul😀"]
bot_channels_to_clean = ["bot_usage"]


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):

    data = {}

    with open('config.json') as f:
        data = json.load(f)

    cleanToken = data["cleanToken"]
    channels_to_clean = data["channelsToClean"]
    bot_channels_to_clean = data["botChannelsToClean"]
    bot_channel_clean_delay = data["botChannelCleaningDelay"]
    pattern = re.compile(f"{cleanToken}")
    print(pattern)
    if pattern.match(message.content):
        channel = message.channel
        print(channel.name)
        if channel.name in channels_to_clean:
            await message.delete()
        if channel.name in bot_channels_to_clean:
            await asyncio.sleep(int(bot_channel_clean_delay))
            await message.delete()

client.run(TOKEN)
