import requests
import re
from bs4 import BeautifulSoup as bs


url = 'http://www.7h365.com/plugin.php?id=votes%3Alist&actid=180page%3D4&page='
person_page_url = 'http://www.7h365.com/plugin.php?id=votes:view&appid='

vote_list_current_page = 1
vote_list_page_count = 4
while vote_list_current_page <= int(vote_list_page_count):
    current_page = requests.get(url + str(vote_list_current_page))
    current_page.encoding = 'utf-8'
    soup = bs(current_page.text, 'html.parser')
    person_id_urls = soup.select('.inside_right_photo')[0].select('.c_b_t_ls')
    print(person_id_urls)
    for person_id_url in person_id_urls:
        person_id = re.findall('\d+', person_id_url.attrs.get('href'))[0]
        person_page = requests.get(person_page_url + person_id)
        person_page.encoding = 'utf-8'
        person_page_soup = bs(person_page.text, 'html.parser')
        person_infos = person_page_soup.select('.clearfix')[2].select('li')
        for person_info in person_infos:
            print(person_info.text)
        if len(person_page_soup.select('.jianjie')) > 0 :
            print('自荐综述')
            for item in person_page_soup.select('.jianjie'):
                print(item.text)
        if len(person_page_soup.select('.art-title')) > 0:
            print('参评报告')
            for item in person_page_soup.select('.art-title'):
                print(item.text)
        print('**************************************************************')
    vote_list_current_page += 1