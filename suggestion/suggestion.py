import discord
from discord.ext import commands

class Suggestion:
    """Skar's Anonymous Suggestion Box"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=False, pass_context=True)
    async def setSuggestOutput(self, ctx, *, chan):
    	"""Set the channel to output annonymous suggestions to. 
    	Use [p]setSuggestOutput <channel> """
		await self.bot.say("Contact @SkardonRydholm#0666 via Discord or via email: skardonrydholm@gmail.com")
    

    @commands.command(no_pm=False, pass_context=True)
    async def suggest(self, ctx, *, sggtn):
    	"""Takes a user's suggestions anonymously. This will be output into a separate channel and the original suggestion will be deleted for user privacy. """	
    	await self.bot.say("Thank you for your suggestion " + user.mention + ". We will review all suggestions periodically. You may see your ideas implemented in the near future!")

def setup(bot):
    bot.add_cog(Suggestion(bot))
