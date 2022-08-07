import asyncio
from pyrogram import Client

api_id = 12345
api_hash = "5290496073:AAGr8DiKkiyk1LeY81inSUKCZqiWQ0nuwy4"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
