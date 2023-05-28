from bs4 import BeautifulSoup 
import requests
source = requests.get("https://nascecresceignora.it/citadel-amazon-rinnova-la-serie-dei-fratelli-russo-per-una-seconda-stagione/")
soup = BeautifulSoup(source.text, "lxml")
raw_text = soup.find_all('p')
for article in raw_text:
    print(article.text)