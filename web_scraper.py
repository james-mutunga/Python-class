import webbrowser
import requests
import threading
from bs4 import BeautifulSoup

def product_details():
    url = 'https://books.toscrape.com/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        product_pods = soup.find_all('article', class_='product_pod')

        names = []
        prices = []
        for pod in product_pods:
            name = pod.h3.a.get('title')
            price_text  = pod.find('p', class_='price_color').get_text(strip=True)
            price_clean = float(price_text.replace('£', ''))
            # This deletes the £ sign
            names.append(name)
            prices.append(price)
            print(f"{name} + {price}")
            

product_details()

