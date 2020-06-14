import discord, os, time, random, json
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot


TOKEN = 'NzAyMDk0NjY1NzY3MzIxNjYw.Xtzahg.Y7BjDwFkWY9yXjHyOgfNZnLMXDQ'
client = commands.Bot(command_prefix = '$')


'''@client.event
async def on_member_join(member):
    await client.send_message(client.get_channel('12324234183172'), 'welcome')
'''
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
    await ctx.send(f'IF SAHIL READS THIS VI VON ZULUL')

@client.command()
async def caw(ctx):
    for i in range (10):
        await ctx.send('CAW')
        time.sleep(random.randint(0,60))

#@client.event
#async def on_message(message):
#    if client.user.mentioned_in(message) and message.mention_everyone is False:
#        await message.channel.send('TriHard')

        
client.run(TOKEN)