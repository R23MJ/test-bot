'''Entry point for the bot'''

import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    '''Prints a message when the bot is ready'''
    print(f'{bot.user} is online!')

@bot.command()
async def ping(ctx):
    '''Responds with pong'''
    await ctx.send('pong')

bot.run(TOKEN)
