import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")


def get_conversion_rate(target_currency, api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP'

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Error: Failed to connect to the internet.")
        return None

    if response.status_code == 200:
        data = response.json()
        # .get() returns None instead of crashing if the currency code doesn't exist
        return data["conversion_rates"].get(target_currency)
    else:
        print("Failed to get currency.")
        return None


def product_details(target_currency="KES"):
    url = 'https://books.toscrape.com/'

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Error: Failed to connect to the internet.")
        return []

    if response.status_code != 200:
        print("Failed to load the page.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    product_pods = soup.find_all('article', class_='product_pod')

    rate = get_conversion_rate(target_currency, api_key)
    # If we have no rate, we stop here instead of crashing on the maths below
    if rate is None:
        print(f"Could not get a rate for {target_currency}.")
        return []

    # One timestamp for the whole run, showing when the conversion happened
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Each book becomes one dictionary, and they all go into this list
    products = []
    for pod in product_pods:
        name = pod.h3.a.get('title')
        price_text = pod.find('p', class_='price_color').get_text(strip=True)
        price_clean = float(price_text.replace('£', ''))
        price_converted = round(price_clean * rate, 2)

        products.append({
            "Book name": name,
            "Price (GBP)": price_clean,
            f"Price ({target_currency})": price_converted,
            "Converted at": timestamp,
        })

    # Returning the list means the data can be reused later in the program
    return products


def main():
    currency = input("Enter a currency code (e.g. KES, USD, EUR) [KES]: ").strip().upper() or "KES"
    products = product_details(currency)

    if not products:
        return

    # A pandas DataFrame turns our list into a table
    df = pd.DataFrame(products)
    print(df.to_string(index=False))

    # Save the table to a CSV file
    df.to_csv("books_prices.csv", index=False)
    print("Saved to books_prices.csv")


if __name__ == "__main__":
    main()