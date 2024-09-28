import discord
from arrays import burns, hug_links, cat_pics, spells
from discord.ext import commands
from urllib.request import urlopen
import youtube_dl
import os
import requests
import bs4
import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy

# Load the language model
nlp = spacy.load('en_core_web_sm')

# Initialize the ChatBot
cb = ChatBot("bot")
trainer = ChatterBotCorpusTrainer(cb)
trainer.train("chatterbot.corpus.english")

# Set up the bot
client = commands.Bot(command_prefix='!')
players = {}
amount_del = 0
rand = 0
chat_bot_on = True

@client.event
async def on_ready():
    """Bot startup message."""
    print("CORTANA ACTIVATED")
    channel = client.get_channel(784519871857033239)  # Replace with your channel ID
    await channel.send("CORTANA ACTIVATED")

@client.event
async def on_message(message):
    """Processes messages sent in the channel."""
    message_content = message.content.strip().lower()

    # Allow data display command
    if "data" in message_content and "show" in message_content:
        await message.channel.send(message)

    # Admin command to quit the bot
    if "you" in message_content and "quit" in message_content:
        if message.author.name == '#ENTER ADMIN NAME':  # Replace with the admin's name
            await message.channel.send("It has been a great time helping you, Bye!")
            quit()
        else:
            await message.channel.send("Sorry, you don't have the permissions to give me that command.")

    await client.process_commands(message)

@client.command()
async def commands(ctx):
    """Displays the list of commands."""
    await ctx.send(
        f'```ini\n[Commands:]\n[!speed]\n[!time]\n[!date]\n[!ping @username]\n[!spam num]\n[!clear num]\n[!kick @username]\n[!ban @username]\n[!web_scrape URL]\n[!play YT.URL]\n[!leave]\n[!pause]\n[!resume]\n[!stop]\n[!weather]\n[!calc equation]\n[!speech]\n[!game]```'
    )

@client.command()
async def ping(ctx, *, member: discord.Member):
    """Pings a specified member a number of times."""
    await ctx.send("How many times do you want to ping?")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    ping_msg_num = int(msg.content)

    for _ in range(ping_msg_num):
        await ctx.send(f'{member.mention}')

@client.command()
async def spam(ctx, *, num):
    """Spams a specified message a number of times."""
    try:
        await ctx.send("What do you want to spam?")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await client.wait_for("message", check=check)

        for _ in range(int(num)):
            await ctx.send(f'{msg.content}')
    except ValueError:
        await ctx.send("Invalid number provided.")

@client.command()
async def clear(ctx, *, amount):
    """Clears a specified number of messages."""
    try:
        await ctx.channel.purge(limit=int(amount) + 1)
    except ValueError:
        await ctx.send("Invalid amount provided.")

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    """Kicks a specified member from the server."""
    try:
        await member.kick(reason=reason or "No reason provided")
        await ctx.send(f'{member.mention} was kicked.')
    except discord.Forbidden:
        await ctx.send("I don't have permission to kick that member.")

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    """Bans a specified member from the server."""
    try:
        await member.ban(reason=reason or "No reason provided")
        await ctx.send(f'{member.mention} was banned.')
    except discord.Forbidden:
        await ctx.send("I don't have permission to ban that member.")

@client.command()
async def time(ctx):
    """Displays the current time."""
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'```diff\n+The time is: {current_time}.```')

@client.command()
async def date(ctx):
    """Displays the current date."""
    from datetime import date
    today = date.today()
    await ctx.send(f'```diff\n+Current date is: {today}.```')

@client.command()
async def web_scrape(ctx, *, url):
    """Scrapes a webpage and sends the HTML."""
    try:
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        with open("html.txt", "w", encoding="utf-8") as file:
            file.write(html)

        await ctx.send(file=discord.File("html.txt"))
        await ctx.send('Code has been sent...')
        os.remove("html.txt")
    except Exception as e:
        await ctx.send("Invalid URL...")

@client.command()
async def play(ctx, url: str):
    """Plays a song from a YouTube URL."""
    song_there = os.path.isfile("song.mp3")
    if song_there:
        os.remove("song.mp3")

    voice_channel = discord.utils.get(ctx.guild.voice_channels, name='General')  # Replace with your channel name
    await voice_channel.connect()
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
    """Disconnects the bot from the voice channel."""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@client.command()
