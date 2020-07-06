import discord, os, time, random, json
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot

f = open('token.json',) 

data = json.load(f) 

TOKEN = json.dumps(data['token'])
print(TOKEN)

f.close()

client = commands.Bot(command_prefix = '$')


currentTime = time.strftime("%w", time.gmtime())

@client.event
async def on_ready():
    print('Bot is ready')
#    print(time.gmtime().tm_wday)
    print(currentTime)

@client.command()
async def ping(ctx):
    await ctx.send(f'your retarded ass is delayed by {round(client.latency * 1000)} ms')

@client.command()
async def zulul(ctx):
    await ctx.send(f'IF RIDDHISH READS THIS VI VON ZULUL')

@client.command()
async def caw(ctx):
    for i in range (10):
        await ctx.send('CAW')
        time.sleep(random.randint(0,60))

@client.command()
async def statlemi(ctx):
    await ctx.send('LEMI PUT MY NUTS ON YOUR FACE LOL')

        
client.run(TOKEN)