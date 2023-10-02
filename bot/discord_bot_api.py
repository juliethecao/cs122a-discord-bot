import discord
import os
from ed import getThreadsByFilter
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
course_id = os.getenv("COURSE_ID")
token = os.getenv("ED_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

ed_types = ["post", "announcement", "question"]
categories = ["General", "Assignments", "Lectures", "Discussion" "Hours", "Social"]
subcategories = ["A1", "A2", "A3", "A4", "A5", "A6"]

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        #whatever yall want
        await message.channel.send('Hello!')
    
    # this will call recent 5 posts (anything)
    if message.content.startswith('!recent'):
        resps = getThreadsByFilter(token, course_id, pinned=False)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            await message.channel.send(output)
    
    if message.content.startswith('!announcement'):
        arguments = message.content.split(" ")
        category = ""
        subcategory = ""
        if len(arguments) > 1 and arguments[1] in categories:
            category = arguments[1]
        if len(arguments) > 2 and arguments[2] in subcategories:
            subcategory = arguments[2]
        resps = getThreadsByFilter(token, course_id, pinned=True, type=arguments[0][1:] , category=category, subcategory=subcategory)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            await message.channel.send(output)
    
    if message.content.startswith('!post'):
        arguments = message.content.split(" ")
        category = ""
        subcategory = ""
        if len(arguments) > 1 and arguments[1] in categories:
            category = arguments[1]
        if len(arguments) > 2 and arguments[2] in subcategories:
            subcategory = arguments[2]
        resps = getThreadsByFilter(token, course_id, pinned=False, type=arguments[0][1:] , category=category, subcategory=subcategory)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            await message.channel.send(output)
    
    if message.content.startswith('!question'):
        arguments = message.content.split(" ")
        category = ""
        subcategory = ""
        if len(arguments) > 1 and arguments[1] in categories:
            category = arguments[1]
        if len(arguments) > 2 and arguments[2] in subcategories:
            subcategory = arguments[2]
        resps = getThreadsByFilter(token, course_id, pinned=False, type=arguments[0][1:] , category=category, subcategory=subcategory)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            await message.channel.send(output)

client.run(discord_token)
