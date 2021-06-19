import discord
import time
import asyncio

client = discord.Client()
id = client.get_guild(Your Server ID)


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")
            await asyncio.sleep(5)
        except  Exception as e:
            print(e)
            await asyncio.sleep(5)
joined = 0
messages = 0
client.loop.create_task(update_stats())

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")
@client.event
async def on_message(message):
    id = client.get_guild(Your Server ID)
    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)
    global messages
    messages += 1
    channels = ["bot-commands"]
    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""Members Number: {id.member_count}""")




# for running bot
client.run("Your Bot Token")