async def pause(ctx):
    """Pauses the currently playing audio."""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@client.command()
async def resume(ctx):
    """Resumes the paused audio."""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

@client.command()
async def stop(ctx):
    """Stops the currently playing audio."""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command()
async def weather(ctx):
    """Fetches and displays weather information."""
    try:
        res = requests.get('#ENTER WEATHER CHANNEL LINK')  # Replace with the actual weather URL
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        temp = soup.select_one('.CurrentConditions--tempValue--3KcTQ')

        if temp:
            await ctx.send(f'*The weather in #LOCATION is: {temp.text}.*')  # Replace #LOCATION with actual location
        else:
            await ctx.send("Could not retrieve weather information.")
    except Exception as e:
        await ctx.send("An error occurred while fetching weather information.")

@client.command()
async def calc(ctx, *, equat):
    """Calculates a mathematical expression."""
    try:
        calculation = eval(equat)
        await ctx.send(f'```{calculation}```')
    except Exception as e:
        await ctx.send("Invalid Equation.")

@client.command()
async def speed(ctx):
    """Displays the bot's latency."""
    embed = discord.Embed(
        title=f'Pong! `{round(client.latency * 1000)} ms`',
        colour=discord.Colour.purple())
    await ctx.send(embed=embed)

@client.command()
async def speech(ctx):
    """Engages in conversation with the user."""
    chat_bot_on = True
    while chat_bot_on:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await client.wait_for("message", check=check, timeout=30)
        inp = msg.content

        await ctx.send(cb.get_response(inp))

        # Check for goodbye phrases to end the conversation
        if any(x in inp for x in ["goodbye", "bye", "see you"]):  # Adjust goodbye phrases as needed
            await ctx.send(f'Goodbye, {msg.author}!')
            chat_bot_on = False

@client.command()
async def game(ctx):
    """Starts a game with spell casting mechanics."""
    # Define spells (Add your Spell class here)
    fire = Spell("fire", 10, 110, "black")
    thunder = Spell("thunder", 15, 160, "black")
    blizzard = Spell("blizzard", 8, 75, "black")
    meteor = Spell("meteor", 20, 205, "black")
    quake = Spell("quake", 14, 132, "black")
    gravity = Spell("gravity", 35, 340, "black")
    balance = Spell("balance", 40, 0, "special")
    trade = Spell("trade", 0, 0, "special")
    cure = Spell("cure", 12, 120, "white")
    cura = Spell("cura", 18, 200, "white")

    running = True
    await ctx.send("Choose difficulty: easy - 1, medium - 2, hard - 3")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check, timeout=120)
    level = int(msg.content)

    # Player and enemy initialization based on difficulty
    if level == 1:
        player = Person(550, 65, 55, 40, [fire, thunder, blizzard, meteor, quake, gravity, balance, trade, cure, cura])
        enemy = Person(1000, 65, 65, 45, [])
    elif level == 2:
        player = Person(500, 50, 60, 30, [fire, thunder, blizzard, meteor, quake, gravity, balance, trade, cure, cura])
        enemy = Person(1100, 70, 70, 65, [])
    elif level == 3:
        player = Person(450, 35, 50, 10, [fire, thunder, blizzard, meteor, quake, gravity, balance, trade, cure, cura])
        enemy = Person(1300, 100, 90, 70, [])

    while running:
        await ctx.send("Choose Action: 1: Attack, 2: Magic")
        
        msg = await client.wait_for("message", check=check, timeout=120)
        choice = int(msg.content)

        if choice == 1:
            dmg = player.gen_damage()
            enemy.take_dmg(dmg)
            await ctx.send(f"You attacked for {dmg} damage. Enemy HP: {enemy.get_hp()}")
        elif choice == 2:
            await player.choose_magic(ctx)
            await ctx.send("Choose Magic:")
            msg = await client.wait_for("message", check=check, timeout=120)
            magic_choice = int(msg.content) - 1
            # Handle magic selection...

        if enemy.get_hp() <= 0:
            await ctx.send("You defeated the enemy!")
            running = False
        elif player.get_hp() <= 0:
            await ctx.send("You were defeated!")
            running = False

# Run the bot with the specified token
client.run('#ENTER DISCORD API HERE')  # Replace with your bot token
