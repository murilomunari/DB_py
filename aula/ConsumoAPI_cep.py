import requests

cep = "095.41-520"

cep = cep.replace("-", "").replace(".", "")

if len(cep) ==8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)
    print(requisicao)

    dic_requisicao = requisicao.json()
    print(dic_requisicao)

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    print(f'cidade: {cidade}')
    print(f'estado: {uf}')
    print(f'bairro: {bairro}')
else:
    print('cep invalido')