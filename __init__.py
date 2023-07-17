from .break import break


async def setup(bot):
    await bot.add_cog(break(bot))
