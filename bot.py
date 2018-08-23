#Gareth Bot V.1 by TheDuck

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Ready...")
    print ("Running as " + bot.user.name)
    print ("ID: " + bot.user.id)

@bot.command(pass_context=True)
async def speak(ctx):
    message = random.randint(0, 11)
    print("User has requested speak")
    if message == 1:
        print("Message 1 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "I've brought Oscar in to see what we do @BluehoopDigital #BringYourDogToWorkDay #TakeYourDogToWorkDay #BorderTerrier")
    elif message == 2:
        print("Message 2 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "It's going to be a long day #SummerSolstice")
    elif message == 3:
        print("Message 3 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Anyone that knows me might think that I'm not that emotional...  Things are very different when it comes to delivering great digital marketing for our clients...")
    elif message == 4:
        print("Message 4 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Very excited! #Solo #solostarwarsstory")
    elif message == 5:
        print("Message 5 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Day trip to Leeds with the sun shining  #grimupnorth #leeds")
    elif message == 6:
        print("Message 6 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Is Facebook listening to your conversations? Here's the 'scientific' evidence... https://www.newstatesman.com/science-tech/social-media/2018/03/testing-facebook-listens-your-conversations-adverts?amp&__twitter_impression=true … #Facebook #CambridgeAnalytics")
    elif message == 7:
        print("Message 7 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "I never believed that Unicorn Boogers were real until now!")
    elif message == 8:
        print("Message 8 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Not the best view from my office window today #Ilkley")
    elif message == 9:
        print("Message 9 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "When I'm not working I'm mostly thinking about bikes...")
    elif message == 10:
        print("Message 10 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Wonder if @dannysavage is making a cameo in The Moorside?")
    elif message == 0:
        print("Message 0 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Follow @Nashwicks on instagram!")
    elif message == 11:
        print("Message 11 chosen.")
        await bot.send_message(discord.Object(id='482109446613368842'), "Are you going to explode? If so, come outside with me...")

            

@bot.command(pass_context=True)
async def gareth(ctx):
    print("User has requested gareth")
    image = random.randint(1, 9)
    if image == 1:
        print("Image 1 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 1.jpg')
    elif image == 2:
        print("Image 2 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 2.jpg')
    elif image == 3:
        print("Image 3 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 3.jpg')
    elif image == 4:
        print("Image 4 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 4.jpg')
    elif image == 5:
        print("Image 5 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 5.png')
    elif image == 6:
        print("Image 6 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 6.png')
    elif image == 7:
        print("Image 7 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 7.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Someone loves my beard!")
    elif image == 8:
        print("Image 8 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 8.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "The christmas ride.")
    elif image == 9:
        print("Image 9 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Gareth 9.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "New profile picture?")
        
        

@bot.command(pass_context=True)
async def debbie(ctx):
    print("User has requested debbie")
    image = random.randint(1, 3)
    if image == 1:
        print("Image 1 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Debbie 1.png')
    elif image == 2:
        print("Image 2 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Debbie 2.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Writing postcards.")
    elif image == 3:
        print("Image 3 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Debbie 3.jpg')


@bot.command(pass_context=True)
async def finn(ctx):
    print("User has requested finn")
    image = random.randint(1, 10)
    if image == 1:
        print("Image 1 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 1.png')
        await bot.send_message(discord.Object(id='482109446613368842'), " New Year's Day walk  bird spotting. Red Grouse (as ever), Starlings, flock of Lapwings, Kestrel, Black Header Seagulls, and a Red Kite eating a mouse.")
    elif image == 2:
        print("Image 2 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 2.png')
    elif image == 3:
        print("Image 3 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 3.png')
    elif image == 4:
        print("Image 4 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 4.png')
    elif image == 5:
        print("Image 5 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 5.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Great to see malham cove without the summer crowds.")
    elif image == 6:
        print("Image 6 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 6.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Isn't this what everyone does on a sunday afternoon in december?")
    elif image == 7:
        print("Image 7 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 7.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Finn up early to watch youtube.")
    elif image == 8:
        print("Image 8 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 8.png')
        await bot.send_message(discord.Object(id='482109446613368842'), " Who's going to win?")
    elif image == 9:
        print("Image 9 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 9.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Holidays.")
    elif image == 10:
        print("Image 10 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Finn 10.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Last minute holly collection.")


@bot.command(pass_context=True)
async def joe(ctx):
    print("User has requested joe")
    image = random.randint(1, 5)
    if image == 1:
        print("Image 1 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Joe 1.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Big moor and big sky - North Yorkshire Moors.")
    elif image == 2:
        print("Image 2 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Joe 2.png')
    elif image == 3:
        print("Image 3 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Joe 3.png')
    elif image == 4:
        print("Image 4 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Joe 4.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Cousin love.")
    elif image == 5:
        print("Image 5 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Joe 5.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Prom wheels.")


@bot.command(pass_context=True)
async def oscar(ctx):
    print("User has requested oscar")
    image = random.randint(1, 9)
    if image == 1:
        print("Image 1 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 1.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Oscar after his Christmas bath and blow-dry. Less smelly but sulking...")
    elif image == 2:
        print("Image 2 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 2.png')
    elif image == 3:
        print("Image 3 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 3.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Back home, time to warmup.")
    elif image == 4:
        print("Image 4 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 4.png')
    elif image == 5:
        print("Image 5 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 5.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Out running with the dog.")
    elif image == 6:
        print("Image 6 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 6.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Dog on building site.")
    elif image == 7:
        print("Image 7 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 7.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Sleepy dog.")
    elif image == 8:
        print("Image 8 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 8.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Slo-mo action shot.")
    elif image == 9:
        print("Image 9 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Oscar 9.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "The dog being tormented by a giant porkscratching.")
    


@bot.command(pass_context=True)
async def lisle(ctx):
    print("User has requested lisle")
    image = random.randint(1, 8)
    if image == 1:
        print("Image 1 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 1.png')
    elif image == 2:
        print("Image 2 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 2.png')
    elif image == 3:
        print("Image 3 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 3.png')
    elif image == 4:
        print("Image 4 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 4.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Tree going up.")
    elif image == 5:
        print("Image 5 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 5.png')
    elif image == 6:
        print("Image 6 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 6.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Dark satanic mills of saltaire...")
    elif image == 7:
        print("Image 7 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 7.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "I love it when it rains.. perfect excuse for sitting and doing absolutely nothing.")
    elif image == 8:
        print("Image 8 chosen.")
        await bot.send_file(discord.Object(id='482109446613368842'), 'Lisle 8.png')
        await bot.send_message(discord.Object(id='482109446613368842'), "Just before the Tour De France. Look, no traffic!")


@bot.command(pass_context=True)
async def info(ctx):
    print("User has requested info.")
    await bot.send_message(discord.Object(id='482109446613368842'), "Here is a list of commands")
    await bot.send_message(discord.Object(id='482109446613368842'), "!speak - I say something to you.")
    await bot.send_message(discord.Object(id='482109446613368842'), "!info - This list appears.")
    await bot.send_message(discord.Object(id='482109446613368842'), "!gareth - A picture of me!")
    await bot.send_message(discord.Object(id='482109446613368842'), "!debbie - A picture of Debbie!")
    await bot.send_message(discord.Object(id='482109446613368842'), "!finn - A picture of Finn!")
    await bot.send_message(discord.Object(id='482109446613368842'), "!joe - A picture of Joe!")
    await bot.send_message(discord.Object(id='482109446613368842'), "!oscar - A picture of Oscar!")
    await bot.send_message(discord.Object(id='482109446613368842'), "!lisle - A picture of multiple Lisles together!")

    

bot.run("NDgyMTA4MTQ3MTIxNzgyNzg4.DmAF-Q.vaKC_tVeS2fwjgaZ_WS4bzZyW2g")
