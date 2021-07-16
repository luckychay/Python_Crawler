import json
import os
import random
import time
import sys
import logging

import requests
from bs4 import BeautifulSoup


def get_category_list(url):
    headers = {
        'sec-ch-ua':
        '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    }

    r = requests.get(url, headers=headers)

    html_txt = open('html.txt', 'w+')
    html_txt.write(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')

    hidden_category_list = soup.find_all(
        'ul',
        attrs={
            'class':
            'nt_menu in_flex wrap al_center'
        })
    # category_txt = open('category.txt', 'w+')
    # category_txt.write(hidden_category)

    # category_list = soup.find_all(
    #     'li',
    #     attrs={
    #         'class': 'menu__item ui-menu-item',
    #         'role': 'presentation'
    #     })

    link_list = []
    for category in hidden_category_list:
        category_link_all = category.find_all('a')
        for category_link in category_link_all:
            link = category_link["href"]
            if link == '#':
                continue
            if 'kids' in link:
                continue
            for i in range(1,70):
                link_list.append(link+'?page='+str(i))

    link_list = list(set(link_list))
    link_list.sort()
    category_txt = open('category.txt', 'a+')
    for link in link_list:
        category_txt.write(f'{link}\n')


if __name__ == "__main__":

    url = 'https://urbanrevivo.com/'
    logging.basicConfig(format='%(asctime)s %(message)s',filename='category.log', encoding='utf-8', level=logging.DEBUG)

    try:
        get_category_list(url)
    except:
        logging.error(sys.exc_info())