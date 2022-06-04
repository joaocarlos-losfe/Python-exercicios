"""
    Teste Prático Python Maio de 2022 - Enttry Software
    candidato: João Carlos de Sousa Fé

    referencias: 
        biblioteca BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        biblioteca openpyxl: https://openpyxl.readthedocs.io/en/stable/
"""

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

def save_to_xls(data: dict, fileName):
    work_book = Workbook()
    sheet = work_book.active
    sheet.title = fileName.removesuffix(".xls")

    sheet["A1"] = "link"
    sheet["B1"] = "actual time"

    sheet.column_dimensions["A"].width = 100
    sheet.column_dimensions["B"].width = 40
 
    line = 3

    for link, current_time, in zip(data.keys(), data.values()):
        sheet[f"A{line}"] = link
        sheet[f"B{line}"] = current_time
        line += 1
    
    work_book.save(fileName)


def recursive_get_link(url:str, depth:int, links):
    if depth < 0:
        return

    response = requests.get(url)
    if response.status_code != 200: 
        return

    page_html = BeautifulSoup(response.content, "html.parser")
    current_time = str(datetime.now().strftime("%H:%M:%S.%f"))
  
    for a in page_html.find_all("a"):
        href = a.get("href")

        if  str(href).startswith("http") and href not in links.keys():
            links[href] = current_time
            print(href)
            recursive_get_link(href, depth-1, links)

def getLinks(URL:str, depth:int, fileName:str):
    links = {}

    recursive_get_link(URL, depth, links)
    save_to_xls(links, fileName)

    return links
                                
if __name__ == "__main__":
    getLinks("https://enttry.com.br/contato", 3, "linksEnttry.xls")