import sys
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop

"""
$ python3.5 skeletona.py <token>

A skeleton for your async telepot programs.
"""

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, handle).run_forever())
print('Listening ...')

loop.run_forever()
