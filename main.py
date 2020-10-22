import os
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="$")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def intent(ctx):
    await ctx.send("`Intent Download`\nhttps://intent.store/intentlauncher/Intent%20Launcher.zip")
@bot.command()
async def youtube(ctx):
    await ctx.send("Don't forget to subscribe to RiskMC!\nhttps://is.gd/RiskMC")
    
@bot.command()
async def gravity(ctx):
    await ctx.send("Gravity is probably the best client for the price right now. Has the fastest non blink fly and has unmatchable bypasses. Buy it from https://intent.store")
    
    
    
# @bot.command()
#async def nuke(ctx, channel: discord.TextChannel = None):
#   """Nuke a whole Channel"""
#   channel = channel if channel else ctx.channel
#  newchannel = await channel.clone()
#   await newchannel.edit(position=channel.position)
#    await channel.delete()
#   await newchannel.send(
#       embed=ctx.embed(
#           footer=f'💣 Channel #{channel.name} successfully nuked by '
#                  f'{ctx.author.display_name}',
#           color=0x1FFF00), delete_after=30)
    
    

if __name__ == "__main__":
    bot.run(TOKEN)
