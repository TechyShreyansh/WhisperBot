# 🤫 Whisper Bot

Whisper Bot is a **secret messaging Telegram bot** that allows you to send private messages that **only the intended recipient can read**.

---

## ✨ Features
✅ **Private whispers** – only the recipient can read  
✅ **Works in groups and private chats**  
✅ **Temporary messages, auto-delete**  
✅ **Lightweight and secure**  
✅ **Inline mode support**  

---

## 🚀 How It Works
1️⃣ In any chat, type:  
```
@yourbotusername wspr username|your_secret_message
```
Example:  
```
@yourbotusername wspr @john|Hey, this is a secret!
```

2️⃣ The recipient will get a **👀 View Message** button  

3️⃣ **Only they can open the secret** ✅  

---

## 🛠 Installation

### 1️⃣ Requirements
- Python 3.9+  
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)  
- Telegram API credentials from [my.telegram.org](https://my.telegram.org)  

---

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/TechyShreyansh/WhisperBot
cd WhisperBot
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File
```env
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
```

---

### 5️⃣ Run the Bot
```bash
python bot.py
```

✅ Your bot will now start running  

---

## 📜 Commands

| Command  | Description |
|----------|-------------|
| `/start` | Show welcome message |
| `/help`  | Show help guide |

Inline Mode:  
```
@yourbotusername wspr username|secret_message
```

---

## 📂 Project Structure

```
📂 WhisperBot
 ├── bot.py           # Main bot code
 ├── requirements.txt # Python dependencies
 ├── .env             # Environment variables
 └── README.md        # This file
```

---

## 🖥 Code Snapshot

```python
from telethon import events, TelegramClient, Button
import logging, os
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputWebDocument
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

TOKEN = os.environ['BOT_TOKEN']
API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
SECRET_IMAGE_URL = "https://i.ibb.co/Sw1kb7W/Uploaded-6910445402.png"

bot = TelegramClient("Whisper", API_ID, API_HASH).start(bot_token=TOKEN)

# ... event handlers, inline whisper logic, callbacks ...

print("🤫 Whisper Bot is now running!")
bot.run_until_disconnected()
```

---

## ☁️ Deployment

You can host it anywhere:
- **Koyeb (free & easy)**
- **Replit**
- **Heroku**
- **Docker**

---

## 🤝 Contribute
Feel free to **fork**, improve, and create a **Pull Request**!  

---

## 📜 License
MIT License – free to use ✅  

---

**Developed with ❤️ by [Tech Shreyansh](https://github.com/TechyShreyansh)**  

---
s
### 💡 Example Usage
```
@whisperbot wspr @alice|This is a top-secret message! 🤫
```
The recipient will only see a **👀 View Message** button, and only they can open it!  

---
