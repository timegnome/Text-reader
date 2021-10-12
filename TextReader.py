#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from scrape import *
# import base64, os


# In[ ]:


executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# book_name = 'release that witch'
book_name = input('Please enter the book_name:  ')
website = input('Select website to scrape from: BN, Other:  ').lower()

# In[ ]:

if website == 'bn':
	book_name = book_name.lower()
	boxnovel(book_name,browser)
else:
	wuxiaco(book_name,browser)
