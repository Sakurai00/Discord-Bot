import discord, os

TOKEN = os.environ["DiscordBotToken"]
client = discord.Client()








def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()