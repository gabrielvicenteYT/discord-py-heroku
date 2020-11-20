import os
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="$")
bot.remove_command('help')
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def youtube(ctx):
    embed=discord.Embed(title="YouTube", url="https://is.gd/", description="Check out _____'s Youtube Channel!.", color=0x00ff4c)
    await ctx.send(embed=embed)
    
@bot.command()
async def help(ctx):
    await ctx.send("`Help:`\n**Commands**")

if __name__ == "__main__":
    bot.run(TOKEN)
