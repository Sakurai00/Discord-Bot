import os, discord
from discord.ext import commands
import settings

TOKEN = settings.TOKEN
bot = commands.Bot(command_prefix = "!")
presence = discord.Game("Bot test")



@bot.event
async def on_ready():
    print(discord.__version__)
    print("ready.")
    await bot.change_presence(activity = presence)

@bot.command()
async def whoami(ctx):
    await ctx.send(ctx.message.author.name)




def main():
    #bot.run(TOKEN)
    try:
        bot.loop.run_until_complete(bot.start(TOKEN))
    except KeyboardInterrupt:
        bot.loop.run_until_complete(bot.close())

if __name__ == '__main__':
    main()