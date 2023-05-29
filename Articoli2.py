import re
from bs4 import BeautifulSoup
import requests

url = input("Enter the URL of the webpage you want to scrape: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
paragraphs = soup.find_all('p')

print('-------------------')
for paragraph in paragraphs:
    text = paragraph.text.strip()
    if text:
        formatted_text = re.sub(r'\.(\s|$)', '.\n', text)
        print(formatted_text)

input("Press enter to close the program")
