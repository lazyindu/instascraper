# instagram_login.py
import logging
import instaloader
from pyrogram import Client, filters

INSTAGRAM_SESSION_FILE = "instagram_session"

async def save_instagram_session(username, password):
    L = instaloader.Instaloader()
    try:
        L.login(username, password)
        L.save_session_to_file(INSTAGRAM_SESSION_FILE)
        return True
    except instaloader.exceptions.LoginException as e:
        logging.error(f"Login failed: {e}")
        return False

@Client.on_message(filters.private & filters.command(["login"]))
async def login(client, message):
    args = message.command[1:]  # Get command arguments
    if len(args) != 2:
        await message.reply_text("Usage: /login {username} {password}")
        return
    
    username, password = args
    success = await save_instagram_session(username, password)
    if success:
        await message.reply_text("Logged in successfully!")
    else:
        await message.reply_text("Login failed. Please check your credentials.")
