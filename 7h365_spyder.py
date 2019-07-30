import requests
import re
from bs4 import BeautifulSoup as bs


url = 'http://www.7h365.com/plugin.php?id=votes:fxsapply'
page = requests.get(url)
page.encoding = 'utf-8'

soup = bs(page.text, 'html.parser')
vote_list_pages = {}

for item in soup.select('.applist')[2].select('li'):
    sub_url = 'http://www.7h365.com/plugin.php?id=votes%3Alist&actid=' + item.select('a')[0].attrs.get('href')[-3:] + 'page='
    sub_title = item.select('a')[0].text
    vote_list_pages[sub_title] = sub_url
#    print(sub_title, sub_url)


for item in vote_list_pages.items():
    #print(item[0], item[1])
    vote_list_url = item[1]
    vote_list_current_page = 1
    vote_list_page = requests.get(vote_list_url + str(vote_list_current_page))

    vote_list_page.encoding = 'utf-8'
    vote_list_soup = bs(vote_list_page.text, 'html.parser')
    vote_list_page_count = 1
    page_count_str = vote_list_soup.select('.inside_right_page')[0].select('span')
    if len(page_count_str) > 0:
        vote_list_page_count = re.findall('\d+', page_count_str[0].text)[0]
    print(vote_list_page_count)

    print(item[0])
    while vote_list_current_page <= int(vote_list_page_count):
        vote_list_page = requests.get(vote_list_url + str(vote_list_current_page))
        print(vote_list_url + str(vote_list_current_page))
        vote_list_page.encoding = 'utf-8'
        vote_list_soup = bs(vote_list_page.text, 'html.parser')

        vote_list_current_page += 1
