import asyncio
import websockets
import json
import logging
import requests
import sys
import sqlite3
import re
import requests
import discord
from discord.ext import commands
from discord import Intents
from discord import app_commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
from discord.ui import Button, View
from discord import ButtonStyle
import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import telethon 
from telethon import TelegramClient, events
import time
import websockets
import json
from web3 import Web3
from solcx import compile_standard, install_solc
import requests
from typing import Optional
from discord import Embed
from discord.ui import Button, View
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import telethon 
from telethon import TelegramClient, events
import logging
import sys
import sqlite3
import re
from discord import Intents
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import asyncio
import websockets
import json
import aiohttp 
import logging
import requests
import sys
import discord
from discord.ext import commands
from discord import Intents
from discord import app_commands
import time
from discord.ui import Button, View
from discord import ButtonStyle
import discord
from discord.ext import commands
from discord import app_commands
import telethon 
from telethon import TelegramClient, events
from discord import Embed
from discord.ui import Button, View
from telethon import TelegramClient, events
from discord import Intents
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='.', intents=intents)

async def send_discord_message_friend(last_message):
    channel_id = #YOUR_CHANNEL_ID 
    channel = bot.get_channel(channel_id)
    print({last_message})
    full_message1 = f"{last_message}"
    await channel.send(full_message1)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await asyncio.gather(
        friend(),
    )
async def friend():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    #Bypass captcha with debbug session and prelog before start code 
    driver = webdriver.Chrome(options=chrome_options)

    time.sleep(5)

    last_message = None

    while True:
        try:
            message_div = driver.find_element(By.CSS_SELECTOR, 'div#other-message-text > div.Home_messageBubble__pkU0t')
            current_message = message_div.text
            if current_message != last_message:
                last_message = current_message
                await send_discord_message_friend(last_message)
            else:
                print("Message same.")
        except Exception as e:
            print(f"Error : {e}")

        await asyncio.sleep(1)

bot.run(YOUR_BOT_TOKEN)
 
