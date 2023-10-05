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
categories = ["general", "assignment", "lectures", "discussion-hours", "social"]
subcategories = ["A1", "A2", "A3", "A4", "A5", "A6"]

client = discord.Client(intents=intents)
discord_channel_name = os.getenv("CHANNEL_NAME")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name != discord_channel_name:
        return

    if message.content.startswith('!help'):
        text = """Hello! I am Moochi, an Ed Discussion retrieving bot.\nType '!' to get a specific command in the following options:
            > !announcement\nRetrieves any posted announcements
            > !post\nRetrieves posts
            > !question\nRetrieves questions asked
            > !recent\nRetrieves the 5 recent posts\n\nEach command can be optionally filtered by a category \nand subcategory to filter results in the following format:
            > !<command> <category> <subcategory>\n\n**Commands:** announcement, post, question, recent\n**Category:** general, assignments, lectures, discussion-hours, social\n**Subcategory:** (this is for assignments) A1, A2, A3, A4, A5, A6
            """
        # await message.author.send(text)
        await message.channel.send(text)
    
    # this will call recent 5 posts (anything)
    if message.content.startswith('!recent'):
        arguments = message.content.lower().split(" ")
        category = ""
        subcategory = ""
        if len(arguments) > 1 and arguments[1] in categories:
            category = arguments[1].replace("-", " ").title()
        if len(arguments) > 2 and arguments[2] in subcategories:
            subcategory = arguments[2].upper()
        resps = getThreadsByFilter(token, course_id, pinned=False, category=category, subcategory=subcategory)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            # await message.channel.send(output)
            await message.author.send(output)
    
    if message.content.startswith('!announcement'):
        arguments = message.content.lower().split(" ")
        category = ""
        subcategory = ""
        if len(arguments) > 1 and arguments[1] in categories:
            category = arguments[1].replace("-", " ").title()
        if len(arguments) > 2 and arguments[2] in subcategories:
            subcategory = arguments[2].upper()
        resps = getThreadsByFilter(token, course_id, pinned=True, type=arguments[0][1:] , category=category, subcategory=subcategory)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            # await message.channel.send(output)
            await message.author.send(output)

    if message.content.startswith('!post'):
        arguments = message.content.lower().split(" ")
        category = ""
        subcategory = ""
        if len(arguments) > 1 and arguments[1] in categories:
            category = arguments[1].replace("-", " ").title()
        if len(arguments) > 2 and arguments[2] in subcategories:
            subcategory = arguments[2].upper()
        resps = getThreadsByFilter(token, course_id, pinned=False, type=arguments[0][1:] , category=category, subcategory=subcategory)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            # await message.channel.send(output)
            await message.author.send(output)

    if message.content.startswith('!question'):
        arguments = message.content.split(" ")
        category = ""
        subcategory = ""
        if len(arguments) > 1 and arguments[1] in categories:
            category = arguments[1].replace("-", " ").title()
        if len(arguments) > 2 and arguments[2] in subcategories:
            subcategory = arguments[2].upper()
        resps = getThreadsByFilter(token, course_id, answers=True, pinned=False, type=arguments[0][1:] , category=category, subcategory=subcategory)
        for resp in resps:
            output = f"\"{resp['title']}\" by {resp['name']}\n{resp['link']}\n{resp['content']}\n{resp['comments']}"
            await message.author.send(output)
            # await message.channel.send(output)

client.run(discord_token)
