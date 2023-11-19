# -*- coding: utf-8 -*-

# api_extract.py
import requests
from prettytable import PrettyTable

#create pretty table object

tableobj = PrettyTable() 
KeyVal = 'db605763-8ae7-41aa-989f-225d961020d7'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='




def extract_cryptocurrency_data(url, api_key):
    
    api_endpoint = url + api_key
    #api_endpoint+= KeyVal
    #api_endpoint
    
    json_data = requests.get(api_endpoint ).json()
    
    #if we want to use a parameters
    #json_data = requests.get(api_endpoint, params=parameters).json()
    
    cryptodata = json_data['data']
     
    for currency in cryptodata:
        #print(currency['name'],currency['quote'] )
        
        curr_name = currency['name']
        curr_price = currency['quote']['USD']['price']
        curr_change_1h = currency['quote']['USD']['percent_change_1h']
        curr_change_24h = currency['quote']['USD']['percent_change_24h']
        curr_change_7d = currency['quote']['USD']['percent_change_7d']
        curr_change_30d = currency['quote']['USD']['percent_change_30d']
        curr_change_60d = currency['quote']['USD']['percent_change_60d']
        curr_change_90d = currency['quote']['USD']['percent_change_90d']
        
        tableobj.add_row([curr_name, curr_price, curr_change_1h, curr_change_24h, curr_change_7d, curr_change_30d, curr_change_60d, curr_change_90d])
        tableobj.field_names = ["Currency Name", "Currency Price", "Currency 1h Change", "Currency 24h Change",  "Currency 7d Change", "Currency 30d Change", "Currency 60d Change", "Currency 90d Change" ]
        print('\n')
        
    print(tableobj)
    
    
    table_txt = tableobj.get_string()

    with open ('crypto_data.txt', 'w') as file:
        file.write(table_txt )



#if __name__ == "__main__":
    # Get the API key from user input or some other source
#    user_api_key =  KeyVal #input("Enter your CoinMarketCap API key: ")

    # Call the function with the API key
#    extract_cryptocurrency_data(url,user_api_key)
