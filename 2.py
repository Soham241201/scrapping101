# https://veterinariansusa.com/il/

import requests
import json
import logging as logger
import time
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

OUTPUT_FOLDER=r"C:\Users\Sohom\Desktop\projects\scrapping22222\results2.txt"

try :

    # url = 'https://veterinariansusa.com/il/addison'
    url = 'https://veterinariansusa.com/il/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = bs(response.content, 'html.parser')




    cities_list = soup.find_all('ul', {'class': 'cities_list'})
    city_links = cities_list[1].find_all('a')
    # print(city_links)

    for link in city_links[40:45]:
        city_name = link.text.strip()
        # city_url = link['href']
        url2 = 'https://veterinariansusa.com/il/' + city_name
        response = requests.get(url2, headers=headers)
        soup = bs(response.content, 'html.parser')

        name = soup.find('div', {'class': 'inside'}).div.h3.text.strip()
        phone = soup.find('div', {'class': 'inside'}).div.ul.li.a.text.strip()
        address = soup.find('div', {'itemprop': 'address'}).text
        print("done")
        
        with open(OUTPUT_FOLDER, 'a') as f: 
                    
                    # f.write(f'Zip: {j}\n')
                    f.write(f'Name: {name}\n')
                    # f.write(f'services-provided: \n')
                    # for k in final_data["services-provided"]:
                    #     f.write(f'{k}\n')
                    f.write(f'Address: {address}\n')
                    f.write(f'Phone number: {phone}\n')
                    f.write(f'\n')
                    


except requests.exceptions.ConnectionError as e:
            logger.error(f'Connection failed..')