#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
import pandas as pd
import time
import requests
# import base64, os


# In[ ]:


executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


book_name = 'release that witch'
book_name = input()


# In[ ]:


try:
    seperator = '-'
    book_name = seperator.join(book_name.split(' '))
    url = f"https://boxnovel.com/novel/{book_name}/"
    browser.visit(url)
    if requests.get(url).status_code == 404:
        exit()
    time.sleep(1)
except:
    print('Welp me I broke')
    exit()
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
container = soup.find_all("div", {"class": "summary-content"})
author = container[3].find("div", {"class": "author-content"}).find_all('a')


# In[ ]:


with open(f'{book_name}.txt', 'w',encoding ='utf8') as out:
    chapter = 1
    seperator = ', '
    author_text = seperator.join([author[0].text, author[1].text])
    BookName = ' '.join([word.capitalize() for word in book_name.split('-')])
    out.write('\t\t\t\t\t\t\t\t\t\t\t\t'+BookName+'\n\n')
    out.write('\t\t\t\t\t\t\t\t\t\t\t\t\t Author:'+author_text+'\n\n\n')
    while True:
        try:
            url = f"https://boxnovel.com/novel/{book_name}/chapter-{chapter}"
            chapter +=1
            browser.visit(url)
            time.sleep(5)
            
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            try:
                container = soup.find_all("div", {"class": "read-container"})
                text_left = container[0].find_all("div", {"class": "text-left"})
                chp_title = text_left[0].find_all("p")[0].text
                pgraphs = text_left[0].find_all("p")
            except:
                print('swomethwing bwroke mwe')
                break
            pgraphs.pop(0)
            chapter_text = [p.text for p in pgraphs]

            out.write('-----------------------------------------'+chp_title+'-----------------------------------------\n\n')
            for text in chapter_text:
                out.write('\t\t'+text+'\n\n')
            try :
                next_page = browser.driver.find_element_by_class_name('next_page')
                next_page.click()
            except :
                break
        except KeyboardInterrupt:
            print '\nPausing...  (Hit ENTER to continue, type quit to exit.)'
            try:
                response = raw_input()
                if response == 'quit':
                    break
                print 'Resuming...'
            except KeyboardInterrupt:
                print 'Resuming...'
                continue
    browser.driver.close()

