import discord, os, time, random, json
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot

TOKEN = 'redacted'
client = commands.Bot(command_prefix = '$')
os.chdir(r'C:\Users\chiku\Downloads\Gigachad')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'your retarded ass is delayed by {round(client.latency * 1000)} ms')

@client.command()
async def zulul(ctx):
    await ctx.send(f'IF SAHIL READS THIS VI VON ZULUL')

@client.command()
async def caw(ctx):
    for i in range (10):
        await ctx.send('CAW')
        time.sleep(random.randint(0,60))

@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and message.mention_everyone is False:
        await message.channel.send('TriHard')

    if 'GIGACHAD' or 'giga chad' in message.clean_content.lower():
        await message.channel.send('Based and {}'.format(client.get_emoji(702109677839712356)))
    await client.process_commands(message)
        
        
client.run(TOKEN)