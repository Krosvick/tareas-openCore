import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching the webpage: {str(e)}")
        return None

def clean_html(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Remove <script> and <style> tags from the soup
        for script in soup(['script', 'style']):
            script.extract()
        return soup.prettify()
    return None

def save_html(html, filename):
    if html:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html)
        print(f"HTML saved to {filename}")

if __name__ == "__main__":
    url = 'https://www.cooperativa.cl/noticias/pais/michelle-bachelet/bachelet-y-los-50-anos-el-ambiente-politico-esta-toxico/2023-09-04/161631.html'
    
    webpage_content = fetch_webpage(url)
    if webpage_content:
        cleaned_html = clean_html(webpage_content)
        if cleaned_html:
            save_html(cleaned_html, 'output.html')