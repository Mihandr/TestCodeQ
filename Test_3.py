import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

url = "https://greenatom.ru"
html = requests.get(url, headers={'User-Agent': UserAgent().chrome})
soup = bs(html.text, 'html.parser')

# 1 вопрос
list_tags = []
for child in soup.recursiveChildGenerator():
    if child.name not in list_tags and child.name is not None:
        list_tags.append(child.name)

print(len(list_tags))

# 2 вопрос
list_tags_with_attrs = []
n = 0

for tag in list_tags:
    find_tags = soup.find_all(tag)
    for check_tag in find_tags:
        if check_tag.attrs:
            list_tags_with_attrs.append(tag)
            break

print(len(list_tags_with_attrs))
