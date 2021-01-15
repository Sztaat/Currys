import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
import time
import winsound
 
now = datetime.now()

while True:
	try:
		page_url = 'https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/gigabyte-geforce-rtx-3060-ti-8-gb-eagle-oc-graphics-card-10219306-pdt.html'
		page = requests.get(page_url)
		soup = BeautifulSoup(page.content, 'html.parser')
		wynik = soup.find('li', class_ = "nostock")
		print(now.strftime("%d/%m/%Y, %H:%M"),"Dostepnosc GIGABYTE GeForce RTX 3060 Ti 8 GB EAGLE OC -",wynik.text)

	except Exception:
		print(now.strftime("%d/%m/%Y, %H:%M"),"Dostepnosc GIGABYTE GeForce RTX 3060 Ti 8 GB EAGLE OC - Prawdopodobnie dostepny")
		winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
		winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
		winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
		break

	try:
		page_url = 'https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/gigabyte-geforce-rtx-3060-ti-8-gb-gaming-oc-graphics-card-10219305-pdt.html'
		page = requests.get(page_url)
		soup = BeautifulSoup(page.content, 'html.parser')
		wynik = soup.find('li', class_ = "nostock")
		print(now.strftime("%d/%m/%Y, %H:%M"),"Dostepnosc GIGABYTE GeForce RTX 3060 Ti 8 GB GAMING OC -",wynik.text)
		
	except Exception:
		print(now.strftime("%d/%m/%Y, %H:%M"),"GIGABYTE GeForce RTX 3060 Ti 8 GB GAMING OC - Prawdopodobnie dostepny")
		winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
		winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
		winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
		break

	time.sleep(3600)	

		



