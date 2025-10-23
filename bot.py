import discord
import requests
import json
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))


# ---------- Helper functions ----------

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    json_data = json.loads(response.text)
    return json_data.get("joke", "Couldn't fetch a joke 😅")

def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    json_data = json.loads(response.text)
    return json_data["slip"]["advice"]


def get_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    return response.json()[0]["url"]

def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    return response.json()["message"]


# ---------- Discord Bot Class ----------

class MyClient(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.intro_users = set()  # Track who got the intro message

    async def on_ready(self):
        print(f'✅ Logged on as {self.user}!')
        
        channel = self.get_channel(CHANNEL_ID)  # Replace with your channel ID (integer)

        if channel:
            await channel.send(
                "👋 **Hello everyone! I'm your fun bot!**\n"
                "Here’s what I can do:\n"
                "🐸 `$meme` – Random meme\n"
                "😂 `$joke` – Random joke\n"
                "💡 `$advice` – Random advice\n"
                "🐱 `$cat` – Cute cat pic\n"
                "🐶 `$dog` – Cute dog pic\n"
                "🧠 `$fact` – Random fact\n"
                "🕒 `$time` – Current time\n"
                "💬 `$hello` – Greet the bot\n"
                "❓ `$help` – Show this list again"
            )

    async def on_message(self, message):
        if message.author == self.user:
            return

        content = message.content.lower()

        # 👋 Send intro to new users once
        if message.author.id not in self.intro_users:
            await message.channel.send(
                f"👋 Hey {message.author.name}! I'm your friendly bot!\n"
                "Here’s what I can do:\n"
                "🐸 `$meme`, 😂 `$joke`, 💡 `$advice`, 🧠 `$fact`, "
                "🐱 `$cat`, 🐶 `$dog`, 🕒 `$time`, 💬 `$hello`, ❓ `$help`"
            )
            self.intro_users.add(message.author.id)

        # ---------- COMMANDS ----------

        if content.startswith('$meme'):
            await message.channel.send(get_meme())

        elif content.startswith('$hello'):
            await message.channel.send(f'Hey {message.author.name}! 👋')

        elif content.startswith('$fact'):
            facts = [
                "Bananas are berries, but strawberries aren’t 🍓",
                "Octopuses have three hearts 🐙",
                "Honey never spoils — edible even after thousands of years 🍯",
                "Cats can’t taste sweetness 😺",
                "Sloths can hold their breath longer than dolphins 🦥"
            ]
            await message.channel.send(random.choice(facts))

        elif content.startswith('$joke'):
            await message.channel.send(get_joke())

        elif content.startswith('$advice'):
            await message.channel.send(f"💡 {get_advice()}")

        elif content.startswith('$cat'):
            await message.channel.send(get_cat())

        elif content.startswith('$dog'):
            await message.channel.send(get_dog())

        elif content.startswith('$time'):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await message.channel.send(f"🕒 Current time: {now}")

        elif content.startswith('$help'):
            help_text = (
                "**🤖 Available Commands:**\n"
                "🐸 `$meme` - Random meme\n"
                "😂 `$joke` - Random joke\n"
                "💡 `$advice` - Random advice\n"
                "🐱 `$cat` - Random cat pic\n"
                "🐶 `$dog` - Random dog pic\n"
                "🧠 `$fact` - Random fact\n"
                "🕒 `$time` - Current time\n"
                "💬 `$hello` - Greet the bot\n"
                "❓ `$help` - Show this list"
            )
            await message.channel.send(help_text)

        # ❓ If unknown command
        elif content.startswith('$'):
            await message.channel.send(
                "❓ I didn’t recognize that command!\n"
                "Try one of these:\n"
                "🐸 `$meme`, 😂 `$joke`, 💡 `$advice`,  🧠 `$fact`, "
                "🐱 `$cat`, 🐶 `$dog`, 🕒 `$time`, 💬 `$hello`, ❓ `$help`"
            )


# ---------- Setup Intents ----------
intents = discord.Intents.default()
intents.message_content = True

# ---------- Run the bot ----------
client = MyClient(intents=intents)
client.run(TOKEN)  #  Replace with your token
