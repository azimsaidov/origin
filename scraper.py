from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://foodpro.ucr.edu/foodpro/shortmenu.asp?sName=University+of+California%2C+Riverside+Dining+Services&locationNum=03&locationName=Glasgow&naFlag=1&WeeksMenus=This+Week%27s+Menus&myaction=read&dtdate=11%2F20%2F2023"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

date_element = soup.find('div', class_='shortmenutitle')
date_string = date_element.text.split('Menus for ')[1].strip()

##Everything above this line is good!

menu_menu = soup.find('div', class_='shortmenumeals')

menu_items = soup.find_all('div', class_='shortmenurecipes')
#get only the text in breakfast_items
menu_items = [item.text for item in menu_items]


#print menu_items to see what it looks like
for item in menu_items:
    print(item)






