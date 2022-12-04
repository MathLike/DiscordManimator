import os
import traceback

import config
import discord
from discord.ext import commands

from pathlib import Path
import asyncio

bot = commands.Bot(
    description="Manim Community Discord Bot",
    activity=discord.Game("Animating with Manim"),
    help_command=None,
    command_prefix=config.PREFIX,
    case_insensitive=True,
    strip_after_prefix=True,
    intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

async def load_extensions():
    for extension in os.listdir(Path(__file__).parent/"cogs/"):
        if extension.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{extension[:-3]}")
            except Exception:
                print(f"{extension} couldn't be loaded.")
                traceback.print_exc()
                print("")

async def main():
    await load_extensions()
    await bot.start(config.TOKEN)

asyncio.run(main())