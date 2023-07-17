import json
from pathlib import Path

from redbot.core.bot import Red

from .break import break

with open(Path(__file).parent / "info.json") as fp:
        __red_end_user_data_statement__ = json.load(fp)["edn_user_data_statement"]


async def setup(bot: Red):
    await bot.add_cog(break(bot))
