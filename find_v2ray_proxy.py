import requests
from bs4 import BeautifulSoup
import re

web_content = requests.get('https://www.mibei77.com/')

web_content.encoding=web_content.apparent_encoding

html_content = BeautifulSoup(web_content.content,'html.parser')

date_pattern = re.compile(r'https://www.mibei77.com/2024/06/\d{8}')

links = html_content.find_all('a',href=True)

real_link = [link['href'] for link in links if date_pattern.match(link['href'])]

first_link = real_link[0]

first_link_open = requests.get(first_link)

first_link_content = BeautifulSoup(first_link_open.content, 'html.parser')

text_content = first_link_content.text

nice_link = re.findall(r'https?://\S+\.txt', text_content)

for site1 in nice_link:
    print(site1)

open_url = requests.get('https://www.fuye.fun/')

open_url.encoding = open_url.apparent_encoding

parser_content = BeautifulSoup(open_url.content, 'html.parser')

url_format = re.compile(r'https://www.fuye.fun/2024/06/\d{7}')

hreflink = parser_content.find_all('a', href=True)

site_urls = [link2['href']for link2 in hreflink if url_format.match(link2['href'])]

site2_first_link = site_urls[0]

open_site2 = requests.get(site2_first_link)

open_site2.encoding = open_site2.apparent_encoding

site2_content = BeautifulSoup(open_site2.content, 'html.parser')

site2_content_text = site2_content.text

site2_nice_link = re.findall(r'https?://\S+\.txt', site2_content_text)

for site2 in site2_nice_link:
    print(site2)