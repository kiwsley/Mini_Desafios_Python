import pandas as pd
from datetime import datetime
import os 
import win32com.client as win32 

caminho = "C:\\Users\\Kiwsley\\Documents\\desafio python\\Mini_Desafios_Python\\Automacao_Planilhas_Python\\bases\\"

arquivos = os.listdir(caminho)
print (arquivos)

tabela_consolidada = pd.DataFrame()

for nome_arquivos in arquivos:
   tabela_vendas = pd.read_csv(os.path.join(caminho, nome_arquivos))
   tabela_vendas["Data de Venda"]= pd.to_datetime("01/01/1900")+pd.to_timedelta(tabela_vendas["Data de Venda"],unit="d")
   tabela_consolidada= pd.concat([tabela_consolidada, tabela_vendas])
   print (tabela_vendas)

tabela_consolidada = tabela_consolidada.sort_values(by="Data de Venda")
tabela_consolidada = tabela_consolidada.reset_index(drop = True)
#print(tabela_consolidada)     
tabela_consolidada.to_excel("Vendas.xlsx", index=False)

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)
email.To = "kiwsleyfreire@gmail.com"
data_hoje = datetime.today().strftime("%d/%m/%Y")
email.Subject = f"Relatório de Vendas {data_hoje}"

email.Body = f"""""
Prezados,

Segue em anexo o relatório de vendas da data {data_hoje} atualizado.
qualquer dúvida estou à disposição.

Abs,
Kiwsley py
"""
caminho = os.getcwd()
anexo=os.path.join(caminho, "Vendas.xlsx")
email.Attachments.Add(anexo)

email.Send()