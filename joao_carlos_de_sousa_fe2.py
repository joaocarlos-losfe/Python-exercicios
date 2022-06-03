"""
    Teste Prático Python Maio de 2022 - Enttry Software
    candidato: João Carlos de Sousa Fé

    referencias: 
        API de clima: https://openweathermap.org/
        API de CEP: https://apicep.com/api-de-consulta/
"""

import json
import requests

API_OPEN_WEATHER_KEY = "d1af9eb638a7a24e06f0889f9e2c6a0d" #e

def getApiData(api_url:str):
    response = requests.get(api_url)
    #print(f"request status code: {response.status_code}")
    if response.status_code == 200:
        return json.dumps(response.json())
    
    return None

def getTemperature(CEP:str):
    try:
        api_url_cep = f"https://ws.apicep.com/cep/{CEP}.json"
        cep_result = getApiData(api_url_cep)

        if cep_result and json.loads(cep_result)["status"] == 200:
            city = json.loads(cep_result)["city"].lower()
            
            api_url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_OPEN_WEATHER_KEY}&lang=pt_br&units=metric"
            weather_result = getApiData(api_url_weather)

            if weather_result and json.loads(cep_result)["status"] == 200:
                print(f"cidade: {city}")
                return json.loads(weather_result)["main"]["temp"]
            else:
                print('a API não encontrou a cidade')
        else:
            print("CEP invalido")
    except:
        pass
        
    return None

if __name__ == "__main__":
    temperature = getTemperature("95020-360")

    if temperature:
        print(f"temperatura: {temperature} °C")


