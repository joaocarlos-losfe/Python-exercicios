"""
    Teste Prático Python Maio de 2022 - Enttry Software
    candidato: João Carlos de Sousa Fé

    referencias (instalar todas pelo pip): 
        biblioteca BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import requests
from bs4 import BeautifulSoup
import json

def getMetas(url: str):
    response = requests.get(url)

    tag_property = []

    if response.status_code == 200:
        html_content = BeautifulSoup(response.content, "html.parser")
        #alguns vão aparecer com "null" devido ter "content" sem "name" ou ter "property" em vez do name
        for meta in html_content.find_all("meta"):
            tag_property.append({"name": meta.get("name"), "content": meta.get("content")})
                
        return json.dumps(tag_property, indent=4)

    else:
        print("não foi possivel acessar a url !")

    return None

if __name__ == "__main__":
    metas = getMetas("https://9to5linux.com/")

    if metas:
        print(metas)