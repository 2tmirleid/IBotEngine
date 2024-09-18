import asyncio
import os

from dotenv import load_dotenv, find_dotenv

from src.example_dir import example_router, example_scene
from core.setup.setuper import IBotEngineSetuper

"""Main app class"""


class Main:
    def __init__(self):
        load_dotenv(find_dotenv())

        self.bot = IBotEngineSetuper(token=os.environ["TOKEN"],
                                     routers=[example_router.router],
                                     scenes=[example_scene.router])
    
    async def start(self):
        await self.bot.launch()


if __name__ == "__main__":
    main = Main()
    asyncio.run(main.start())
