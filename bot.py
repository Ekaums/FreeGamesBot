import requests
import json
import discord
import responses    
# https://jsoneditoronline.org/  <-- Good tool for JSON


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "MTA1NjM3NjI0NTQzMDAxMzk5NA.GSLtgY.UehiBlWxgDWo-7kdHsInwv0F-I5QTibU0fWOzE"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' in {channel}")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)
        
    client.run(TOKEN)







# Send HTTP request to GET this info
#response = requests.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=CA&allowCountries=CA")

# Convert this data to JSON form
#data = response.json()

#print(data["data"]["Catalog"]["searchStore"]["elements"])

#for info in data["data"]["Catalog"]["searchStore"]["elements"]:
 #   print([info["title"]])




## Get all current free games



## Today's Current Free Game

"""
print("TODAY\'S FREE GAMES:")
print()

response = requests.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=CA&allowCountries=CA")
data = response.json()
# Through Chrome Dev Tools, it is revealed that this request header will provide the data regarding today's free games


games = data["data"]["Catalog"]["searchStore"]["elements"]
# This will return a list, with one element being the current redeemable game, and the other being the new game

for game in games: # Both elements of the list are dictionaries, with values
    print(game["title"])
    # Image of game / Hyperlink?
    # Description




"""



## Promotions




## Notify when new game is released
