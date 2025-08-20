import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from consultaReceita import verifica_receita
CPF = '00408731702'
DATA_NASC = '11061968'
NUMERO_SEI = 'SEI-490002/001152/2025'
NOME = 'RECEITA_IVONE'
DATA = f"{datetime.date.today().day:02d}{datetime.date.today().month:02d}{datetime.date.today().year}"
objetos_site = {
     'CLASSE_LINHA' : 'infraTrClara'
    ,'ID_USUARIO' : 'txtUsuario'
    ,'ID_SENHA' : 'pwdSenha'
    ,'ID_ORGAO' : 'selOrgao'
    ,'ID_BOTAO' : 'sbmAcessar'
    ,'ID_BOTAO_SALVAR' : 'btnSalvar'
    ,'ID_BOTAO_LUPA' : 'spnInfraUnidade'
    ,'ID_BOTAO_ANEXAR' : 'lblArquivo'
    ,'ID_INFORMAR_ARQUIVO' : 'filArquivo'
    ,'ID_CAMPO_BUSCA' : 'txtPesquisaRapida'
    ,'ID_CAMPO_DESCRICAO' : 'txtDescricao'
    ,'ID_CAMPO_ARVORE' : 'txtNomeArvore'
    ,'ID_CAMPO_NUMERO' : 'txtNumero'
    ,'ID_CAMPO_DATA' : 'txtDataElaboracao'
    ,'XPATH_BOTAO_NOVO' : '//*[@id="divArvoreAcoes"]/a[1]/img'
    ,'ID_TIPO_DOC' : 'selSerie'
    ,'XPATH_SEL_ANEXO' : '//*[@id="tblSeries"]/tbody/tr[1]/td/a[2]'
    ,'XPATH_SEL_NATO' : '//*[@id="divOptNato"]/div/label'
    ,'XPATH_SEL_PUBLICO' : '//*[@id="divOptPublico"]/div/label'
}
dados_de_acesso = {
    'USUARIO': "andre0695", 'SENHA' : "@lfa0110", 'ORGAO' : "CEHAB"
}
chrome_options = Options()
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
LINK = "https://sei.rj.gov.br/sip/login.php?sigla_orgao_sistema=ERJ&sigla_sistema=SEI"

# comprovante = verifica_receita(CPF, DATA_NASC, NOME)
comprovante = r'D:\PROJETOS EM ANDAMENTO\consulta_receita\PDFs\RECEITA_00408731702_RECEITA_IVONE.pdf'
navegador = webdriver.Chrome(options=chrome_options)

def anexar_receita(navegador, NOME, comprovante, DATA):
    navegador.get(LINK)
    navegador.find_element(By.ID, objetos_site['ID_USUARIO']).send_keys(dados_de_acesso['USUARIO'])
    sleep(1)
    navegador.find_element(By.ID, objetos_site['ID_SENHA']).send_keys(dados_de_acesso['SENHA'])
    sleep(1)
    select_element = navegador.find_element(By.ID, objetos_site['ID_ORGAO'])
    sleep(1)
    select_object = Select(select_element)
    sleep(1)
    select_object.select_by_visible_text(dados_de_acesso['ORGAO'])
    sleep(3)
    navegador.find_element(By.ID, objetos_site['ID_BOTAO']).click()
    sleep(3)
    if len(navegador.find_elements(By.CLASS_NAME, 'sparkling-modal-frame')) > 0:
        iframe = navegador.find_element(By.NAME, 'modal-frame')
        navegador.switch_to.frame(iframe)
        navegador.find_element(By.CLASS_NAME, 'infraCheckboxDiv ').click()
        navegador.find_element(By.CLASS_NAME, 'sparkling-modal-close ').click()
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divInfraBarraSistemaPadraoD"]/div[3]')))
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.ID, objetos_site['ID_CAMPO_BUSCA']))).send_keys(NUMERO_SEI)
    navegador.find_element(By.ID, objetos_site['ID_BOTAO_LUPA']).click()
    sleep(3)
    iframe2 = navegador.find_element(By.ID, 'ifrConteudoVisualizacao')
    navegador.switch_to.frame(iframe2)
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_BOTAO_NOVO']))).click()
    iframe3 = navegador.find_element(By.ID, 'ifrVisualizacao')
    navegador.switch_to.frame(iframe3)
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_SEL_ANEXO']))).click()
    select_element = WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.ID, objetos_site['ID_TIPO_DOC'])))
    select = Select(select_element)
    sleep(2)
    select.select_by_visible_text('Anexo')
    sleep(2)
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_SEL_NATO']))).click()
    print(f'Arquivo está em: {comprovante}')
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.ID, objetos_site['ID_CAMPO_DATA']))).send_keys(f'{DATA}')
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.ID, objetos_site['ID_CAMPO_ARVORE']))).send_keys(f'{NOME}')
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.ID, objetos_site['ID_INFORMAR_ARQUIVO']))).send_keys(comprovante)
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_SEL_PUBLICO']))).click()
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.ID, objetos_site['ID_BOTAO_SALVAR']))).click()
    input('confere')

anexar_receita(navegador, NOME, comprovante, DATA)
