# Importa as bibliotecas nescessárias
# Importa a função load_dotenv da biblioteca dotenv para carregar variáveis de ambiente de um arquivo .env
import os
from dotenv import load_dotenv

# carrega as variáveis do arquivo .env
load_dotenv()

# Vai até a memória e busca o valor guardado na chave "DISCORD_TOKEN" e atribui à variavel DISCORD_TOKEN. Se a chave não existir, retorna None.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Faz a validação se a variável DISCORD_TOKEN foi carregada corretamente. Se não, lança um erro informando que o token não foi encontrado.
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN não encontrado no arquivo .env")