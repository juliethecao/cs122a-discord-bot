# CS122A Server Discord Bot
### Languages and Tools

<p>
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" style="padding:5px"/>
  <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" style="padding:5px"/>
  <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" style="padding:5px"/>
  <img src="https://img.shields.io/badge/Ed Discussion-654B9C?style=for-the-badge&logoColor=white" style="padding:5px">
</p>

## Description
- Build a bot using the Discrd API to help manage a class server from Discord
- Use Ed Discussion API to retrieve information from user queries for the bot

## How to Use

#### Installation and SetUp:
`pip install -r requirements.txt`

Create a `.env` file using `.env-template` as a guide for required tokens/information.

Obtain [Ed Discussion Token and Course ID](https://edstem.org/us/) and create a [discord bot and token](https://discord.com/developers/docs/getting-started). Accounts are needed for both platforms.

#### User Instructions
Type `!` to get a specific command in the following options via Discord:

`!help`
Displays all the commands below
            
`!announcement`
Retrieves any posted announcements
            
`!post`
Retrieves posts
            
`!question`
Retrieves questions asked
            
`!recent`
Retrieves the 5 recent posts

Each command can be optionally filtered by a category and subcategory to filter results in the following format:
            
`!<command> <category> <subcategory>`

Commands: announcement, post, question, recent
Category: general, assignments, lectures, discussion-hours, social
Subcategory: (this is for assignments) A1, A2, A3, A4, A5, A6

## Preview
Below is an image when you call the bot. If the `!help` is called, the bot will showcase the commands that you can use.

<img width="537" alt="Screenshot 2023-10-05 at 9 00 41 PM" src="https://github.com/juliethecao/cs122a-discord-bot/assets/116243642/5bce5a51-c38a-4ef5-809f-4fd27078298b">

You will receive the posts privately via your direct messages. 
<p><img width="69" alt="Screenshot 2023-10-05 at 9 01 01 PM" src="https://github.com/juliethecao/cs122a-discord-bot/assets/116243642/e8942ef0-4cc0-44c8-b2e6-34950f782606"></p>

Here is how the messages will appear through your direct messages.
<img width="1097" alt="Screenshot 2023-10-05 at 9 01 28 PM" src="https://github.com/juliethecao/cs122a-discord-bot/assets/116243642/8d98a49e-3ea6-4cf8-9247-c195818cce95">

Credit: Discord profile picture by Mimu Bot.
