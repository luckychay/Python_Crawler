from PIL import Image
import os
import sys
import logging 
 
def get_urllist():
    base = r'./test/'#这个是要清理的文件夹
    list = os.listdir(base)
    urllist = []
    for i in list:
        url = base + i
        urllist.append(url)
    return urllist
 
def get_imgSize(filename):
    img = Image.open(filename)
    imgSize = img.size
    print(imgSize)
 
    return imgSize
 
if __name__ == '__main__':
    file_list = get_urllist()
    logging.basicConfig(format='%(asctime)s %(message)s',filename='remove.log', encoding='utf-8', level=logging.INFO)
    logging.info('start removing low resolution pics...')
    for a in file_list:
        try:
            imgSize = get_imgSize(a)
            maxSize = max(imgSize)
            minSize = min(imgSize)
            logging.info(a+'  maxSize: '+str(maxSize)+' minSize: '+str(minSize))
            if (maxSize<900 and minSize<900 and (minSize+minSize)<1800):
                try:
                    os.remove(a)
                    logging.info("removed resolution less than 900x900：%s" % a)
                except:
                    logging.error(sys.exc_info())
            else:
                pass
        except:
            os.remove(a)
    logging.info('end removing low resolution pics.')