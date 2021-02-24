import discord
from arrays import burns
from arrays import hug_links
from arrays import cat_pics
from arrays import spells
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
nlp = spacy.load('en_core_web_sm')

cb = ChatBot("bot")
trainer = ChatterBotCorpusTrainer(cb)
trainer.train("chatterbot.corpus.english")

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

    await client.process_commands(message)

@client.command()
async def commands(ctx):
    await ctx.send(
      f'```ini\n[Commands:]\n[!speed]\n[!time]\n[!date]\n[!ping @username]\n[!spam num]\n[!clear num]\n[!kick @username]\n[!ban @username]\n[!roast @username]\n[!hug @username]\n[!web_scrape URL]\n[!play YT.URL]\n[!leave]\n[!pause]\n[!resume]\n[!stop]\n[!weather]\n[!calc equation]\n[!speech]\n[!game]```')


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
    try:
        await ctx.send(f"What do you want to spam?")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await client.wait_for("message", check=check)

        for i in range(int(num)):
            await ctx.send(f'{msg.content}')
    except:
        pass


@client.command()
async def clear(ctx, *, amount):
    try:
        await ctx.channel.purge(limit=int(amount) + 1)
    except:
        pass


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason="Just for kicks")
        await ctx.send(f'{member.mention} was kicked.')
    except:
        pass


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason="idek")
        await ctx.send(f'{member.mention} was banned.')
    except:
        pass


@client.command()
async def time(ctx):
    try:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await ctx.send(f'```diff\n+The time is: {current_time}.```')
    except:
        pass


@client.command()
async def date(ctx):
    try:
        from datetime import date
        today = date.today()
        await ctx.send(f'```diff\n+Current date is: {today}.```')
    except:
        pass

@client.command()
async def roast(message, member: discord.Member):
    try:
        rand_roast = random.choice(burns)
        await message.channel.send(f'{member.mention}, {rand_roast} :joy:')
    except:
        pass

@client.command()
async def hug(ctx, member: discord.Member):
    try:
        rand_hugs = random.choice(hug_links)
        await ctx.send(f'{rand_hugs}')
        await ctx.send(f'{member.mention} gets a hug.')
    except:
        pass


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
    try:
        res = requests.get('https://weather.com/weather/today/l/43.59,-79.64?par=google&temp=c')
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        soup.select('.CurrentConditions--tempValue--3KcTQ')

        for i in soup.select('.CurrentConditions--tempValue--3KcTQ'):
            await ctx.send(f'*The weather in mississauga is: {i.text}.*')
    except:
        pass


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

    msg = await client.wait_for("message", check=check, timeout=30)
    inp = msg.content

    if "cortana" in inp:
      inp = inp.replace("cortana", "")

    await ctx.send(cb.get_response(inp))

    for x in goodbye:
      if x in inp:
        await ctx.send(f'{random.choice(goodbye)}, {msg.author}')
        chat_bot_on = False
        return None

