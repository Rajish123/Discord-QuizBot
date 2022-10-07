import asyncio
import json
from urllib import request
import discord
import requests

def get_question():
    qs = ""
    id = 1
    answer= 0
    response = request.get("http://127.0.0.1:8000/api/random/")
    json_data = json.loads(response.text)
    qs = "Question: \n"
    qs += json_data[0]['title']+ "\n"
    for item in json_data[0]['answer']:
        qs += str(id) + "." + item['answer'] + "\n"
        if item['is_correct']:
            answer = id
        id += 1

    return(qs, answer)

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
    if message.content.startswith('$question'):
        qs, answer = get_question()
        await message.channel.send(qs)

        # checks for comments and whether user's input is digit
        def check(m):
            return m.author == message.author and m.content.isdigit()
            try:
                # creates websocket between user and server and waits for 5sec
                # check:checks if there is user input
                guess  = await client.wait_for('message', check = check, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(
                    'Sorry! Time Out.'
                )
            if int(guess.content) == answer:
                await message.channel.send("You are right")
            else:
                await message.channel.send("Opps!You are incorrect.")

    client.run('need token')
