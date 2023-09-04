import requests
from bs4 import BeautifulSoup

url = 'https://www.cooperativa.cl/noticias/pais/michelle-bachelet/bachelet-y-los-50-anos-el-ambiente-politico-esta-toxico/2023-09-04/161631.html'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    #pretiffy and save the html
    with open('output.html', 'w') as file:
        file.write(soup.prettify())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