@client.command()
async def game(message):

    class Person:
        def __init__(self, hp, mp, atk, df, magic):
            self.maxhp = hp
            self.hp = hp
            self.maxmp = mp
            self.mp = mp
            self.atkl = atk - 10
            self.atkh = atk + 10
            self.df = df
            self.magic = magic
            self.action = ["attack", "magic"]

        def gen_damage(self):
            return random.randrange(self.atkl, self.atkh)

        def take_dmg(self, dmg):
            self.hp -= dmg
            if self.hp < 0:
                self.hp = 0
                return self.hp

        def heal(self, dmg):
            self.hp += dmg

        def get_hp(self):
            return self.hp

        def get_max_hp(self):
            return self.maxhp

        def get_mp(self):
            return self.mp

        def get_max_mp(self):
            return self.maxmp

        def reduce_mp(self, cost):
            self.mp -= cost

        async def choose_action(self):
            i = 1
            await message.channel.send("**Actions**")
            for item in self.actions:
                await message.channel.send(f'{str(i)}:, {item}')
                i += 1

        async def choose_magic(self):
            await message.channel.send('1: fire (Cost: 10, damage: 110)\n2: thunder (Cost: 15, damage: 160)\n3: blizzard (Cost: 8, damage: 75)\n4: meteor (Cost: 20, damage: 205)\n5: quake (Cost: 14, damage: 132)\n6: gravity (Cost: 35, damage: 340)\n7: balance (Cost: 40, Ability: enemies HP = Players HP, effectiveness varies)\n8: trade (Cost: 0, Ability: trade 80 HP for 30 MP)\n9: cure (Cost: 12, Heal: 120)\n10: cura (Cost: 18, Heal: 200)')

    class spell:
        def __init__(self, name, cost, dmg, type):
            self.name = name
            self.cost = cost
            self.dmg = dmg
            self.type = type

        def generate_dmg(self):
            low = self.dmg - 15
            high = self.dmg + 15
            return random.randrange(low, high)


    blizzard = spell("blizzard", 8, 75, "black")
    fire = spell("fire", 10, 110, "black")
    thunder = spell("thunder", 15, 160, "black")
    quake = spell("quake", 14, 132, "black")
    meteor = spell("meteor", 20, 205, "black")
    gravity = spell("gravity", 35, 340, "black")

    balance = spell("balance", 40, 0, "special")
    trade = spell("trade", 0, 0, "special")

    cure = spell("cure", 12, 120, "white")
    cura = spell("cura", 18, 200, "white")

    running = True
    i = 0

    await message.channel.send("```css\n[An enemy attacks !!!]```\nchoose difficulty: easy - 1, medium - 2, hard - 3")

    try:
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        msg = await client.wait_for("message", check=check, timeout=120)
        level = int(msg.content)
    except:
        await message.channel.send("Invalid input")
        await message.channel.send(
            "```css\n[An enemy attacks !!!]```\nchoose difficulty: easy - 1, medium - 2, hard - 3")

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        msg = await client.wait_for("message", check=check, timeout=120)
        level = int(msg.content)

    if level == 1:
        player = Person(550, 65, 55, 40, [fire, thunder, blizzard, meteor, quake, gravity, balance, trade, cure, cura])
        enemy = Person(1000, 65, 65, 45, [])

    if level == 2:
        player = Person(500, 50, 60, 30, [fire, thunder, blizzard, meteor, quake, gravity, balance, trade, cure, cura])
        enemy = Person(1100, 70, 70, 65, [])

    if level == 3:
        player = Person(450, 35, 50, 10, [fire, thunder, blizzard, meteor, quake, gravity, balance, trade, cure, cura])
        enemy = Person(1300, 100, 90, 70, [])

    while running:
        await message.channel.send("==============\n```diff\n-Actions```\n1: Attack\n2: Magic\nChoose Action:")

        try:
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            msg = await client.wait_for("message", check=check, timeout=120)
            pick = int(msg.content)
            index = int(pick) - 1
            enemy_choice = random.randint(1, 2)
            enemy_dmg = enemy.gen_damage()

        except:
            await message.channel.send("Invalid input")
            await message.channel.send("==============\n```diff\n-Actions```\n1: Attack\n2: Magic\nChoose Action:")

            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            msg = await client.wait_for("message", check=check, timeout=120)
            pick = int(msg.content)
            index = int(pick) - 1
            enemy_dmg = enemy.gen_damage()


        if index == 0:
            dmg = player.gen_damage()
            enemy.take_dmg(dmg)
            await message.channel.send(f"you attacked for {dmg} points of damage, Enemy HP: {enemy.get_hp()}")
            player.take_dmg(enemy_dmg)
            await message.channel.send(f"Enemy attacks for {enemy_dmg} points of damage, player hp: {player.get_hp()}")

        elif index == 1:
            await player.choose_magic()
            await message.channel.send("Choose Magic:")

            try:
                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel

                msg = await client.wait_for("message", check=check, timeout=120)
                magic_choice = int(msg.content) - 1

            except:
                await message.channel.send("Invalid input")
                await player.choose_magic()
                await message.channel.send("Choose Magic:")

                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel

                msg = await client.wait_for("message", check=check, timeout=120)
                magic_choice = int(msg.content) - 1


            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg()
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg()
            current_mp = player.get_mp()
            if int(spell.cost) > int(current_mp):
                await message.channel.send('Not Enough MP')
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                await message.channel.send(f"{spell.name} heals for {str(magic_dmg)} HP.")
                player.take_dmg(enemy_dmg)
                await message.channel.send(f"Enemy attacks for {enemy_dmg} points of damage, player hp: {player.get_hp()}")

            elif spell.type == "black":
                enemy.take_dmg(magic_dmg)
                await message.channel.send(f"{spell.name} deals, {str(magic_dmg)} points of damage")
                player.take_dmg(enemy_dmg)
                await message.channel.send(f"Enemy attacks for {enemy_dmg} points of damage, player hp: {player.get_hp()}")

            elif spell.name == "balance":
                enemy.hp = player.get_hp()
                player.hp = player.hp - random.randint(0, 15)
                effic = round((player.hp / enemy.hp) * 100)
                await message.channel.send(f"{spell.name} has equilibrated both yours and enemies HP, balance spell effectiveness = {str(effic)}%")

            elif spell.name == "trade":
                player.hp -= 80
                player.mp += 30
                await message.channel.send(f"{spell.name}  has taken 80 HP in return for 30 MP")
                player.take_dmg(enemy_dmg)
                await message.channel.send(f"Enemy attacks for {enemy_dmg} points of damage, player hp: {player.get_hp()}")

        await message.channel.send("```----------------------------------------------------------```")
        await message.channel.send(f"Enemy HP: {str(enemy.get_hp())} / {str(enemy.get_max_hp())}\nYour HP: {str(player.get_hp())} / {str(player.get_max_hp())}\nYour MP: {str(player.get_mp())} / {str(player.get_max_mp())}")

        if player.get_hp() == 0 and enemy.get_hp() == 0:
            await message.channel.send('```fix\nTIE```')
            running = False

        elif enemy.get_hp() == 0:
            await message.channel.send('```ini\n[YOU WIN]```')
            running = False

        elif player.get_hp() == 0:
            await message.channel.send('```diff\n-YOU LOSE```')
            running = False


client.run('NzkyNDI2NDM4NjQwMTQwMzE4.X-dioQ.uB86HSfV1n-Ldx0sMHesY9roKL4')
