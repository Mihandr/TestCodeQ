import requests
from bs4 import BeautifulSoup as bs

def take_ip():
    url = "https://ifconfig.me/ip"
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    return soup