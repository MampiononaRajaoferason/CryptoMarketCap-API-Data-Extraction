# -*- coding: utf-8 -*-

# main.py
from api_extract import extract_cryptocurrency_data, KeyVal, url

#KeyVal = 'db605763-8ae7-41aa-989f-225d961020d7'

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
if __name__ == "__main__":
    # Get the API key from user input or some other source
    #user_api_key = KeyVal#input("Enter your CoinMarketCap API key: ")

    # Call the function with the API key
    extract_cryptocurrency_data(url, KeyVal)
