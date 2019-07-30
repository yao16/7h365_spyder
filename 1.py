import requests
from bs4 import BeautifulSoup as bs
import re

#url = 'http://www.7h365.com/plugin.php?id=votes%3Alist&actid=183&page=4'
url = 'http://www.7h365.com/plugin.php?id=votes:view&appid=4751'
url = 'http://www.7h365.com/plugin.php?id=votes:view&appid=5801'
page = requests.get(url)
page.encoding = 'utf-8'

soup = bs(page.text, 'html.parser')

print(soup.select('.clearfix')[2].select('li')[0].text)
print(soup.select('.clearfix')[2].select('li')[1].text)
print(soup.select('.clearfix')[2].select('li')[2].text)
print(soup.select('.clearfix')[2].select('li')[3].text)
print(soup.select('.clearfix')[2].select('li')[4].text)
print(soup.select('.clearfix')[2].select('li')[5].text)
print('自荐综述', soup.select('.jianjie')[0].text)
print('参评报告', soup.select('.art-title'))
