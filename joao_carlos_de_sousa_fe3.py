"""
    Teste Prático Python Maio de 2022 - Enttry Software
    candidato: João Carlos de Sousa Fé

    referencias (instalar todas pelo pip): 
        biblioteca BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        biblioteca openpyxl: https://openpyxl.readthedocs.io/en/stable/
"""

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

def save_to_xls(data: dict, fileName:str):
    work_book = Workbook()
    sheet = work_book.active
    sheet.title = fileName.removesuffix(".xls")

    sheet["A1"] = "link"
    sheet["B1"] = "actual time"

    sheet.column_dimensions["A"].width = 100
    sheet.column_dimensions["B"].width = 40
 
    LINE = 3

    for link, current_time, in data.items():
        sheet[f"A{LINE}"] = link
        sheet[f"B{LINE}"] = current_time
        LINE += 1
    
    work_book.save(fileName)


def recursive_get_link(url:str, depth:int, links:dict):
    if depth < 0:
        return

    response = requests.get(url)
    if response.status_code != 200: 
        return

    page_html = BeautifulSoup(response.content, "html.parser")
    
    for a in page_html.find_all("a"):
        href = a.get("href")
        
        if  str(href).startswith("http") and href not in links.keys():
            current_time = datetime.now().strftime("%H:%M:%S.%f")
            links[href] = current_time
            print(href)
            recursive_get_link(href, depth-1, links)

def getLinks(URL:str, depth:int, fileName:str):
    links = {}
    print("capturando links...")
    recursive_get_link(URL, depth, links)
    
    print("gerando arquivo...")
    save_to_xls(links, fileName)

    print("finalizado")

    return links
                                
if __name__ == "__main__":
    getLinks("https://enttry.com.br/contato", 1, "linksEnttry.xls")