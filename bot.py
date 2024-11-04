import logging
import logging.config
from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, PORT
from aiohttp import web
from plugins.web_support import web_server

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="instascrapper",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username 
       app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, PORT).start()
       logging.info(f"{me.first_name} ✅✅ BOT started successfully - ✅✅")

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped 🙄 - \nContact @LazyDeveloper on telegram for any query")
        
bot = Bot()
import logging
import logging.config
from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, PORT
from aiohttp import web
from plugins.web_support import web_server

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="instascrapper",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        logging.info(f"{me.first_name} ✅✅ BOT started successfully - ✅✅")

    async def stop(self, *args):
        await super().stop()      
        logging.info("Bot Stopped 🙄 - \nContact @LazyDeveloper on telegram for any query")

# Create a global bot instance
bot = Bot()

async def main():
    await bot.start()
    print("Bot is running...")

    # Keep the bot running indefinitely
    await bot.idle()

# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

