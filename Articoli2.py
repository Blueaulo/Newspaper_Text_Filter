from bs4 import BeautifulSoup 
import requests
url = input()
source = requests.get(url)
soup = BeautifulSoup(source.text, "lxml")
raw_text = soup.find_all('p')
for article in raw_text:
    print(article.text)