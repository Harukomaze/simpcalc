import asyncio
import aiohttp
import urllib.parse
from simpcalc.errors import Overflow, BadArgument


class Calculate:
    def __init__(self):
        pass

    async def calculate(self, expr):
        expr = expr.replace('**', '^')
        my_expr = "".join(expr.split(expr))
        my_expr = urllib.parse.quote(expr)
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.mathjs.org/v4/?expr={my_expr}") as r:
              result = await r.text()
        if result.startswith("Error:"):
            raise BadArgument("An Invalid argument was passed.")
        return result
        
        
