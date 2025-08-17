import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Example: get all links
links = [a['href'] for a in soup.find_all('a', href=True)]
# print(links)
print(f"requests - {response.__getattribute__}")
