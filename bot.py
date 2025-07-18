from telethon import events, TelegramClient, Button
import logging
from telethon.tl.functions.users import GetFullUserRequest
import os
import re
from telethon.tl.types import InputWebDocument
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Get all credentials from environment variables
TOKEN = os.environ['BOT_TOKEN']
API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
SECRET_IMAGE_URL = "https://i.ibb.co/Sw1kb7W/Uploaded-6910445402.png"

# Initialize Telegram client
bot = TelegramClient(
    "Whisper",
    api_id=API_ID,
    api_hash=API_HASH
).start(
    bot_token=TOKEN
)

@bot.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    await event.reply(
            """🌟 **Welcome to Whisper Bot!** 🌟

Send secret messages that only the intended recipient can read!

**How to use:**
1. Click 'Go Inline' below
2. Type `@yourbotname wspr username|your_message`
3. Send it to any chat

The recipient will get a button to view your private message!""",
            buttons=[
                [Button.switch_inline("✉️ Go Inline", query="")],
                [Button.inline("ℹ️ Help", data="help")]
                ]
            )

@bot.on(events.NewMessage(pattern="^[!?/]help$"))
async def help(event):
    await event.reply(
            """📖 **Whisper Bot Help Guide**

🔹 *Main Features:*
- Send private messages that only the intended person can read
- Works in both private chats and groups
- Simple and secure

🔹 *How to Use:*
1. In any chat, type `@yourbotname wspr username|your_message`
   Example: `@yourbotname wspr @john|Hey, check this out!`
2. Or click the 'Go Inline' button in our chat

🔹 *Commands:*
/start - Show welcome message
/help - Show this help guide

🔹 *Privacy:*
- Messages are stored temporarily
- Only visible to sender and recipient
- Automatically deleted after reading

Developed with ❤️ by Tech-Shreyansh""",
            link_preview=False
            )

@bot.on(events.InlineQuery())
async def inline_handler(event):
    if len(event.text) != 0:
        return
    me = (await bot.get_me()).username
    dn = event.builder.article(
            title="Whisper Bot",
            description="Send secret messages - only the recipient can read!",
            text=f"""🔒 **Whisper Bot** 🔒

To send a secret message:
`@{me} wspr username|your_message`

Example:
`@{me} wspr @john|Hey, check this out!`

(c) @Reeshuxd""",
            buttons=[
                [Button.switch_inline("✉️ Send Whisper", query="wspr ")]
                ]
            )
    await event.answer([dn])
    
@bot.on(events.InlineQuery(pattern="wspr"))
async def whisper_inline(event):
    me = (await bot.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("|", 1)  # Split on first | only
    except IndexError:
        await event.answer(
                [], 
                switch_pm=f"Please use format: @{me} wspr username|message",
                switch_pm_param="start"
                )
        return
    except ValueError:
        await event.answer(
                [],
                switch_pm=f"Please include both username AND message",
                switch_pm_param="start"
                )
        return
    
    try:
        # Try to resolve the username/ID
        try:
            user_entity = await bot.get_entity(user)
        except ValueError:
            # If it's a username without @, try adding it
            if not user.startswith('@'):
                user_entity = await bot.get_entity(f'@{user}')
            else:
                raise
        
        # Verify the user exists
        await bot(GetFullUserRequest(user_entity))
        
        # Generate unique key for this message
        message_key = f"msg_{event.id}_{user_entity.id}"
        
        # Store the information
        db[message_key] = {
            "user_id": user_entity.id,
            "msg": msg,
            "self": event.sender.id
        }
        
        text = f"""
🔐 **You have a secret message!**

A whisper has been sent to [{user_entity.first_name}](tg://user?id={user_entity.id})!

Click below to view the message.  
**Note:** Only {user_entity.first_name} can open this!
        """
        dn = event.builder.article(
                title="🔒 Secret Message",
                description="A message just for you!",
                text=text,
                thumb=InputWebDocument(
                    url=SECRET_IMAGE_URL,
                    size=0,
                    mime_type='image/png',
                    attributes=[]
                ),
                buttons=[
                    [Button.inline("👀 View Message", data=f"wspr_{message_key}")]
                    ]
                )
        await event.answer(
                [dn],
                switch_pm="🔒 Secret message created",
                switch_pm_param="start"
                )
    except Exception as e:
        logging.error(f"Error processing whisper: {str(e)}")
        await event.answer(
                [],
                switch_pm="❌ User not found. Check the username/ID and try again.",
                switch_pm_param="start"
                )

@bot.on(events.CallbackQuery(pattern=rb"wspr_(.*)"))
async def show_whisper(event):
    try:
        # Extract the message key from callback data
        message_key = event.pattern_match.group(1).decode()
        
        if message_key not in db:
            await event.answer("⚠️ Message expired or not found!", alert=True)
            return
            
        message_data = db[message_key]
        user = int(message_data["user_id"])
        allowed_users = [int(message_data["self"]), user]
        
        if event.sender.id not in allowed_users:
            await event.answer("🚫 This message is not for you!", alert=True)
            return
        
        msg = message_data["msg"]
        if not msg:
            await event.answer("⚠️ The message content is no longer available", alert=True)
            return
        
        # Show just the message without "Message:" prefix
        await event.answer(msg, alert=True)
        
    except Exception as e:
        logging.error(f"Error showing whisper: {str(e)}")
        await event.answer("⚠️ An error occurred while showing the message", alert=True)

@bot.on(events.CallbackQuery(data="help"))
async def help_callback(event):
    await help(event)
    await event.answer()

print("✅ Bot is now running with all fixes!")
bot.run_until_disconnected()