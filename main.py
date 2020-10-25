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
async def intent(ctx):
    embed=discord.Embed(title="Download", url="https://intent.store/intentlauncher/Intent%20Launcher.zip", description="Click to install the Intent Launcher.", color=0x00ff4c)
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx):
    embed=discord.Embed(title="Download", url="https://is.gd/RiskMC", description="Click to link to open RiskMC's channel.", color=0x00ff4c)
    await ctx.send(embed=embed)
    
@bot.command()
async def gravity(ctx): #best client ww 
    embed=discord.Embed(title="Gravity Discord", url="https://intent.store", description="Check out Gravity client. It's probably the best client out right now for the price. Has fastest non-blink fly for hypixel and has many bypasses for other servers such as Mineplex. All for that for only 12 dollars usd.")
    await ctx.send(embed=embed)
    
@bot.command()
async def help(ctx):
    await ctx.send("`Help:`\n**Commands**")
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
