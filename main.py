import os
import discord
import openai
from keep_alive import keep_alive

client = discord.Client()

#WORKING CODE

def gpt3(text):
  openai.api_key = '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'
  response = openai.Completion.create(
    engine="curie",
    prompt=text,
    temperature=0,
    max_tokens=100,
    top_p=1,  
    frequency_penalty=0,
    presence_penalty=0,
  )
  return((response.choices[0].text))
"""
#TEST FOR MORE CLEAN ANSWER
start_sequence = "\nA:"
restart_sequence = "\n\n"

def gpt3(text):
  openai.api_key = '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'
  response = openai.Completion.create(
    engine="curie",
    prompt=(text + "\n\n"),
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
  )
#END TEST FOR MORE CLEAN ANSWER
"""
@client.event
async def on_ready():
  print(f"{client.user} logged in now!")

@client.event
async def on_message(message):
  if message.content.startswith("$oceanfact "):
    text = message.content
    await message.channel.send(gpt3(text[11:]))


keep_alive()

my_secret = os.environ['token']
client.run(my_secret)
