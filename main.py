from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://foodpro.ucr.edu/foodpro/shortmenu.asp?sName=University%20of%20California%2C%20Riverside%20Dining%20Services&locationNum=03&locationName=Glasgow&naFlag=1&_gl=1*10y1920*_ga*MjA1OTk2NTU1NS4xNjg0MTA3MzM1*_ga_S8BZQKWST2*MTY5OTM5MDc3Ni40OS4wLjE2OTkzOTA4MjQuMC4wLjA.*_ga_Z1RGSBHBF7*MTY5OTM5MDc3Ni40OS4wLjE2OTkzOTA4MjQuMC4wLjA."
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

breakfast_table = soup.find_all('table')[4]
breakfast_menu = breakfast_table.find_all('div', class_ = "shortmenurecipes")
breakfast_menu_names = [title.text.strip() for title in breakfast_menu]

lunch_table = soup.find_all('table')[21]
lunch_menu = lunch_table.find_all('div', class_ = "shortmenurecipes")
lunch_menu_names = [title.text.strip() for title in lunch_menu]

dinner_table = soup.find_all('table')[58]
dinner_menu = dinner_table.find_all('div', class_ = "shortmenurecipes")
dinner_menu_names = [title.text.strip() for title in dinner_menu]



for i in breakfast_menu_names:
    print(i)




