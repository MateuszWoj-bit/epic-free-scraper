import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

chrome_path = "./chromedriver.exe"
chrome_service = ChromeService(chrome_path)
driver = webdriver.Chrome(service=chrome_service)

url = "https://store.epicgames.com/pl/"
http = "https://store.epicgames.com"

driver.get(url)
driver.implicitly_wait(5)

html_code = driver.page_source

soup = BeautifulSoup(html_code, 'html.parser')

game_elements = [a for a in soup.find_all('a') if 'Bezpłatne gry' in a.get('aria-label', '')]

games_data = []

for game_element in game_elements:
    title = game_element.find('div', class_='css-n55ojx').text.strip()
    link = game_element['href']

    img_element = game_element.find('img', class_='css-174g26k')
    img_url = img_element['src'] if img_element else 'No Image Found'
  
    game_info = {
        'Title': title,
        'Link': f"{http}{link}",
        'Image URL': img_url
    }
    games_data.append(game_info)

    print(f"Title: {title}\nLink: {http}{link}\nImage URL: {img_url}\n")

with open('games_data.json', 'w', encoding='utf-8') as jsonfile:
    # Write the game data to the JSON file
    json.dump(games_data, jsonfile, ensure_ascii=False, indent=2)

driver.quit()
