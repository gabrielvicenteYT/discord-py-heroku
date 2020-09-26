import os
from discord.ext import commands

bot = commands.Bot(command_prefix="-")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def config(ctx):
    await ctx.send("Current Configs: `-Mineplex` `-Verus` `-Ghostly`")

@bot.command()
async def mineplex(ctx):
    await ctx.send("`Mineplex Config`")
    
if __name__ == "__main__":
    bot.run(TOKEN)
