import os
from twitchio.channel import Channel
from twitchio.user import User
from twitchio.ext import commands
import db_helper as db
import api_helper as api
import time
import threading

def point_timer():
    while True:
        time.sleep(300)
        if not api.is_live():
            continue
        users = db.get_online_users()
        for user in users:
            db.add_points(user[0], 50)
            db.add_watchtime(user[0], 300)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['ACCESS_TOKEN'], prefix='???', initial_channels=[os.environ['CHANNEL']])
    
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        db.reset_online_status()
        t = threading.Thread(target=point_timer, daemon=True, args=[])
        t.start()
    
    async def event_message(self, message):
        if message.echo:
            return
        message.content = message.content.lower()
        await self.handle_commands(message)
        
    async def event_join(self, channel: Channel, user: User):
        print(f'{user.name} joined')
        db.set_status(user.name, 1)
        return await super().event_join(channel, user)

    async def event_part(self, user: User):
        print(f'{user.name} parted')
        db.set_status(user.name, 0)
        return await super().event_part(user)

    async def handle_commands(self, message):
        if message.content[0] == "?":
            message.content = message.content[1:]
            ctx = await self.get_context(message)
            args = message.content.split(" ")
            await self.handle_command(ctx, args)
        db.set_last_message(message.author.name, message.content)

    async def handle_command(self, ctx, args):
        commands = {
            "points": self.get_points,
            "addpoints": self.add_points,
            "give": self.give_points,
            "addcommand": self.add_command,
            "removecommand": self.remove_command,
            "commands": self.list_commands,
            "watchtime": self.watchtime,
        }

        command = args[0]
        if command in commands:
            await commands[command](ctx, args[1:])
        elif command in await self.list_commands():
            await ctx.send(db.get_command(command))
        else:
            print("Invalid command")
            # await ctx.send("Invalid command")

    async def get_points(self, ctx, args):
        if len(args) > 0:
            user = args[0]
        else:
            user = ctx.author.name
        points = db.get_points(user)
        await ctx.send(f"Points {user}: {points}")

    async def add_points(self, ctx, args):
        if not ctx.author.is_mod:
            await ctx.send("You do not have permission to use this command")
            return
        if len(args) < 2:
            await ctx.send("Invalid command")
            return
        try:
            user = args[0]
            points = int(args[1])
            db.add_points(user, points)
            await ctx.send(f"Added {points} points to {user}")
        except ValueError:
            await ctx.send("Failed to add points")

    async def give_points(self, ctx, args):
        if len(args) < 2:
            await ctx.send("Invalid command")
            return
        try:
            user = args[0]
            points = int(args[1])
            if db.remove_points(ctx.author.name, points):
                db.add_points(user, points)
                await ctx.send(f"Gave {points} points to {user}")
            else:
                await ctx.send("Not enough points")
        except ValueError:
            await ctx.send("Failed to give points")

    async def watchtime(self, ctx, args):
        if len(args) > 0:
            user = args[0]
        else:
            user = ctx.author.name
        watchtime = db.get_watchtime(user)
        if watchtime < 60*60:
            await ctx.send(f"Watchtime {user}: {watchtime//60} minutes!")
        else:
            await ctx.send(f"Watchtime {user}: {watchtime//(60*60)} hours and {(watchtime // 60) % 60} minutes!")

    async def add_command(self, ctx, args):
        if not ctx.author.is_broadcaster and ctx.author.name != "krazzier":
            await ctx.send("You do not have permission to use this command")
            return
        if len(args) < 2:
            await ctx.send("Invalid command")
            return
        command = args[0]
        message = " ".join(args[1:])
        if command in await self.list_commands():
            await ctx.send("Command already exists")
            return
        db.add_command(command, message)
        await ctx.send(f"Added command {command}")

    async def remove_command(self, ctx, args):
        if not ctx.author.is_mod:
            await ctx.send("You do not have permission to use this command")
            return
        if len(args) < 1:
            await ctx.send("Invalid command")
            return
        command = args[0]
        db.remove_command(command)
        await ctx.send(f"Removed command {command}")

    async def list_commands(self, ctx = None, args = None):
        commands = db.list_commands()
        if ctx is None:
            return commands
        await ctx.send(f"Commands: {commands}")

bot = Bot()
bot.run()
