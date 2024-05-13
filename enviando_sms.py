# Passo a Passo para a Solução

# 1 - Abrir os 6 arquivos Excel
# 2 - para cada arquivo, vou verificar se algum valor naquele arquivo na coluna de vendas é maior que 55 000
# 3 - Se for maior que 55 000, envio um SMS para o meu número, com o Nome do vendedor, Mês e as vendas do Vendedor.

# Importar Bibliotecas

# Pandas - Integração do Python com Excel
!pip install pandas

# OpenPyXL - Integração do Python com Excel (Pandas e OpenPyXL atuam em Conjunto)
!pip install openpyxl

# Twilio - Integraçao do Python com SMS
!pip install twilio

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Seu Twilio SID"
# Your Auth Token from twilio.com/console
auth_token  = "Seu Token"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
  tabela_vendas = pd.read_excel(f'Materiais 1a aula/{mes}.xlsx')
  if (tabela_vendas['Vendas'] > 55000).any():
    # .any() -> esta pegando cada valor dentro da coluna Vendas

    vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
    vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
    # .loc[] ajuda a localizar uma ou mais linhas de uma tabela, no colchetes eu passo qual linha e qual coluna eu quero
    # o .loc[] Como faço para achar a linha que na coluna vendas bateu 55000? Deve ser feita uma condição...
    # no caso a condição ja foi feita no If, preciso de vendas que bateu 55000: tabela_vendas['Vendas'] > 55000
    # .values[] como .loc[] não retorna um valor e sim uma tabela, o .values[0] serve para retornar somente o valor.

    print(f'No mês de {mes} o vendedor {vendedor} bateu a meta! Total em vendas: {vendas} reais.')
    message = client.messages.create(
            to="Seu Numero Celular", # para qual numero vai enviar
            from_="Seu Numero Twilio", # meu numero Twilio
            body=f'No mês de {mes} o vendedor {vendedor} bateu a meta! Total em vendas: {vendas} reais.')
    print(message.sid)
