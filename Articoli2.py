from bs4 import BeautifulSoup 
import requests
url = input("Put your link here: ")
source = requests.get(url)
soup = BeautifulSoup(source.text, "lxml")
raw_text = soup.find_all('p')
print ('-------------------')
for article in raw_text:
    print(article.text)
input("Press enter to close program")