import discord
from discord.ext import commands
import aiohttp
#from .utils.dataIO import fileIO
#from random import choice as randchoice
#import os

outChan = ""

class Suggestion:
    """Skar's Anonymous Suggestion Box"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(no_pm=True, pass_context=True)
    async def setSuggestOutput(self, ctx, *, chan):
    	"""Set the channel to output annonymous suggestions to. 
    	Use [p]setSuggestOutput <channel> """
    	outChan = chan
    	if outChan != "":
    		await self.bot.say("Output set to " + outChan + "successfully.")
    	else: 
    		await self.bot.say("OH NOES! Something went wrong. I'm sorry, but I couldn't save that as the output channel. It may not exist or there may be an error in the script. Contact @SkardonRydholm#0666 via Discord or via email: skardonrydholm@gmail.com")
    

    @commands.command(no_pm=True, pass_context=True)
    async def suggest(self, ctx, *, sggtn):
    	"""Takes a user's suggestions anonymously. This will be output into a separate channel and the original suggestion will be deleted for user privacy. """
    	if outChan == "":
    		await self.bot.say("There is currently no output channel set and your suggestion could not be registered. Please contact a server administrator to notify them of this error.")
    	else:
    		suggestion = sggtn
    		#delete user message for anonymity.
    		sggtnID = ctx.message.id 
    		await self.bot.delete_message(sggtnID)
    		#send suggestion to output channel
    		await self.bot.say("Thank you for your suggestion " + user.mention + ". We will review all suggestions periodically. You may see your ideas implemented in the near future!")

def setup(bot):
    bot.add_cog(Suggestion(bot))
