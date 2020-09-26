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
   

@bot.command()
@has_permissions(Administrator=True)  
async def nuke(ctx, channel: discord.TextChannel = None):
    channel = channel if channel else ctx.channel
    newchannel = await channel.clone()
    if discord.User permissions = "admin":
        try:
          await newchannel.edit(position=channel.position)
    await channel.delete()
    embed = discord.Embed(

        title = 'nuke go brr',
        description = '',
        color = discord.Color.blue( )
    )
    embed.set_footer(text='DortBot')
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Seal_of_the_Federal_Bureau_of_Investigation.svg/1200px-Seal_of_the_Federal_Bureau_of_Investigation.svg.png')
    embed.set_author(name='NUKED CHANNEL',
    icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Seal_of_the_Federal_Bureau_of_Investigation.svg/1200px-Seal_of_the_Federal_Bureau_of_Investigation.svg.png')

    await newchannel.send(embed=embed, delete_after=10)
        except Exception as e:
          ee = "Error: " + e
          await ctx.send_message(content=ee)
    
    

if __name__ == "__main__":
    bot.run(TOKEN)
