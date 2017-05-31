import discord
import random
import bot
import json
from discord.ext import commands


description = "Aryas-Bot"
bot_prefix = '?'

with open('secrets.json') as data_file:
    SECRETS = json.load(data_file)

bot = commands.Bot(command_prefix='?', description=description)



@bot.event
async def on_ready():
    print('Logged in')
    print('Name : {}'.format(bot.user.name))
    print('ID : {}'.format(bot.user.id))
    print(discord.__version__)



@bot.command(pass_context = True)
async def clear(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await bot.delete_message(x)
            counter += 1
            await asyncio.sleep(0.1) #1.2 second timer so the deleting process can be even


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('Pong!')

bot.run(SECRETS['discord']['token'])
