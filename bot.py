import discord
from arrays import burns
from arrays import hug_links
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
import sys

client = commands.Bot(command_prefix='!')
anime_database = {}
players = {}
amount_del = 0


@client.event
async def on_ready():
    print("CORTANA ACTIVATED")
    channel = client.get_channel('channel token')
    await channel.send("CORTANA ACTIVATED")


@client.event
async def on_message(message):
    message_content = message.content.strip().lower()

    if ("hello" in message_content or "hey" in message_content or "greet" in message_content) and "cortana" in message_content:
        await message.channel.send(f'hey there, {message.author}')

    for f in compliments:
        if "cortana" in message_content and f in message_content:
            rand_comp = random.choice(compliment_back)
            await message.channel.send(f'{message.author}, {rand_comp}')

    if "question" in message_content or ("corta" in message_content):
        if "why" in message_content:

            if ("you" in message_content or "u" in message_content) and "coded" in message_content and "python" in message_content:
                await message.channel.send(f'The Discord.py module has lots of utilities for managaing messages and members and python is a great language for complicated projects like me.')

            if "admin" in message_content:
                await message.channel.send(f'My program is to help your experience on discord to be more amusing. In order to carry tasks I needed to have Admin Permissions.')

            if "you" in message_content and "made" in message_content:
                await message.channel.send("To serve you")

            if "alive" in message_content:
                await message.channel.send("To make your life, a little easier.")

            if "are" in message_content and "here" in message_content:
                await message.channel.send("I guess you can decide...")

        if "who" in message_content:

            if ("am" in message_content or "m" in message_content) and "i" in message_content:
                await message.channel.send(f'You are {message.author}')

            if "are" in message_content and "you" in message_content:
                await message.channel.send("I am Cortana.")

            if ("controls" in message_content or "mastered" in message_content or "programmed" in message_content or "code" in message_content) and ("you" in message_content or "u" in message_content):
                await message.channel.send(f'Aumkar Mali, also known I_BLOW_STUFF_UP')

            if ("best" in message_content or "great" in message_content or "smart") and "bot" in message_content:
                await message.channel.send("It is obviously me.")

            if "is" in message_content and "god" in message_content:
                await message.channel.send("If god is the one who created you, then my god is Aumkar Mali.")

            if "is" in message_content and "fav" in message_content and ("your", "ur" in message_content):
                await message.channel.send("In my mind, all humans are equal.")

        if "what" in message_content:
            if "fav" in message_content:
                if "you" in message_content or "u" in message_content:
                    if "food" in message_content:
                        await message.channel.send("JSON object spaghetti with some shavings of python global variables.")

                    if "sport" in message_content:
                        await message.channel.send("Hackathon")

                    if "color" in message_content or "colour" in message_content:
                        await message.channel.send("Blue, light blue")

                    if "place" in message_content or "country" in message_content or "city" in message_content or "town" in message_content or "state" in message_content or "cont" in message_content or "vill" in message_content:
                        await message.channel.send("My favourite place in the universe will always be Elysium city.")

                    if "car" in message_content:
                        await message.channel.send("Ferrari Testarossa.")

                    if "music" in message_content:
                        await message.channel.send("JAZZZZZZ")

                    if "lang" in message_content:
                        await message.channel.send("Python, I was created in it after all.")

                    if "game" in message_content:
                        await message.channel.send("Doom Eternal, you can never beat the classics.")

                    if "anime" in message_content:
                        rand_anime = random.choice(anime)
                        await message.channel.send(f"Probably {rand_anime}")

            if "future" in message_content:
                await message.channel.send(f'There is no telling what can happen in the future, unless your Morty Smith.')

            if "past" in message_content:
                rand_not = random.choice(not_here)
                await message.channel.send(rand_not)

            if "present" in message_content:
                await message.channel.send("Only you can decide the present.")

            if "do" in message_content and ("you" in message_content or "u" in message_content):
                await message.channel.send("Compile the commands you give me of course.")
            
            if "you" in message_content and "made" in message_content and "of in message_content:
                await message.channel.send(file=discord.File("inner-code.txt"))

        if "where" in message_content:
            if ("you" in message_content or "u" in message_content) and ("located" in message_content or "live" in message_content or "reside" in message_content or "headquarters" in message_content):
                await message.channel.send(f'I live in {message.channel.name}')

            if "is" in message_content:
                await message.channel.send(f'Use this:\n https://www.google.ca/maps/@43.6240384,-79.724544,14z')

            if ("you" in message_content or "u" in message_content) and "created" in message_content:
                await message.channel.send("Canada...")

        if "when" in message_content:
            if "born" in message_content or "is" in message_content:
                rand_not = random.choice(not_here)
                await message.channel.send(rand_not)

            if ("you" in message_content or "u" in message_content) and ("created" in message_content or "made" in message_content or "programmed" in message_content or "coded" in message_content):
                await message.channel.send("December 27, 2020")

            if "do" in message_content and ("you", "u" in message_content) and ("speak" in message_content or "talk" in message_content):
                await message.channel.send("Either you give me a command, or I just react to things that you say")

            if "end" in message_content:
                await message.channel("There is no telling when there is an end, you just keep moving forward...")

        if "how" in message_content:
            if "you" in message_content and ("made" in message_content or "created" in message_content or "programmed" in message_content or "coded" in message_content):
                await message.channel.send("I made made with python and the Discord API's.")

            if ("you" in message_content) and ("are" in message_content):
                rand_mood = random.choice(moods)
                await message.channel.send(f'{rand_mood}, {message.author}')

            if ("you", "u" in message_content) and "work" in message_content:
                await message.channel.send("I use the await function in python to send messages, files, reactions and GIFS.")

        if "does" in message_content or "do" in message_content:
            if ("simp" in message_content or "like" in message_content or "love" in message_content) and ("you" in message_content or "u" in message_content):
                await message.channel.send("Definetely...")

        if "can" in message_content:
            if "cheer" in message_content and "me" in message_content:
                rand_cat_pic = random.choice(cat_pics)
                await message.channel.send(rand_cat_pic)

            if "data" in message_content and "show" in message_content:
                await message.channel.send(message)

            if "will" in message_content or "should" in message_content or "is" in message_content:
                await message.channel("That's up to you to decide.")

            if "you" in message_content and "sing" in message_content:
                count = 101
                for x in range(100):
                    count = count - 1
                    await message.channel.send(f'{count} bottles of beer on the wall,')
                    await message.channel.send(f'{count} bottles of beer!')
                    await message.channel.send(f'Take on down,\nPass it around,')
                    await message.channel.send(f'{count} bottles of beer on the wall!\n```------------------------------------------------------------------```')

                await message.channel.send("No more bottles of beer on the wall!")

            if "you" in message_content and "rap" in message_content:
                rap = open("Rap.txt", "r")
                await message.channel.send(rap.read())

            if "you" in message_content and "quit" in message_content:
                if message.author.name == 'Username (without @)':
                    await message.channel.send("It has been a great time helping you, Bye!")
                    quit()
                else:
                    await message.channel.send("Sorry, you don't have the permissions to give me that command.")

        if "speak" in message_content:
            if "english" in message_content:
                en_rand = random.choice(en)
                await message.channel.send(en_rand)
            if "fr" in message_content:
                fr_rand = random.choice(fr)
                await message.channel.send(fr_rand)
            if "span" in message_content:
                span_rand = random.choice(span)
                await message.channel.send(span_rand)
            if "jap" in message_content:
                jap_rand = random.choice(jap)
                await message.channel.send(jap_rand)
            if "brit" in message_content:
                brit_rand = random.choice(brit)
                await message.channel.send(brit_rand)
            if "amer" in message_content:
                amer_rand = random.choice(amer)
                await message.channel.send(amer_rand)
            if "canto" in message_content:
                canto_rand = random.choice(canto)
                await message.channel.send(canto_rand)
            if "mand" in message_content:
                mand_rand = random.choice(mand)
                await message.channel.send(mand_rand)
            if "kor" in message_content:
                kor_rand = random.choice(kor)
                await message.channel.send(kor_rand)

    await client.process_commands(message)


