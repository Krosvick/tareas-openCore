from asyncore import write
from venv import create
import bs4
import requests
import os

def read_links(file_name):
    links = []
    with open(file_name, 'r') as f:
        links = f.readlines()
    for i in range(len(links)):
        links[i] = (links[i])[:-2]
    #print(links)
    return links

def download_page(url):
    page = requests.get(url)
    return page

def get_links(page):
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        #print(link.get('href'))
        try:
            if link.get('href').find('https') != -1 and link.get('href') != '#':
                links.append(link.get('href'))
        except:
            print('sin links')
            break
    return links

def friendly_name(name):
    return name.replace('https://', '').replace('/', '').replace('.', '').replace('?', '').replace('|', '').replace('\\', '').replace('<', '').replace('>', '').replace(':', '').replace('"', '').replace('*', '').replace('=', '').replace('[', '').replace(']', '').replace(',', '')

def create_dir(directory, path):
    file_name = friendly_name(directory)
    completeName = os.path.join(path, file_name)
    if not os.path.exists(completeName):
        os.makedirs(completeName)

def write_page(link, path):
    url = download_page(link)
    #print(link)
    completeName = os.path.join(path, friendly_name(link) + '.html')
    with open(completeName , 'wb') as fd:
        fd.write(url.content)

links = read_links('C:/Users/gpall/Desktop/U/Analisis de Algoritmos/paginas.txt')
save_path = 'C:/Users/gpall/Desktop/U/Analisis de Algoritmos'
lista_paginas = []
for link in links:
    create_dir(link, save_path)
    write_page(link, save_path)
    lista_paginas.append(link)
    links1 = get_links(download_page(link))
    for i in links1:
        save_path = 'C:/Users/gpall/Desktop/U/Analisis de Algoritmos' + '/' + friendly_name(link)
        if i in lista_paginas:
            print('repetido profundidad 1')
            continue
        lista_paginas.append(i)
        print('\nprofundidad 1')
        print('página: ' + i)
        print('directorio: ' + save_path)
        write_page(i, save_path)
        create_dir(i, save_path)
        links2 = get_links(download_page(i))
        for j in links2:
            if j in lista_paginas:
                print('repetido profundidad 2')
                continue
            lista_paginas.append(j)
            save_path = 'C:/Users/gpall/Desktop/U/Analisis de Algoritmos' + '/' + friendly_name(link) + '/' + friendly_name(i)
            print('\nprofundidad 2')
            print('página: ' + j)
            print('directorio: ' + save_path)
            write_page(j, save_path)