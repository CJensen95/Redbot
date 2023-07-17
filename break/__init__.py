from .core import break

__red_end_user_data_statement__ = (
        "this cog stores data about users"
)


async def setup(bot):
    await bot.add_cog(break(bot))
