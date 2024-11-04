from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import instaloader
import os
from config import START_PIC, FLOOD, ADMIN 

# Initialize Instagram loader
L = instaloader.Instaloader()

try:
    L.login("lazyprincesx", "zxc@786")
except instaloader.exceptions.LoginException as e:
    print(f"Login failed: {e}")


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user           
    txt = (f"👋 Hello {user.mention} \n\n"
           "I am an Advanced server uploader BOT with custom filename support.\n\n"
           "<blockquote>Send me any video or document!</blockquote>")
    
    button = InlineKeyboardMarkup([[ 
        InlineKeyboardButton('⚡️ About', callback_data='about'),
        InlineKeyboardButton('🤕 Help', callback_data='help')
    ], [
        InlineKeyboardButton("🐱‍👤 About Developer 🐱‍👤", callback_data='dev')
    ]])
    
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)

async def download_latest_reel(username):
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        if post.is_video:
            video_path = f"reels/{username}/{post.shortcode}.mp4"
            if not os.path.exists(video_path):  # Check if reel has been downloaded before
                os.makedirs(f"reels/{username}", exist_ok=True)
                L.download_post(post, target=f"reels/{username}")
                return video_path
    return None

async def post_reel_to_telegram(client, channel_username, video_path, caption):
    try:
        await client.send_video(channel_username, video_path, caption=caption)
        print(f"Reel posted to {channel_username}")
    except FloodWait as e:
        print(f"Rate limit hit! Waiting for {e.x} seconds.")
        await sleep(e.x)

async def automate_reels_posting(client, channels):
    for channel, insta_page in channels.items():
        video_path = await download_latest_reel(insta_page)
        if video_path:
            await post_reel_to_telegram(client, channel, video_path, f"New reel from @{insta_page}!")
        else:
            print(f"No new reel found for {insta_page}")

@Client.on_message(filters.private & filters.command("run"))
async def run_command(client, message):
    channels = {
        "@real_MoviesAdda7": "filmygyan",
        # Add more Instagram page - Telegram channel pairs as needed
    }
    
    await automate_reels_posting(client, channels)
    await message.reply_text("Checked for new reels and posted them if available.")


# from asyncio import sleep
# from pyrogram import Client, filters, enums
# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from pyrogram.errors import FloodWait
# import humanize
# import instaloader
# import os
# import time
# from config import START_PIC, FLOOD, ADMIN 
# from helper.utils import initate_lazy_verification

# # Initialize Instagram loader
# L = instaloader.Instaloader()

# @Client.on_message(filters.private & filters.command(["start"]))
# async def start(client, message):
#     user = message.from_user           
#     txt = f"👋 Hello {user.mention} \n\nI am an Advance server uploader BOT with custom filename support.\n\n<blockquote>Send me any video or document!</blockquote>"
#     button = InlineKeyboardMarkup([[ 
#         InlineKeyboardButton('⚡️ About', callback_data='about'),
#         InlineKeyboardButton('🤕 Help', callback_data='help')
#     ], [
#         InlineKeyboardButton("🐱‍👤 About Developer 🐱‍👤", callback_data='dev')
#     ]])
    
#     if START_PIC:
#         await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
#     else:
#         await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)

# async def download_latest_reel(username):
#     profile = instaloader.Profile.from_username(L.context, username)
#     for post in profile.get_posts():
#         if post.is_video:
#             video_path = f"reels/{username}/{post.shortcode}.mp4"
#             if not os.path.exists(video_path):  # Check if reel has been downloaded before
#                 os.makedirs(f"reels/{username}", exist_ok=True)
#                 L.download_post(post, target=f"reels/{username}")
#                 return video_path
#     return None

# async def post_reel_to_telegram(client:Client, channel_username, video_path, caption):
#     try:
#         await client.send_video(channel_username, video_path, caption=caption)
#         print(f"Reel posted to {channel_username}")
#     except FloodWait as e:
#         print(f"Rate limit hit! Waiting for {e.x} seconds.")
#         await sleep(e.x)

# async def automate_reels_posting(channels):
#     for channel, insta_page in channels.items():
#         video_path = await download_latest_reel(insta_page)
#         if video_path:
#             await post_reel_to_telegram(channel, video_path, f"New reel from @{insta_page}!")
#         else:
#             print(f"No new reel found for {insta_page}")

# @Client.on_message(filters.private & filters.command("run"))
# async def run_command(client, message):
#     channels = {
#         "@real_MoviesAdda7": "filmygyan",
#         # Add more Instagram page - Telegram channel pairs as needed
#     }
    
#     await automate_reels_posting(channels)
#     await message.reply_text("Checked for new reels and posted them if available.")

