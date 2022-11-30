from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions


import time

baseURL = "https://opensea.io"
urls= []

opts = ChromeOptions()
opts.add_argument("--window-size=2024,1080")

browser = webdriver.Chrome("./chromedriver", options=opts)

def append_to_urls(urls_):
	for result in urls_:
	        link = result["href"]
	        if link not in urls and "collection" in link:
	        	urls.append(link)



url = "https://opensea.io/rankings/trending"
browser.get(url)
soup = BeautifulSoup(browser.page_source,"html.parser")
results = soup.findAll('a', {'class':"sc-1f719d57-0"})
append_to_urls(results)


SCROLL_PAUSE_TIME = 1

# Get scroll height
height_to_scroll = 1080
while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, {});".format(height_to_scroll))
    height_to_scroll += 1080
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    soup = BeautifulSoup(browser.page_source,"html.parser")
    results = soup.findAll('a',{'class':"sc-1f719d57-0"})
    append_to_urls(results)
    new_height = browser.execute_script("return 1080")
    print(browser.execute_script("return window.scrollY") , browser.execute_script("return document.body.scrollHeight")) 
    if browser.execute_script("return window.scrollY") == 8319:
        break

print(urls)
print(len(urls))

weburls=[]

for li in urls:
	browser.get(baseURL+li)
	soup = BeautifulSoup(browser.page_source,"html.parser")
	results = soup.findAll('path',{'d':"M2 12C2 6.48 6.47 2 11.99 2C17.52 2 22 6.48 22 12C22 17.52 17.52 22 11.99 22C6.47 22 2 17.52 2 12ZM15.97 8H18.92C17.96 6.35 16.43 5.07 14.59 4.44C15.19 5.55 15.65 6.75 15.97 8ZM12 4.04C12.83 5.24 13.48 6.57 13.91 8H10.09C10.52 6.57 11.17 5.24 12 4.04ZM4 12C4 12.69 4.1 13.36 4.26 14H7.64C7.56 13.34 7.5 12.68 7.5 12C7.5 11.32 7.56 10.66 7.64 10H4.26C4.1 10.64 4 11.31 4 12ZM5.08 16H8.03C8.35 17.25 8.81 18.45 9.41 19.56C7.57 18.93 6.04 17.66 5.08 16ZM5.08 8H8.03C8.35 6.75 8.81 5.55 9.41 4.44C7.57 5.07 6.04 6.34 5.08 8ZM12 19.96C11.17 18.76 10.52 17.43 10.09 16H13.91C13.48 17.43 12.83 18.76 12 19.96ZM9.5 12C9.5 12.68 9.57 13.34 9.66 14H14.34C14.43 13.34 14.5 12.68 14.5 12C14.5 11.32 14.43 10.65 14.34 10H9.66C9.57 10.65 9.5 11.32 9.5 12ZM14.59 19.56C15.19 18.45 15.65 17.25 15.97 16H18.92C17.96 17.65 16.43 18.93 14.59 19.56ZM16.5 12C16.5 12.68 16.44 13.34 16.36 14H19.74C19.9 13.36 20 12.69 20 12C20 11.31 19.9 10.64 19.74 10H16.36C16.44 10.66 16.5 11.32 16.5 12Z"})
	if len(results) > 0:
		weburls.append(results[0].parent.parent.parent.parent.parent["href"])
		print(results[0].parent.parent.parent.parent.parent["href"])
	
print(weburls)
print(len(weburls))

