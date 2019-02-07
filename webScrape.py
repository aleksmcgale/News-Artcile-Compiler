import requests
import re
from bs4 import BeautifulSoup


def get_website_text(link):
    html = requests.get(link).text
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.decompose()
    txt = soup.get_text().strip()
    "".join(txt.split())
    txt = re.sub(r"\s+", " ", txt)
    return txt


if __name__ == '__main__':
    link = "https://discover.rbcroyalbank.com/navigating-canadas-health-care-system-while-you-wait-for-" \
           "your-health-card/?_ga=2.206394451.1792650953.1548987950-143445113.1547152928"
    t = get_website_text(link)