import requests
from bs4 import BeautifulSoup
def inst(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.find("meta", attrs={"property": "og:image"})
        if meta_tag:
            image_url = meta_tag["content"]
            image_response = requests.get(image_url)
            with open(f"img.jpeg", "wb") as f:
                f.write(image_response.content)
            f.close()