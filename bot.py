import basc_py4chan
import discord
from discord.ext import commands
import os

files = None

def get_files(board, thread_id):
    print("Getting from /" + board  + "/" + str(thread_id))
    board = basc_py4chan.Board(board)
    thread = board.get_thread(thread_id)

    return thread.file_objects()


bot = commands.Bot(command_prefix='pp')

@bot.command()
async def set(ctx):
    global files
    args = ctx.message.content.split()
    board = args[1] 
    thread = args[2]

    files = get_files(board, int(args[2]))

    await ctx.send('Set the thread')

@bot.command()
async def next(ctx):
    await ctx.send(files.__next__().file_url)

@bot.command()
async def test(ctx):
    print("test")
    await ctx.send('test')



if __name__ == '__main__':
    bot.run(os.environ["DISC_BOT"])


