import asyncio
import logging
import re
from datetime import datetime
import os
import sys
import random
from time import sleep


logging.basicConfig(level=logging.ERROR)
from operator import pow, sub, mul, add, truediv

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.types import UpdateNewMessage, PeerChannel
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, YouBlockedUserError, PhoneNumberBannedError
from datetime import datetime
from telethon import functions, types
from colorama import Fore, init as color_ama
color_ama(autoreset=True)
#os.system('cls' if os.name=='nt' else 'clear')
api_id = 717425
api_hash = '322526d2c3350b1d3530de327cf08c07'

chnl = '@DOGE_Star_bot'

def selow(x):
    tm= datetime.now().strftime("%X")
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("[\033[1;33m"+tm+"\033[1;37m] Please wait for\033[1;32m {:02d} \033[1;37mseconds..".format(remaining))
       sys.stdout.flush()
       sleep(1)

async def main():
	
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	
	if not os.path.exists("Account"):
		os.mkdir("Account")
   
    # Connect to client
	client = TelegramClient('Account/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	if me is not None:
		try:
			await client.send_message(chnl, '💶 Star Bonus')
		except YouBlockedUserError:
#			msg_print(Back.GREEN + Fore.WHITE+"You Banned from Channel"+Back.RESET+" "+Fore.RED+phone+Fore.RESET)
			sys.exit()

	@client.on(events.NewMessage( chats=chnl, incoming=True))
	async def clls(event):
		global now
		now= datetime.now().strftime("%X")
		id=event.raw_text
		if '👏Congratulations ....' in id:
			pr= '0.16000000 Doge'
			sys.stdout.write("\r")
			sys.stdout.write("                                                                ")
			sys.stdout.write("\r")
			sys.stdout.write('[\033[1;35m'+now+'\033[1;37m]=[\033[1;32m Success You Get a Bonus \033[1;37m=> \033[1;33m'+pr+' \033[1;37m]\n')
			sys.stdout.flush()
			selow(600)
			await client.send_message(chnl, '💶 Star Bonus')
		else:
			selow(600)
			await client.send_message(chnl, '💶 Star Bonus')
			
		

	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())