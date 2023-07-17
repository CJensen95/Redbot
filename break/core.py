import discord
from redbot.core import commands
from discord.ext.commands import has_permissions, CheckFailure

class Break(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_roles = {}  # Store user's roles
        self.staff_roles = ["manager", "barista", "cafe attendant", "caffeinated crew", "shop owner", "server hr", "CST"]

    async def cog_before_invoke(self, ctx):
        member = ctx.author
        if not any(role.name in self.staff_roles for role in member.roles):
            raise CheckFailure("You do not have the necessary role to use this command.")

    @commands.command()
    @has_permissions(manage_roles=True)
    async def onbreak(self, ctx, break_role: str):
        member = ctx.message.author
        self.user_roles[member.id] = [role for role in member.roles if role.name in self.staff_roles]  # Save the user's roles
        for role in self.user_roles[member.id]:  # Remove user's roles
            await member.remove_roles(role)
        on_break_role = discord.utils.get(member.guild.roles, name=break_role)  # Get the break role
        if on_break_role is not None:
            await member.add_roles(on_break_role)  # Assign break role
        else:
            await ctx.send(f"Role {break_role} not found.")

    @commands.command()
    @has_permissions(manage_roles=True)
    async def offbreak(self, ctx, break_role: str):
        member = ctx.message.author
        on_break_role = discord.utils.get(member.guild.roles, name=break_role)  # Get the break role
        if on_break_role in member.roles:
            await member.remove_roles(on_break_role)  # Remove break role
            for role in self.user_roles[member.id]:  # Assign user's previous roles
                await member.add_roles(role)
            del self.user_roles[member.id]  # Delete the stored roles
        else:
            await ctx.send(f"Role {break_role} not found.")

async def setup(bot):
    await bot.add_cog(Break(bot))
