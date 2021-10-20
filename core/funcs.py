import os
from time import sleep
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, find_dotenv


# Encontra o .env e carrega as informações de configuração
load_dotenv(find_dotenv())

# Abre uma instância do navegar Chrome
driver = Chrome()

# Altera o tamanho do navegador
driver.set_window_size(1200, 800)

# Aguarda 2 segundos antes de continuar a execução
sleep(2)
# Pega o domínio do site no arquivo de configuração .env
driver.get(os.getenv("DOMAIN"))

sleep(2)
# Pega o elemento botão da página e efetua o click para navegar até a página de login
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a").click()


# Função para inserir os dados no formulário
def inserting_data():
  try:
    # Acha o elemento de input de E-mail e senha para inserir os dados
    driver.find_element_by_xpath("//*[@id='login_field']").send_keys(os.getenv("EMAIL"))
    sleep(1.5)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(os.getenv("PASSWORD"))
    sleep(1.5)
    # Acha o elemento botão para fazer autenticação
    driver.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()
    sleep(3)
  except:
    print("Erro! Falha na execução")


# Função para fazer a validação dos status
def validate():
  try:
    error = driver.find_element_by_class_name("flash.flash-full.flash-error").text
    if error == "Incorrect username or password.":
      print("\nAutenticação falhou")
      sleep(4)
      driver.close()
  except (NoSuchElementException):
    driver.close()
    