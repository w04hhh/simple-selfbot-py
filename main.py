version = 0.69
dev = "michi.exe (cum master)"

import discord
import json
import os

import requests

from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)
token = config.get("Token")
prefix = config.get("Prefix")

client = commands.Bot(self_bot=True, command_prefix=prefix, case_insensitive=True,)
client.remove_command("help")

@client.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Michi SelfBot | {version} | Logged Into: {client.user} | Prefix: {prefix}")
    print(f"Michi-SelfBot {version}\nLogged Into: {client.user} - ID: {client.user.id}", 1)
    print(f"--------------------------------------------------")


# COPY THE CODE BELOW & CHANGE "LTC" to whatever you want as cmd + Change the text below which should get sent.
	
@client.command()
async def ltc(ctx):
    await ctx.message.delete()
    await ctx.send(f"YOUR LTC ADDY")
    

try:
    client.run(token)
except discord.errors.LoginFailure:
    print(f"NVALID TOKEN, uwu")
    os.system('pause >NUL')

# .gg/michitools 