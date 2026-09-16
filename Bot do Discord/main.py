# Importa as bibliotecas nescessárias
import asyncio
import discord
from discord.ext import commands
from config import DISCORD_TOKEN

# configuração dos intents (Acessos privilegiados ativados no portal do Discord)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# cria o bot com o prefixo de comando "!"
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_extensions():
    #carrega todas as extensões (cogs) do diretório "presentation/cogs."
    #lista de cogs a serem carregadas
    initial_cogs = [
        "src.presentation.cogs.system_cog",
    ]
    # faz um loop para carregar cada cog da lista
    for cog in initial_cogs:
        try:
            await bot.load_extension(cog)
            print(f"Cog Módulo {cog} carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar o Módulo {cog}: {e}")

# Inicia o bot com o token do Discord
async def main():
    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())