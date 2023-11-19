from openai import OpenAI
import os 
from bs4 import BeautifulSoup
import pandas as pd
import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)


#web scraper

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



def get_menu_items(weight, height, diet_plan):
  client = OpenAI(
      # defaults to os.environ.get("OPENAI_API_KEY")
      api_key="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",
  )
  food_list = menu_items
  
  completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    temperature = 0.8,
    max_tokens = 500,
  
    messages=[
              {"role": "system", "content": 'You are a concise health assistant helping the user maintain a healthy diet.'},
              {"role": "user", "content": f"Display a short list containing a personalized menu for the date: {date_string}. Write in a bulleted list format, a personalized meal plan for the user for each meal given the breakfast menu: {food_list[:13]}, the lunch menu: {food_list[14:43]}, and the dinner menu: {food_list[44:-1]}. Consider the user's weight (pounds):{weight} and height (inches): {height}, and diet plan: {diet_plan}. It should include the date. It shoudl include calories, protein, and fat for each food item and meal. Limit to up to three items per meal. Keep it concise and simple. No extra information is needed."},
      ]
      )
  
  return (completion.choices[0].message.content)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_meal_plan', methods=['POST'])
def generate_meal_plan():
    user_data = request.json  # Get user inputs from the POST request
    weight = user_data['weight']
    height = user_data['height']
    diet_plan = user_data['dietPlan']

    # Call your function and pass user inputs
    meal_plan = get_menu_items(weight, height, diet_plan)

    return jsonify(meal_plan)

if __name__ == "__main__":
     app.run(debug=True ,port=5000,use_reloader=False)

