from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep
import json
from datetime import date
class GupyScrapper():
    driver = webdriver.Firefox()
    num_pages = 1
    lista_vagas = {
        'vaga': "",
        'local': ""
    }
    def __init__(self):
        #o site a ser raspado
        url = "https://brisanet.gupy.io"
        self.driver.get(url)
        sleep(1)
        self.reject_cookies()
        self.scroll_down()
        self.num_pages = self.get_num_pages()
        self.driver.refresh()
        sleep(1)
        self.scroll_down()
        self.get_jobs(self.num_pages)
        self.save_json(self.lista_vagas)
        self.check_interests(self.lista_vagas)
        self.driver.quit()

    def reject_cookies(self):
        """Retira o pop-up perguntando sobre o uso de cookies"""
        sleep(1)
        botao_cookie = self.driver.find_element(By.CLASS_NAME, 'dp-bar-button')
        botao_cookie.click()

    def scroll_down(self):
        """Scrola pra baixo para que o botão next fique visível"""
        self.driver.execute_script('window.scrollBy(0,-100)')

    def get_num_pages(self):
        """Passa por várias páginas para poder verificar qual a última"""
        print("\033[32m Verificando quantas páginas existem \033[m")
        for i in range(15):
            botao_proximo = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/section[3]/div[3]/nav/ul/li[5]/button')
            botao_proximo.click()
        botao_ultimo = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/section[3]/div[3]/nav/ul/li[4]/button')
        num_pages = int(botao_ultimo.text)
        print("\033[32m Há "+ str(num_pages) + " páginas \033[m")
        return num_pages

    def get_jobs(self, num_pages):
        jobs_list = []
        places_list = []
        print("\033[32m Copiando cada vaga \033[m")
        for page in range(num_pages):
            vagas = self.driver.find_elements(By.CLASS_NAME, 'sc-f5007364-4')
            locais = self.driver.find_elements(By.CLASS_NAME, 'KCtRP')
            for vaga in vagas:
                jobs_list.append(vaga.text)
            for local in locais:
                places_list.append(local.text)
            #sleep(1)
            botao_proximo = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/section[3]/div[3]/nav/ul/li[5]/button')
            botao_proximo.click()
        print("\033[32m Foram encontradas "+ str(len(jobs_list)) +" vagas \033[m")
        self.lista_vagas['vaga'] = jobs_list
        self.lista_vagas['local'] = places_list

    def save_json(self, lista_vagas):
        json_data = json.dumps(lista_vagas)
        data = date.today()
        print("\033[32m Salvando dados em arquivo JSON \033[m")
        with open(f"vagas {data}.json", "w") as arquivo:
            arquivo.write(json_data)
    
    def check_interests(self, lista_vagas):
        vagas = lista_vagas['vaga']
        vagas_juazeiro = []
        vagas_dev = []
        for vaga in vagas:
            if 'Juazeiro do Norte' in vaga:
                vagas_juazeiro.append(vaga)
            if 'Desenvolvedor' in vaga or'Programador' in vaga or 'Programação' in vaga or 'Back-End' in vaga or 'Front-End' in vaga:
                vagas_dev.append(vaga)
        print(f"\033[32m Foram encontradas {len(vagas_juazeiro)} vagas em Juazeiro do norte: \033[m")
        for vaga in vagas_juazeiro:
            print(f"\033[33m {vaga} \033[m")
        print(f"\033[32m Foram encontradas {len(vagas_dev)} vagas na área dev: \033[m")
        for vaga in vagas_dev:
            print(f"\033[33m {vaga} \033[m")

GupyScrapper()