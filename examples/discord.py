from discord.ext import commands
from simpcalc import simpcalc

class Calc(commands.Cog):
     def __init__(self, bot):
	self.bot = bot
        self.calculator = simpcalc.Calculate()
        
     @commands.command()
     async def calculate(self, ctx, *, expr = None):
        if not expr:
          return await ctx.send('You have to provide an equation to calculate!')
        result = await self.calculator.calculate(expr)
        await ctx.send(f'The result is {result}')
        
        
def setup(bot):
  bot.add_cog(Calc(bot))
  
