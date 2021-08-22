#Copyright (C) 2021  Anwar Gatto, Michael Gatto
#    This program comes with ABSOLUTELY NO WARRANTY; for details go to https://www.gnu.org/licenses/
 #   This is free software, and you are welcome to redistribute it
  #  under certain conditions; for details go to https://www.gnu.org/licenses/
# Built for the Anza Trail School and the Anza Trail Music Department. Ownership retained by Anwar Gatto (I.E. Software remains open source under GNU GPLv3 Licanse)
# All rights reserved.
print("Copyright (C) 2021  Anwar Gatto, Michael Gatto")
print("This program comes with ABSOLUTELY NO WARRANTY; for details go to https://www.gnu.org/licenses/")
print("This is free software, and you are welcome to redistribute it under certain conditions; for details go to https://www.gnu.org/licenses/")
print("https://github.com/RyzenGatto/BoenziBotPublic")

"""
Track a student's location.

Update a google sheets' "location" column from discord, based on the user's discord username
"""


#import os
import discord
import gspread
#import sys
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.py', scope)
gc = gspread.authorize(credentials)
wks = gc.open("Insert the name of your google sheet here").sheet1
#sys.exit()

client = discord.Client()

#token = os.getenv('INSERT DISCORD BOT TOKEN HERE')
token = ('INCSERT DISCORD BOT TOKEN HERE') # @TODO refactor for security

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Command to insert data to excel
    # !w is the prefix for the bot, change it to whatever you'd like (or keep it)
    if message.content.startswith('!w ') or message.content.startswith('!W '):
        location = message.content[3:]

        result = [x.strip() for x in location.split(',')]
        if len(result) == 1:

            name = str(message.author)
            #name = repl(message.author)

            cell = wks.find(name)
                #check for error
            
            wks.update_cell(cell.row, cell.col + 1, result[0])
                #check for error

            await message.channel.send('Done')
        else:
            # Needs more/less fields
            # The string below is optional
            await message.channel.send('Error: Invalid. Please select one of the three listed. PM SERVER OWNER if you need more help.'.format(FIELDS,FIELDS-1))
    
    # Whois
    # Please dont remove the copyright and github repo
    elif len(message.mentions) > 0:
        for muser in message.mentions:
            if muser.id == client.user.id:
                if any(word in message.content for word in ['whois','who is','Help','help','info']):
                    await message.channel.send('This bot was made by RyzenGatto on Github. More details at https://github.com/RyzenGatto/BoenziBotV2')

client.run(token)