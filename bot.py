import discord

# initiate discord
# building connection to discord
client = discord.Client()

# we have to do something before bot does something
# bot works on events
@client.event

# this bot is going to be using asynchronous programming 
# in discord channel if the message is been sent then this event will be detected by our bot and perform some action
async def on_message(message): 
    # if the message is sent from client i.e, bot
    if message.author == client.user:
        return
    # in your discord channel when bot is turned on and user types in hello then bot will respond
    if message.content.startswith('hello'):
        await message.channel.send('hello, I am bot')

    client.run('need token')
