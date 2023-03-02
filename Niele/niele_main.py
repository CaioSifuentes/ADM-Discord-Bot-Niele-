import discord
from discord.ext.commands import Bot
import json
import os

with open('config.json') as t:
    configData = json.load(t)

niele_client = Bot(command_prefix=">>", intents=discord.Intents.all())

for filename in os.listdir("./functions"):
    if filename.endswith(".py") and not filename.startswith("__"):
        niele_client.load_extension(f"functions.{filename[:-3]}")


# Avisa se o Bot está Online.
@niele_client.event
async def on_ready():
    print('\033[33m=' * 15)
    print(f'\033[35m{"Niele chegou!":^15}')
    print('\033[33m=\033[m' * 15)

    # Escreva abaixo o ID do canal de denúncias.
    report_channel = niele_client.get_channel(1017613515156111390)
    if report_channel is None:
        print("Status: \033[31mCanal de denúncias: NOT FOUND")
    else:
        print("Status: \033[32mCanal de denúncias: OK")

niele_client.run(configData["TOKEN"])
