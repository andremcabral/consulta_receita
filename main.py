import pandas as pd
from consultaReceita import verifica_receita
from anexaArquivo import anexar_arquivo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options_sei = Options()
chrome_options_sei.add_argument("--headless=new")
chrome_options_sei.add_argument("start-maximized")
chrome_options_sei.add_argument("--disable-extensions")
nome_arquivo = 'dados.xlsx'

df = pd.read_excel("dados.xlsx", dtype=str)
df = df.fillna('')
dados = df.to_dict(orient="records")
print(dados)
receita = 'sim'
anexa = 'sim'

def testar():
    if receita == 'sim':
        for index, mutuario in enumerate(dados):
            with webdriver.Chrome(options=chrome_options) as navegador_receita:
                try:
                    dados[index]['COMPROVANTE'] = verifica_receita(mutuario, navegador_receita)
                    df_atualizado = pd.DataFrame(dados)
                    df_atualizado.to_excel("dados.xlsx", index=False)
                except:
                    dados[index]['COMPROVANTE'] = verifica_receita(mutuario, navegador_receita)
                    df_atualizado = pd.DataFrame(dados)
                    df_atualizado.to_excel("dados.xlsx", index=False)
    if anexa == 'sim':
        for index, mutuario in enumerate(dados):
            with webdriver.Chrome(options=chrome_options_sei) as navegador_sei:
                anexar_arquivo(mutuario, navegador_sei)
# try:
testar()
#     df_atualizado = pd.DataFrame(dados)
#     df_atualizado.to_excel("dados.xlsx", index=False)
# except (ValueError, TypeError) as e:
#     print('❌ Erro no código')
#     print(f"Erro: {e}")
