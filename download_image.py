import json
import os
import random
import sys
import time
import requests
import logging

from bs4 import BeautifulSoup

#####
import io
from PIL import Image

def download_img_via_url(url):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    print(url)

    img_name = 'ur_images/' + url.split('/')[-1].replace('.jpg?',
                                                           '_') + '.png'

    response = requests.get(url, headers=headers, stream=True)
    response.encoding = response.apparent_encoding
    try:
        response.raise_for_status()
    except:
        pass
    ###########
    byte_stream = io.BytesIO(response.content)# 把请求到的数据转换为Bytes字节流

    roiImg = Image.open(byte_stream)    # Image打开Byte字节流数据创建一个空的Bytes对象

    imgByteArr = io.BytesIO()     # 创建一个空的Bytes对象

    roiImg.save(imgByteArr, format='PNG') # PNG就是图片格式

    imgByteArr = imgByteArr.getvalue()   # 这个就是保存的图片字节流
    #############
    
    if response.status_code != 200:
        fail_txt = open('fail_list.txt', 'a+')
        fail_txt.write(f'{url}\n')

    if not os.path.exists(img_name):
        with open(img_name, 'wb') as file:
            file.write(imgByteArr)
    print('saved img:'+img_name)


def download_img(url):
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

    image_list = soup.find_all(
        'div', attrs={'data-grname': 'not4'})

    image_url_list = []
    for image_item in image_list:
        image_url_list.append('https:'+image_item['data-src'].replace(".jpg","_4100x.jpg"))

    image_url_list = list(set(image_url_list))

    for image_url in image_url_list:
        download_img_via_url(image_url)
        time.sleep(random.randint(0, 5))


if __name__ == "__main__":
    os.makedirs('ur_images', exist_ok=True)
    logging.basicConfig(format='%(asctime)s %(message)s',filename='download.log', encoding='utf-8', level=logging.DEBUG)

    product_id_list = open('product_list.txt', 'r').readlines()

    for product_link in product_id_list:
        time.sleep(random.randint(1, 3))
        try:
            download_img(product_link[:-1])
        except:
            logging.error(sys.exc_info())
            raise NotImplementedError
        
    