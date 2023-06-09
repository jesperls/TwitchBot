import os
from twitchio.channel import Channel
from twitchio.ext import commands
import db_helper
import time
import threading
import asyncio
import requests

from twitchio.user import User

async def point_timer():
    while True:
        await asyncio.sleep(5)
        users = db_helper.get_online_users()
        info = await bot.fetch_channel(os.environ['CHANNEL'], os.environ['ACCESS_TOKEN'])
        print(info.title, info.delay)
        for user in users:
            db_helper.add_points(user[0], 100)


class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(token=os.environ['ACCESS_TOKEN'], prefix='?', initial_channels=[os.environ['CHANNEL']])
    
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        db_helper.reset_online_status()
        # task = asyncio.Task(point_timer())
        # t = threading.Thread(target=point_timer, daemon=True, args=[])
        # t.start()
    
    async def event_message(self, message):
        if message.echo:
            return
        message.content = message.content.lower()
        await self.handle_commands(message)
        
    async def event_join(self, channel: Channel, user: User):
        print(f'{user.name} joined')
        db_helper.set_status(user.name, 1)
        return await super().event_join(channel, user)

    async def event_part(self, user: User):
        print(f'{user.name} parted')
        db_helper.set_status(user.name, 0)
        return await super().event_part(user)

    async def handle_commands(self, message):
        ctx = await self.get_context(message)
        args = message.content.split(" ")
        db_helper.set_status(ctx.author.name, 1)
        if args[0] == "?points":
            if len(args) > 1:
                await ctx.send(f'Points {args[1]}: {db_helper.get_points(args[1])}')
            else:
                await ctx.send(f'Points {ctx.author.name}: {db_helper.get_points(ctx.author.name)}')
        if args[0] == "?addpoints" and ctx.author.is_mod:
            if len(args) > 1:
                try:
                    if len(args) > 2:
                        db_helper.add_points(args[1], int(args[2]))
                    else:
                        db_helper.add_points(ctx.author.name, int(args[1]))
                except ValueError:
                    print("SOME DOOFUS GOOFED")



bot = Bot()
bot.run()