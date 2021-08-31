import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
}

url = "http://www.reddit.com/r/Waifu"
response = requests.get(url, headers=HEADERS)


soup = BeautifulSoup(response.content, "html.parser")

soup.prettify
images = soup.find_all("img", attrs={"alt": "Post image"})
number = 0
for image in images:
    image_src = image["src"]
    print(image_src)
    number += 1