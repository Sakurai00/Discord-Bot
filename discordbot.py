import discord
from discord.ext import commands
import settings as st


discord_intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix = "!",
    case_insensitive=True,
    intents = discord_intents,
    activity = discord.Game("Bot test")
)



@bot.event
async def on_ready():
    print(discord.__version__ + "ready")

@bot.command()
async def whoami(ctx):
    await ctx.send(ctx.message.author.name)




def main():
    try:
        bot.loop.run_until_complete(bot.start(st.TOKEN))
    except KeyboardInterrupt:
        bot.loop.run_until_complete(bot.close())


if __name__ == '__main__':
    main()