import discord
import os
import youtube_dl
from discord.ext import commands

@client.event
async def on_ready():
    print("Bot online.")

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    if channel is None:
        await client.say(":exclamation: | **You need to join a voice channel!**")
        return
    await client.join_voice_channel(channel)
    await client.say(f"**I have joined {channel}** <:music:503713910763814912>")

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    if voice_client is None:
        await client.say(":exclamation: | **I am not in a voice channel!**")
        return
    await voice_client.disconnect()
    await client.say(f"**I have left** <:music:503713910763814912>")
    
client.run(os.environ.get('BOT_TOKEN'))
