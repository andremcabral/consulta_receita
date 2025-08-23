import time
import os
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import threading
# def verifica_receita_original(CPF, DATA_NASC, NOME):
#     _link = "https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp"
#     _xpath_cpf = '//*[@id="txtCPF"]'
#     _xpath_data = '//*[@id="txtDataNascimento"]'
#     _xpath_btconsulta = '//*[@id="id_submit"]'
#     _xpath_imprimir = '//*[@id="imgPrint"]'
#     _id_captcha = 'checkbox'
#     # cpf = '07671592765'
#     # data_nasc = '28111939'
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     pdf_save_path = os.path.join(script_dir, fr'PDFs\RECEITA_{CPF}_{NOME}.pdf')
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-software-rasterizer")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--window-size=1280,1024")  # Define tamanho padrão da janela
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(_link)
#     time.sleep(2)
#     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, _xpath_cpf))).send_keys(CPF)
#     # driver.find_element(By.XPATH, _xpath_cpf).send_keys(CPF)
#     time.sleep(2)
#     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, _xpath_data))).send_keys(DATA_NASC)
#     # driver.find_element(By.XPATH, _xpath_data).send_keys(DATA_NASC)
#     time.sleep(2)
#     # Resolver o captcha
#     iframe = driver.find_element(By.XPATH, '//*[@id="hcaptcha"]/iframe')
#     driver.switch_to.frame(iframe)
#     driver.find_element(By.ID, _id_captcha).click()
#     time.sleep(5)
#     driver.switch_to.default_content()
#     # Realizar consulta
#     driver.find_element(By.XPATH, _xpath_btconsulta).click()
#     # time.sleep(5)
#     # Clicar no botão imprimir que abre o conteúdo de impressão
#     driver.find_element(By.XPATH, _xpath_imprimir).click()
#     # time.sleep(4)
#     # Trocar para a nova aba
#     original_window = driver.current_window_handle
#     for handle in driver.window_handles:
#         if handle != original_window:
#             driver.switch_to.window(handle)
#             break
#     # time.sleep(3)
#     # Gerar PDF usando DevTools Protocol
#     result = driver.execute_cdp_cmd("Page.printToPDF", {
#         "landscape": False,
#         "printBackground": True,
#         "paperWidth": 8.27,   # A4
#         "paperHeight": 11.69,
#         "marginTop": 0.4,
#         "marginBottom": 0.4,
#         "marginLeft": 0.4,
#         "marginRight": 0.4
#     })
#     # Salvar PDF
#     pdf_data = base64.b64decode(result['data'])
#     with open(pdf_save_path, 'wb') as f:
#         f.write(pdf_data)
#     driver.quit()
#     print(f"✅ PDF gerado com sucesso em: {pdf_save_path}")
#     return pdf_save_path

def verifica_receita(mutuario, navegador_receita):
    dom_site = {
        '_link' : "https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp"
        ,'_xpath_cpf' : '//*[@id="txtCPF"]'
        ,'_xpath_data' : '//*[@id="txtDataNascimento"]'
        ,'_xpath_btconsulta' : '//*[@id="id_submit"]'
        ,'_xpath_imprimir' : '//*[@id="imgPrint"]'
        ,'_id_captcha' : 'checkbox'
    }
    print(f'Buscando dados de: {mutuario["NOME"]}')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_save_path = os.path.join(script_dir, fr'PDFs\RECEITA_{mutuario['CPF']}_{mutuario['NOME']}.pdf')
    navegador_receita.get(dom_site['_link'])
    time.sleep(2)
    WebDriverWait(navegador_receita, 60).until(EC.presence_of_element_located((By.XPATH, dom_site['_xpath_cpf']))).send_keys(mutuario['CPF'])
    time.sleep(2)
    WebDriverWait(navegador_receita, 60).until(EC.presence_of_element_located((By.XPATH, dom_site['_xpath_data']))).send_keys(mutuario['DATA_NASC'])
    time.sleep(2)
    iframe = navegador_receita.find_element(By.XPATH, '//*[@id="hcaptcha"]/iframe')
    navegador_receita.switch_to.frame(iframe)
    navegador_receita.find_element(By.ID, dom_site['_id_captcha']).click()
    time.sleep(5)
    navegador_receita.switch_to.default_content()
    navegador_receita.find_element(By.XPATH, dom_site['_xpath_btconsulta']).click()
    navegador_receita.find_element(By.XPATH, dom_site['_xpath_imprimir']).click()
    original_window = navegador_receita.current_window_handle
    for handle in navegador_receita.window_handles:
        if handle != original_window:
            navegador_receita.switch_to.window(handle)
            break
    result = navegador_receita.execute_cdp_cmd("Page.printToPDF", {
        "landscape": False,
        "printBackground": True,
        "paperWidth": 8.27,   # A4
        "paperHeight": 11.69,
        "marginTop": 0.4,
        "marginBottom": 0.4,
        "marginLeft": 0.4,
        "marginRight": 0.4
    })
    pdf_data = base64.b64decode(result['data'])
    with open(pdf_save_path, 'wb') as f:
            f.write(pdf_data)
        # navegador_receita.quit()
    print(f"✅ PDF gerado com sucesso em: {pdf_save_path}")
    return pdf_save_path

# def run_verifica_receita():
#     verifica_receita(cpf, data_nasc)

# thread = threading.Thread(target=run_verifica_receita)
# thread.start()