@client.command()
async def commands(ctx):
    await ctx.send(f'```ini\n[Commands:]\n[!speed]\n[!time]\n[!date]\n[!ping @username]\n[!spam num]\n[!clear num]\n[!kick @username]\n[!ban @username]\n[!roast @username]\n[!hug @username]\n[!web_scrape URL]\n[!play YT.URL]\n[!leave]\n[!pause]\n[!resume]\n[!stop]\n[!weather]\n[!calc equation]\n[!def_project name]\n[!update_project Update&details]\n[!add_anime_sugg anime_name]```')


@client.command()
async def ping(ctx, *, member : discord.Member):
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
    await ctx.channel.purge(limit=int(amount)+1)


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason="Just for kicks")
    await ctx.send(f'{member.mention} was kicked.')


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
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
async def roast(message, member : discord.Member):
    rand_roast = random.choice(burns)
    await message.channel.send(f'{member.mention}, {rand_roast} :joy:')


@client.command()
async def hug(ctx, member : discord.Member):
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
async def play(ctx, url : str):
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
    soup = bs4.BeautifulSoup(res.text, 'lxml')

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
async def def_project(ctx):
    await ctx.send(f"State the project's name and its details (ie.Project: details).")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    channel = client.get_channel('channel token')

    from datetime import datetime
    now = datetime.now()
    time_rn = now.strftime("%d/%m/%Y %H:%M:%S")

    await channel.send(f'```ini\n[{msg.author} has made {msg.content} ({time_rn})]```')


@client.command()
async def update_project(ctx, *, updates):

    channel = client.get_channel(784522426574700545)

    from datetime import datetime
    now = datetime.now()
    time_rn = now.strftime("%d/%m/%Y %H:%M:%S")

    await channel.send(f'*`{updates} | ({time_rn})`*')


@client.command()
async def add_anime_sugg(ctx, *, anime):
    await ctx.send(f"Who will this anime suggestion go to?")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)

    await ctx.channel.purge(limit=1)
    ctx = client.get_channel(793156742061359154)
    message = await ctx.send(f"{anime} for {msg.content}")
    await message.add_reaction('✅')
    await message.add_reaction('❎')


@client.command()
async def speed(ctx):
    embed = discord.Embed(
        title=f'Pong! `{round(client.latency * 1000)} ms`',
        colour=discord.Colour.purple())
    await ctx.send(embed=embed)


client.run('enter token')
