import requests
from bs4 import BeautifulSoup

url = 'https://www.cooperativa.cl/noticias/pais/michelle-bachelet/bachelet-y-los-50-anos-el-ambiente-politico-esta-toxico/2023-09-04/161631.html'

response = requests.get(url, timeout=5)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove <script> tags from the soup
    for script in soup(['script' , 'style']):
        script.extract()

    # Save the modified HTML
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

