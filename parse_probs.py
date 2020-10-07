import re
import requests
from bs4 import BeautifulSoup
import os


def get_prob_set(href):
    url = 'http://noi-test.zzstep.com' + href
    rsp = requests.get(url)
    soup = BeautifulSoup(rsp.text)
    return soup.find_all('a', href=re.compile(r'contest/0x'))


def parse_prob(url):
    rsp = requests.get(url)
    soup = BeautifulSoup(rsp.text)
    res = soup.find_all('pre')
    return res[0].get_text(), res[1].get_text()


def main():
    url = 'http://noi-test.zzstep.com/contest?type=1'
    rsp = requests.get(url)
    soup = BeautifulSoup(rsp.text)
    links = soup.find_all('a', href=re.compile(r'contest/0x'))
    for link in links:
        prob_links = get_prob_set(link['href'])
        for prob_link in prob_links[1:]:
            prob_url = 'http://noi-test.zzstep.com' + prob_link['href']
            dir_name = os.path.join(
                'Problems', link.get_text(), prob_link.get_text())
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
                with open(os.path.join(dir_name, 'solution.cpp'), 'w') as file:
                    file.write('//link:' + prob_url + '\n')
                test_in, test_out = parse_prob(prob_url)
                with open(os.path.join(dir_name, 'test.in'), 'w') as file:
                    file.write(test_in.lstrip())
                with open(os.path.join(dir_name, 'test.out'), 'w') as file:
                    file.write(test_out.lstrip())


if __name__ == '__main__':
    main()
