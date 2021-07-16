import json
import os
import random
import re
import sys
import time
import logging

import requests
from bs4 import BeautifulSoup


def get_item_list(url):
    headers = {
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    }

    r = requests.get(url, headers=headers)

    html_txt = open('html.txt', 'w+')
    html_txt.write(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')

    product_list = soup.find_all('div',{'class':'product-image pr oh lazyload'})

    url_list = []
    for product in product_list:
        product_link = product['data-include']
        product_link = product_link.split('?')[0]
        url = f'https://urbanrevivo.com'+product_link
        url_list.append(url)

    url_list = list(set(url_list))
    url_list.sort()

    url_txt = open('product_list.txt', 'a+')
    for url in url_list:
        url_txt.write(f'{url}\n')


if __name__ == "__main__":
    category_list = open('category.txt', 'r').readlines()
    logging.basicConfig(format='%(asctime)s %(message)s',filename='item.log', encoding='utf-8', level=logging.DEBUG)

    for category_url in category_list:
        try:
            get_item_list(category_url[:-1])
        except:
            logging.error(sys.exc_info())
        time.sleep(random.randint(1, 3))
