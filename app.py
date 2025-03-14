'''Entry point for the bot'''

print('Entered bot...')

import os
import discord
from discord.ext import commands

print('Imported discord...')

intents = discord.Intents.default()
intents.message_content = True

print('Created intents...')

bot = commands.Bot(command_prefix='/', intents=intents)

print('Created bot...')

TOKEN = os.getenv("DISCORD_TOKEN")

print('Got token...')

@bot.event
async def on_ready():
    '''Prints a message when the bot is ready'''
    print(f'{bot.user} is online!')

@bot.command()
async def ping(ctx):
    '''Responds with pong'''
    await ctx.send('pong')

print('Ready to run...')
bot.run(TOKEN)
