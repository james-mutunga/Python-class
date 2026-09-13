# These are our import module functons to allow access to the web browser for requests and threading.

import webbrowser
import requests
import threading
from bs4 import BeautifulSoup

# This is to import our .env so that we can access the "EXCHANGE_API_KEY"
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")

# I started by creating my conversion rate function.
def get_conversion_rate(target_currency, api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP'

# This is my error handling using try/except in the case of a failed connection
    try:
        response = requests.get(url)
    # The except function here creates a request exception that will allow us to print our error message if "respons = requests.get(url)" doens't run
    except requests.exceptions.RequestException:
        print("Error: Failed to connect to the internet.")
        # We return none to stop the program
        return None

    if response.status_code == 200:
        # response.json() here converts the code into readable python for later use in the program
        data = response.json()
        rate = data["conversion_rates"][target_currency]
        return rate
    else:
        print("Failed to get currency.")

# This is my product_details function that will allow me to scrape both the names and the prices of each product; in this case each book and its price in pounds.
def product_details():
    url = 'https://books.toscrape.com/'

    try:
            response = requests.get(url)
    except requests.exceptions.RequestException:
            print("Error: Failed to connect to the internet.")
            return None

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # All book names and prices are included in the 'product_pod' div (article) of the website.
        product_pods = soup.find_all('article', class_='product_pod')

        # This is our rate which we will use later on
        rate = get_conversion_rate("KES", api_key)

        # Here i have the names of each variable that i'll be using. the names will have each name of the book, prices will hold its original price, cleaned_prices will hold each cleaned versions of the prices (without the £).
        names = []
        prices = []
        cleaned_prices = []
        converted_prices = []

        # This is my for loop that will allow me to get the exact name and exact price for my books.
        for pod in product_pods:
            # The name of my books are in "product_pod" under "h3" and wrapped around in an href" if we add "get('title)" i should be able to get the exact name
            name = pod.h3.a.get('title')
            # strip=True here will help us to strip any trailing whitespaces. in this case we have none.
            price_text = pod.find('p', class_='price_color').get_text(strip=True)
            # Here we are cleaning the price_text by removing the pound sign
            price_clean = float(price_text.replace('£', ''))
            # Here we are introducing price_converted where we will multiply the clean price by the current rate
            price_converted = price_clean * rate
            # Now we will append each results; names and prices into the lists we introduced
            names.append(name)
            prices.append(price_text)
            cleaned_prices.append(price_clean)
            converted_prices.append(price_converted)
            # This will give us the name of the book, its price in GDP and its price in Kes
            print(f"Book name: {name}, Book price in GBP: {price_clean}, Book price in KES: {price_converted:.2f}")

product_details()