# python-crawler
A crawler for image based on BeautifulSoup. Some other packages like **Selenuim** can also be used to mimic human behavior on explorer.  

**Step 1** 

Run `python category_scraper.py` to get category links from a website such as Hm Nike. It will generate a txt file named `category.txt` to save the results.

**Step 2**

Run `python item_list_scraper.py` to get product links. It will generate another txt file named `product_list.txt` based on `category.txt` in step 1.

**Step 3**

Run `python download_image.py` to download the images into local folder. 

**Step 4**

Use `remove_pics.py` to remove images which are not in right resolution.
