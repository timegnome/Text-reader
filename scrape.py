from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
import pandas as pd
import time
import requests
import sys

def boxnovel(book,browser):
	try:
		seperator = '-'
		book = seperator.join(book.split(' '))
		url = f"https://boxnovel.com/novel/{book}/"
		browser.visit(url)
		if requests.get(url).status_code == 404:
			browser.driver.close()
			sys.exit()
		time.sleep(1)
	except:
		print('Hwelp mwe! I bwroke.')
		try:
			browser.driver.close()
		except:
			sys.exit()
		sys.exit()
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')
	container = soup.find_all("div", {"class": "summary-content"})
	author = container[3].find("div", {"class": "author-content"}).find_all('a')


	# In[ ]:


	with open(f'{book}.txt', 'w',encoding ='utf8') as out:
		chapter = 1
		seperator = ', '
		author_text = seperator.join([author[0].text, author[1].text])
		BookName = ' '.join([word.capitalize() for word in book.split('-')])
		out.write('\t\t\t\t\t\t\t\t\t\t\t\t'+BookName+'\n\n')
		out.write('\t\t\t\t\t\t\t\t\t\t\tAuthor:'+author_text+'\n\n\n')
		
		try:
			# url = f"https://boxnovel.com/novel/{book}/chapter-{chapter}"
			chapter_1.click()
			# browser.visit(url)
			time.sleep(5)
			while True:
				try:
					html = browser.html
					soup = BeautifulSoup(html, 'html.parser')
					time.sleep(5)
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
						out.write(text+'\n\n')
					try :
						next_page = browser.driver.find_element_by_class_name('next')
						next_page.click()
					except :
						break
				except KeyboardInterrupt:
					print ('\nPausing...  (Hit ENTER to continue, type quit to exit.)')
					try:
						response = input()
						if response == 'quit':
							break
						print ('Resuming...')
					except KeyboardInterrupt:
						print ('Resuming...')
						continue
		except:
			print('Fwalure')
	browser.driver.close()

def wuxiaco(book,browser):

	try:
		seperator = '-'
		book = seperator.join(book.split(' '))
		url = f"https://www.wuxiaworld.co/{book}/"
		browser.visit(url)
	#     if requests.get(url).status_code == 404:
	#         browser.driver.close()
	#         sys.exit()
		time.sleep(10)
	except:
		print('Hwelp mwe! I bwroke.')
		try:
			browser.driver.close()
		except:
			print('nothing')
	#         sys.exit()
	#     sys.exit()
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')
	container = soup.find_all("div", {"class": "person-info"})
	author = container[1].find("div", {"class": "author"}).find_all('span')[1].text
	chapter_list = soup.find_all("ul", {"class": "chapter-list"})
	chapter_1 = browser.driver.find_element_by_class_name("chapter-item")

	# In[ ]:


	with open(f'{book}.txt', 'w',encoding ='utf8') as out:
		seperator = ', '
		BookName = ' '.join([word.capitalize() for word in book.split('-')])
		out.write('\t\t\t\t\t\t\t\t\t\t\t\t'+BookName+'\n\n')
		out.write('\t\t\t\t\t\t\t\t\t\t\t Author:'+author+'\n\n\n')

		try:
			# url = f"https://boxnovel.com/novel/{book}/chapter-{chapter}"
			chapter_1.click()
			# browser.visit(url)
			time.sleep(5)
			while True:
				try:
					html = browser.html
					soup = BeautifulSoup(html, 'html.parser')
					time.sleep(5)
					try:
						container = soup.find_all("div", {"class": "chapter-entity"})
						title = soup.find_all("h1", {"class": "chapter-title"})[0].text
						for br in container[0].find_all("br"):
							br.replace_with("\n")
						chapter_text =re.sub('((\\t)*(\\n)*[\w ]* https:[/\w\.\- ]*)', '\n', container[0].text)
					except:
						print('swomethwing bwroke mwe')
						break
					out.write('-----------------------------------------'+title+'-----------------------------------------\n\n')
					out.write(chapter_text)
					try :
						next_page = browser.driver.find_element_by_class_name('next')
						browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_page)
						next_page.click()
					except :
						break
				except KeyboardInterrupt:
					print ('\nPausing...  (Hit ENTER to continue, type quit to exit.)')
					try:
						response = input()
						if response == 'quit':
							break
						print ('Resuming...')
					except KeyboardInterrupt:
						print ('Resuming...')
						continue
		except:
			print('Fwalure')
	browser.driver.close()