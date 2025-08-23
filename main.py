import pandas as pd
from consultaReceita import verifica_receita
from anexaArquivo import anexar_arquivo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
nome_arquivo = 'dados.xlsx'

df = pd.read_excel("dados.xlsx", dtype=str)
df = df.fillna('')
dados = df.to_dict(orient="records")
print(dados)

def testar():
    with webdriver.Chrome(options=chrome_options) as navegador_receita:
        for index, mutuario in enumerate(dados):
            dados[index]['COMPROVANTE'] = verifica_receita(mutuario, navegador_receita)
    print(dados)
    # with webdriver.Chrome(options=chrome_options) as navegador_sei:
    #     for index, mutuario in enumerate(mutuarios):
    #         anexar_arquivo(mutuario, navegador_sei)
testar()
df_atualizado = pd.DataFrame(dados)
df_atualizado.to_excel("dados.xlsx", index=False)
