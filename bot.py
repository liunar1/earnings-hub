import nextcord
from nextcord.ext import commands
import json
import requests
import web_retrieve

intents = nextcord.Intents.default()
intents.message_content = True # this is to allow the bot to send messages
bot = commands.Bot(command_prefix='$', intents=intents) # $ goes before every command

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def earnings(ctx):
    start = "2025-03-03"
    end = "2025-03-07"

    url = f"https://api.savvytrader.com/pricing/assets/earnings/calendar?start={start}&end={end}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  
        # print(type(data))
        # print(json.dumps(data, indent=2))
        await ctx.send(f"companies earnings from {start} to {end}:")
        for company in data:
            await ctx.send(f"{company['symbol']} - {company['assetName']} on {company['earningsDate']}")
        with open("earnings.json", "w") as earnings_json:
            json.dump(data, earnings_json, indent=4)
    else:
        print("Request failed with status:", response.status_code)
    # await web_retrieve.get_page()
    await ctx.send("hi")

my_json = None
with open("keys.json", "r") as keys:
    my_json = json.load(keys)

token = my_json["token"]
bot.run(token)
