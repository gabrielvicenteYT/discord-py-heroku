import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("Logged in as {}({})".format(bot.user.name, bot.user.id))

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await bot.change_presence(activity=stream)
if __name__ == "__main__":
    bot.run(TOKEN)
