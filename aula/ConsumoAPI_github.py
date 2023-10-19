import requests

print('Github user')

username = input('Usuário: ')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(data)
    print(f"Nome completo: {data['name']}")
    print(f'Localização: {data["localization"]}')
else:
    print("usario não encontrado")
