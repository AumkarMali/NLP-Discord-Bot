import discord
from arrays import burns
from arrays import hug_links
from arrays import no
from arrays import topics
from arrays import questions
import random
from arrays import moods
from arrays import cat_pics
from arrays import not_here
from arrays import compliments
from arrays import compliment_back
from arrays import en, fr, span, brit, amer, canto, mand, kor, jap, anime
from discord.ext import commands
from urllib.request import urlopen
import youtube_dl
import os
import requests
import bs4
import random
from chatterbot import ChatBot
import en_core_web_sm
nlp = en_core_web_sm.load()

cb = ChatBot("bot")

client = commands.Bot(command_prefix='!')
anime_database = {}
players = {}
amount_del = 0
rand = 0
chat_bot_on = True

goodbye = ['bye', 'cya', 'later']
nickname = "Master"


@client.event
async def on_ready():
    print("CORTANA ACTIVATED")
    channel = client.get_channel(784519871857033239)
    await channel.send("CORTANA ACTIVATED")


@client.event
async def on_message(message):
    message_content = message.content.strip().lower()

    if "can" in message_content:
        if "cheer" in message_content and "me" in message_content:
            rand_cat_pic = random.choice(cat_pics)
            await message.channel.send(rand_cat_pic)

        if "data" in message_content and "show" in message_content:
            await message.channel.send(message)

        if "you" in message_content and "sing" in message_content:
            count = 101
            for x in range(100):
                count = count - 1
                await message.channel.send(f'{count} bottles of beer on the wall,')
                await message.channel.send(f'{count} bottles of beer!')
                await message.channel.send(f'Take on down,\nPass it around,')
                await message.channel.send(
                    f'{count} bottles of beer on the wall!\n```------------------------------------------------------------------```')

            await message.channel.send("No more bottles of beer on the wall!")

        if "you" in message_content and "quit" in message_content:
            if message.author.name == 'I_BLOW_STUFF_UP':
                await message.channel.send("It has been a great time helping you, Bye!")
                quit()
            else:
                await message.channel.send("Sorry, you don't have the permissions to give me that command.")

    client.process_commands(message)

@client.command()
async def commands(ctx):
    await ctx.send(
      f'```ini\n[Commands:]\n[!speed]\n[!time]\n[!date]\n[!ping @username]\n[!spam num]\n[!clear num]\n[!kick @username]\n[!ban @username]\n[!roast @username]\n[!hug @username]\n[!web_scrape URL]\n[!play YT.URL]\n[!leave]\n[!pause]\n[!resume]\n[!stop]\n[!weather]\n[!calc equation]\n[!speech]```')


@client.command()
async def ping(ctx, *, member: discord.Member):
    await ctx.send(f"How many times do you want to ping")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    ping_msg_num = int(msg.content)

    for j in range(ping_msg_num):
        await ctx.send(f'{member.mention}')


@client.command()
async def spam(ctx, *, num):
    await ctx.send(f"What do you want to spam?")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)

    for i in range(int(num)):
        await ctx.send(f'{msg.content}')


@client.command()
async def clear(ctx, *, amount):
    await ctx.channel.purge(limit=int(amount) + 1)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason="Just for kicks")
    await ctx.send(f'{member.mention} was kicked.')


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason="idek")
    await ctx.send(f'{member.mention} was banned.')


@client.command()
async def time(ctx):
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'```diff\n+The time is: {current_time}.```')


@client.command()
async def date(ctx):
    from datetime import date
    today = date.today()
    await ctx.send(f'```diff\n+Current date is: {today}.```')


@client.command()
async def roast(message, member: discord.Member):
    rand_roast = random.choice(burns)
    await message.channel.send(f'{member.mention}, {rand_roast} :joy:')


@client.command()
async def hug(ctx, member: discord.Member):
    rand_hugs = random.choice(hug_links)
    await ctx.send(f'{rand_hugs}')
    await ctx.send(f'{member.mention} gets a hug.')


@client.command()
async def web_scrape(ctx, *, url):
    try:
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        with open("html.txt", "w", encoding="utf-8") as file:
            file.write(html)

        await ctx.send(file=discord.File("html.txt"))
        await ctx.send('Code has been sent...')
        os.remove("html.txt")

    except:
        await ctx.send("Invalid URL...")


@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")

    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the '!stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def weather(ctx):
    res = requests.get('https://weather.com/weather/today/l/43.59,-79.64?par=google&temp=c')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    soup.select('.CurrentConditions--tempValue--3KcTQ')

    for i in soup.select('.CurrentConditions--tempValue--3KcTQ'):
        await ctx.send(f'*The weather in mississauga is: {i.text}.*')


@client.command()
async def calc(ctx, *, equat):
    try:
        calculation = eval(equat)
        await ctx.send(f'```{calculation}```')
    except:
        await ctx.send("Invalid Equation.")


@client.command()
async def speed(ctx):
    embed = discord.Embed(
        title=f'Pong! `{round(client.latency * 1000)} ms`',
        colour=discord.Colour.purple())
    await ctx.send(embed=embed)


@client.command()
async def speech(ctx):
  chat_bot_on = True
  while chat_bot_on:
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    inp = msg.content

    if "cortana" in inp:
      inp = inp.replace("cortana", "")

    await ctx.send(cb.get_response(inp))

    for x in goodbye:
      if x in inp:
        await ctx.send(f'{random.choice(goodbye)}, {msg.author}')
        chat_bot_on = False
        return None


client.run('NzkyNDI2NDM4NjQwMTQwMzE4.X-dioQ.uB86HSfV1n-Ldx0sMHesY9roKL4')