import datetime
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
DATA = f"{datetime.date.today().day:02d}{datetime.date.today().month:02d}{datetime.date.today().year}"
_LINK_SEI = "https://sei.rj.gov.br/sip/login.php?sigla_orgao_sistema=ERJ&sigla_sistema=SEI"
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
UNIDADES = {
         'CIF': {'XPATH_TOPO': '//*[@id="divInfraAreaTabela"]/table/tbody/tr[2]/td[1]', 'textoUnidade': 'CEHAB/03-COOIF'}
        ,'SHF': {'XPATH_TOPO': '//*[@id="divInfraAreaTabela"]/table/tbody/tr[4]/td[1]', 'textoUnidade': 'CEHAB/03-SERVHF'}
        ,'SFI': {'XPATH_TOPO': '//*[@id="divInfraAreaTabela"]/table/tbody/tr[3]/td[1]', 'textoUnidade': 'CEHAB/03-SERVFI'}
}

def troca_unidade(navegador, unidade):
    print(unidade)
    navegador.find_element(By.XPATH, '//*[@id="divInfraBarraSistemaPadraoD"]/div[3]').click()
    try:
        navegador.find_element(By.XPATH, f"{UNIDADES[unidade]['XPATH_TOPO']}").click()
    except:
        navegador.find_element(By.XPATH, f"{UNIDADES[unidade]['XPATH_TOPO']}").click()

def anexar_arquivo(mutuario, navegador_sei):
    try:
        navegador_sei.get(_LINK_SEI)
        navegador_sei.find_element(By.ID, objetos_site['ID_USUARIO']).send_keys(dados_de_acesso['USUARIO'])
        sleep(1)
        navegador_sei.find_element(By.ID, objetos_site['ID_SENHA']).send_keys(dados_de_acesso['SENHA'])
        sleep(1)
        select_element = navegador_sei.find_element(By.ID, objetos_site['ID_ORGAO'])
        sleep(1)
        select_object = Select(select_element)
        sleep(1)
        select_object.select_by_visible_text(dados_de_acesso['ORGAO'])
        sleep(3)
        navegador_sei.find_element(By.ID, objetos_site['ID_BOTAO']).click()
        sleep(3)
        unidade_atual = navegador_sei.find_element(By.XPATH, '//*[@id="divInfraBarraSistemaPadraoD"]/div[3]').text
        # print('unidade_atual')
        # print(unidade_atual)
        # print('Unidade do SEI')
        unidade_sei = mutuario['UNIDADE']
        # print(unidade_sei)
        # print(UNIDADES[unidade_sei])
        # print(type(UNIDADES[unidade_sei]))
        # print(UNIDADES[mutuario['UNIDADE']['textoUnidade']])

        if unidade_atual == UNIDADES[unidade_sei]['textoUnidade']:
            pass
        else:
            troca_unidade(navegador_sei, mutuario['UNIDADE'])
        unidade_atual = navegador_sei.find_element(By.XPATH, '//*[@id="divInfraBarraSistemaPadraoD"]/div[3]').text
        print(f'Buscando em: {unidade_atual}')
        print(f"{mutuario['NUMERO_SEI']} - {mutuario['NOME']}")
        if len(navegador_sei.find_elements(By.CLASS_NAME, 'sparkling-modal-frame')) > 0:
            iframe = navegador_sei.find_element(By.NAME, 'modal-frame')
            navegador_sei.switch_to.frame(iframe)
            navegador_sei.find_element(By.CLASS_NAME, 'infraCheckboxDiv ').click()
            navegador_sei.find_element(By.CLASS_NAME, 'sparkling-modal-close ').click()
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divInfraBarraSistemaPadraoD"]/div[3]')))
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.ID, objetos_site['ID_CAMPO_BUSCA']))).send_keys(mutuario['NUMERO_SEI'])
        navegador_sei.find_element(By.ID, objetos_site['ID_BOTAO_LUPA']).click()
        sleep(3)
        iframe2 = navegador_sei.find_element(By.ID, 'ifrConteudoVisualizacao')
        navegador_sei.switch_to.frame(iframe2)
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_BOTAO_NOVO']))).click()
        iframe3 = navegador_sei.find_element(By.ID, 'ifrVisualizacao')
        navegador_sei.switch_to.frame(iframe3)
        # input('verificar')
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_SEL_ANEXO']))).click()
        select_element = WebDriverWait(navegador_sei, 60).until(EC.presence_of_element_located((By.ID, objetos_site['ID_TIPO_DOC'])))
        select = Select(select_element)
        sleep(2)
        select.select_by_visible_text('Anexo')
        sleep(2)
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_SEL_NATO']))).click()
        sleep(2)
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.ID, objetos_site['ID_CAMPO_DATA']))).send_keys(f'{DATA}')
        sleep(2)
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.ID, objetos_site['ID_CAMPO_ARVORE']))).send_keys(f'RECEITA_{mutuario['NOME']}')
        sleep(2)
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.ID, objetos_site['ID_INFORMAR_ARQUIVO']))).send_keys(mutuario['COMPROVANTE'])
        sleep(2)
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.XPATH, objetos_site['XPATH_SEL_PUBLICO']))).click()
        sleep(2)
        WebDriverWait(navegador_sei, 5).until(EC.presence_of_element_located((By.ID, objetos_site['ID_BOTAO_SALVAR']))).click()
        sleep(2)
        # input('✅ Hora de conferência')
        # navegador_sei.quit()
    except (ValueError, TypeError) as e:
        print('❌ Erro ao anexar arquivo')
        # navegador_sei.quit()
        print(f"Erro: {e}")

# anexar_receita(navegador_sei, NOME, comprovante, DATA)
