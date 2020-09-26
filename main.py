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
   

@bot.command(name="nuke")
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        """Nuke a whole Channel"""
        channel = channel if channel else ctx.channel
        newchannel = await channel.clone()
        await newchannel.edit(position=channel.position)
        await channel.delete()
        await newchannel.send(
            embed=ctx.embed(
                footer=f'💣 Channel #{channel.name} successfully nuked by '
                       f'{ctx.author.display_name}',
                color=0x1FFF00), delete_after=30)
    
    

if __name__ == "__main__":
    bot.run(TOKEN)
