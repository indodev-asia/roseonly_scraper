#!/usr/bin/env python3
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time
def scrape_roses_and_save_to_txt():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.rosesonly.com.au/occasion/all-flowers")
        time.sleep(8)
        content = page.content()
        soup = BeautifulSoup(content, 'html.parser')
        product_name_divs = soup.find_all('div', class_='prodName')
        product_price_divs = soup.find_all('div', class_='prodPrice')
        i = 0
        fp = open("log.txt", 'w')
        for product_name_div in product_name_divs:
            product_name = product_name_div.find('span').text.strip()   
            product_price = product_price_divs[i].text.strip()
            print(f"Product Name: {product_name}")
            if product_price.find(" ") != -1:
                ar = product_price.split(" ")
                product_price = ar[1]
            print(f"Product Price: {product_price}")
            fp.write( f"product name : {product_name}\n")
            fp.write( f"product price : {product_price}\n")
            fp.write('\n====================\n')
            i += 1
        fp.close()

scrape_roses_and_save_to_txt()   