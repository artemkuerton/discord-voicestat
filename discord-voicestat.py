import discord
from discord.ext import commands
import asyncio
import collections

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary for storing usage time in the voice channel
user_time = collections.defaultdict(int)


@bot.event
async def on_ready():
    print(f'The bot is launched as {bot.user}')


@bot.event
async def on_voice_state_update(member, before, after):
    global user_time

    # Show the user when they enter a voice channel
    if after.channel is not None:
        print(f'{member.name} joined the channel {after.channel.name}')

        # Start a timer
        while member in after.channel.members:
            await asyncio.sleep(1)
            user_time[member.id] += 1  # Increase time by 1 second

    # Show the user when they leave the voice channel
    if before.channel is not None:
        print(f'{member.name} left the channel {before.channel.name}')


@bot.command()
async def time(ctx):
    # Command to check time spent in voice chat
    if ctx.author.id in user_time:
        await ctx.send(f'{ctx.author.name}, you spent {user_time[ctx.author.id]} seconds in voice chat.')
    else:
        await ctx.send(f'{ctx.author.name}, You havent spent any time in voice chat yet.')


# Running a bot
bot.run('TOKEN')
