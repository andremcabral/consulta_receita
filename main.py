from consultaReceita import verifica_receita
from anexaArquivo import anexar_arquivo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

mutuarios = [
    {
    'CPF' : '00408731702'
    ,'DATA_NASC' : '11061968'
    ,'NUMERO_SEI' : 'SEI-490002/001152/2025'
    ,'NOME' : 'RECEITA_IVONE'
    ,'COMPROVANTE' : ""
    }
    ,{
    'CPF' : '00408731702'
    ,'DATA_NASC' : '11061968'
    ,'NUMERO_SEI' : 'SEI-490002/001152/2025'
    ,'NOME' : 'SEGUNDA_VEZ'
    ,'COMPROVANTE' : ""
    }
]

print(mutuarios)
with webdriver.Chrome(options=chrome_options) as navegador_receita:
    for index, mutuario in enumerate(mutuarios):
        mutuarios[index]['COMPROVANTE'] = verifica_receita(mutuario, navegador_receita)
print(mutuarios)

with webdriver.Chrome(options=chrome_options) as navegador_sei:
    for index, mutuario in enumerate(mutuarios):
        anexar_arquivo(mutuario, navegador_sei)