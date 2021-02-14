

import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import re  # regular expression
import validators # pip install validators

css_links = []
page_links = []
own_links = []

max_depth = 1 # maximum level recursion
url = ''
includeAssets = False
def getAllPageLink( url, depth = 0, includeAssets = True ):
  source_code = requests.get( url )
  soup = BeautifulSoup(source_code.content, 'lxml')
  if includeAssets:
    for link in soup.findAll("link", rel="stylesheet"):
      if link not in css_links:
        css_links.append(link)
  for link in soup.find_all('a', href=True):
    href_link = str(link.get('href'))
    if validators.url(href_link):
      if href_link not in page_links:
        page_links.append(href_link)
        if depth < max_depth:
          getAllPageLink(href_link, depth + 1)
    else:
      if href_link not in own_links:
        own_links.append(href_link)

while(True):
  url = input('Enter url : ')
  if validators.url(url):
    break
  else:
    print('Invalid URL')
while(True):
  max_depth = input('Enter depth : ')
  if max_depth.isnumeric():
    max_depth = int(max_depth)
    break
  else:
    print('Not a number')
while(True):
  includeAssets = input('Include assets? (y/n) ')
  if includeAssets == "y":
    includeAssets = True
  break
  

getAllPageLink(url)

print('++++++++++++++++++++++++++++++++++++ ALL LINKS +++++++++++++++++++++++++++++++++++++')
for item in own_links:
  print(item)
for item in page_links:
  print(item)
for item in css_links:
  print(item)
print('++++++++++++++++++++++++++++++++++++ END +++++++++++++++++++++++++++++++++++++')





# print('done', data)
# def remove_duplicates(l): # remove duplicates and unURL string
#   for item in l:
#     match = re.search("(?P<url>https?://[^\s]+)", item)
#     if match is not None:
#       links.append((match.group("url")))


# for link in soup.find_all('a', href=True):
#   data.append(str(link.get('href')))
# flag = True
# remove_duplicates(data)
# while flag:
#   try:
#     for link in links:
#       for j in soup.find_all('a', href=True):
#         temp = []
#         source_code = requests.get(link)
#         soup = BeautifulSoup(source_code.content, 'lxml')
#         temp.append(str(j.get('href')))
#         remove_duplicates(temp)

#         if len(links) > 162: # set limitation to number of URLs
#           break
#         if len(links) > 162:
#           break
#         if len(links) > 162:
#           break
#   except Exception as e:
#     print(e)
#     if len(links) > 162:
#       break

# for url in links:
#   print(url)


# print('done', result.status_code)