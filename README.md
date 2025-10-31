
# 🤖 Fun Discord Bot

## 🎥 Demo



https://github.com/user-attachments/assets/7ef708be-779f-4958-b56f-14365f9d2461


A simple and fun Discord bot built using **Python** and **discord.py** that sends memes, quotes, jokes, and fun facts — all through simple chat commands!  
It’s lightweight, beginner-friendly, and perfect for learning API integration in Discord bots.

---

## 🌟 Features

✅ `$meme` → Sends a random meme 😆 <br>
✅ `$advice` → Gives a random advice 😇 <br>
✅ `$joke` → Tells a random joke 😂  
✅ `$fact` → Shares an interesting fact 🤯  
✅ `$help` → Lists all available commands 📜  

---

## 🛠️ Tech Stack

- 🐍 Python 3.9+
- 💬 [discord.py](https://discordpy.readthedocs.io/)
- 🌍 [python-dotenv](https://pypi.org/project/python-dotenv/)
- 🌐 Public APIs (Meme, ZenQuotes, Joke, Useless Facts)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fun-discord-bot.git
cd fun-discord-bot
````

### 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can create one with:

```bash
pip freeze > requirements.txt
```

**Required packages:**

```
discord.py
requests
python-dotenv
```

---

### 3️⃣ Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** → Give it a name
3. Go to the **Bot** tab → Click **Add Bot**
4. Copy your **Token** (you’ll need it later)
5. Under **Privileged Gateway Intents**, enable:

   * ✅ Message Content Intent
   * ✅ Presence Intent *(optional)*

---

### 4️⃣ Create a `.env` File

Create a new file named `.env` in your project folder and add:

```
DISCORD_TOKEN=your_bot_token_here
CHANNEL_ID=123456789012345678
```

⚠️ **Do NOT share this file or upload it to GitHub!**
Add `.env` to your `.gitignore` file like this:

```
.env
```

---

### 5️⃣ Run the Bot

Run the bot in your terminal:

```bash
python bot.py
```

You should see:

```
✅ Logged on as MyBot#1234
```

Then, in your Discord server, type:

```
$meme
$advice
$joke
$fact
$help
```

---

## 🧩 API Sources

| Feature | API Used          | Endpoint                                                                                                     |
| ------- | ----------------- | ------------------------------------------------------------------------------------------------------------ |
| Meme    | Meme API          | [https://meme-api.com/gimme](https://meme-api.com/gimme)                                                     |
| Advice  | Advice API     | [https://api.adviceslip.com/advice](https://api.adviceslip.com/advice)                                           |
| Joke    | Official Joke API | [https://official-joke-api.appspot.com/random_joke](https://official-joke-api.appspot.com/random_joke)       |
| Fact    | Useless Facts API | [https://uselessfacts.jsph.pl/random.json?language=en](https://uselessfacts.jsph.pl/random.json?language=en) |

---

## 🔒 Security Tips

* 🔐 Never commit your `.env` file or bot token.
* 🛑 Always use `.gitignore` to exclude sensitive data.
* 🌀 If you accidentally leak your token, **regenerate it immediately** from the Developer Portal.

---
