

API_KEY = '639d50780031bb94a42a33ddf2cee2d2'

from requests import get 
from json import dumps

API_KEY = input("Insira sua key para utilizar a API: ")
repositorio = input("Digite o repositorio a ser consultado: ")


dados = []
with open(repositorio , 'r', encoding='UTF-8') as x:
    for i in x.readlines():

        i = i.replace('\n','').replace(' ','') 
        modelo1 = i.split(',') 
        dados.append(modelo1) 

for informacoes in dados:    
   
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={informacoes[3]}&lon={informacoes[2]}&appid={API_KEY}'   
    resposta = get(url)
    print(resposta.text)

    if resposta.status_code == 200:
        print(f'Criando repositorio: {informacoes[0]}.json')
        with open(informacoes[0] + '.json', 'w', encoding='UTF-8') as repositorio:
            dadosjson = dumps({informacoes[1]:resposta.json()}, indent=4) 
            repositorio.write(dadosjson)
    else:
        print(f'Erro ao consultar as informações para: {informacoes}')