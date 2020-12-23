import discord
from discord.ext import commands
import settings as st
import random


discord_intents = discord.Intents.all()

client = commands.Bot(
    command_prefix = "$",
    case_insensitive=True,
    intents = discord_intents,
    activity = discord.Game("Bot test")
)



@client.event
async def on_ready():
    print("v" + discord.__version__ + " ready")


@client.command()
async def whoami(ctx):
    await ctx.send(ctx.message.author.name)


@client.command()
async def roll(ctx, dice : str):
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        return
    ans = ""
    sum = 0
    for r in range(rolls):
        tmp = random.randint(1, limit)
        sum += tmp
        ans += (str(tmp) + " ")
    result = ans + " " + str(sum)
    await ctx.send(result)


def main():
    try:
        client.loop.run_until_complete(client.start(st.TOKEN))
    except KeyboardInterrupt:
        client.loop.run_until_complete(client.close())


if __name__ == '__main__':
    main()