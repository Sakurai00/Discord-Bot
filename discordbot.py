import discord, os
import settings

TOKEN = settings.TOKEN
client = discord.Client()








def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()