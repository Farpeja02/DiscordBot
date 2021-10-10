
import time
from discord.ext import commands
import music
import testCog
import discord

cogs = [music,testCog]
intents = discord.Intents().all()
client = commands.Bot(command_prefix='?',intents = intents)
americaList = []
europeList = []
token = 'Token'

client.load_extension('testCog')


@client.event
async def on_ready():
    channel = client.get_channel(620487227646148618)
    #await channel.send('The leaderboard has been reset! go poop!')
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'[{username}: {user_message} ({channel})')

    if message.author == client.users:
        return
    if user_message.lower() == 'i pooped':
        msg = await message.channel.send(f'yaaayyy, please rate your poop!')
        print("test")
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")

    if user_message.lower() == 'when is halloween':
        currentTime = int(time.time())
        HaloweenTime = 1635634800
        timeUntilDays = (HaloweenTime - currentTime) / 60 / 60 / 24
        timeUntilHours = (HaloweenTime - currentTime) / 60 / 60
        timeUntilMinutes = (HaloweenTime - currentTime) / 60
        await message.channel.send(f'There are {int(timeUntilDays)} days or {int(timeUntilHours)} Hours or {int(timeUntilMinutes)} or Minutes, till Halloween! :smiley: ')
        return


    if user_message.lower() == 'leaderboard':
        if len(europeList) > 0 and len(americaList) > 0:
            fullEuNumber = 0
            fullUSANumber = 0
            for item in europeList:
                fullEuNumber += item
            for item in americaList:
                fullUSANumber += item
            avgNumEU = fullEuNumber / len(europeList)
            avgNumUSA = fullUSANumber / len(americaList)
            await message.channel.send(f'The average score of Europe is: {avgNumEU:.2f}, And the average score of North America is: {avgNumUSA:.2f}')
            print(europeList)
            print(americaList)
        else:
            await message.channel.send(f'One of the continents, havent pooped, please wait for them to poop!')





@client.event
async def on_reaction_add(reaction,user):
    currentEmoji = 0
    if reaction.emoji == "1️⃣":
        currentEmoji = 1
        print("1")
    if reaction.emoji == "2️⃣":
        currentEmoji = 2
        print("2")
    if reaction.emoji == "3️⃣":
        currentEmoji = 3
        print("3")
    if reaction.emoji == "4️⃣":
        currentEmoji = 4
        print("4")
    if reaction.emoji == "5️⃣":
        currentEmoji = 5
        print("5")

    europeRole = discord.utils.get(user.roles, name="europe")
    americaRole = discord.utils.get(user.roles, name="north america")
    if americaRole in user.roles:
        if currentEmoji > 0:
            print("america role" + str(currentEmoji))
            americaList.append(currentEmoji)
    if europeRole in user.roles:
        if currentEmoji > 0:
            europeList.append(currentEmoji)
            print("europe role" + str(currentEmoji))
    print(str(currentEmoji)+ "Is it over 0?")


client.run(token)