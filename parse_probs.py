import re
import requests
from bs4 import BeautifulSoup
import os

def get_prob_set(href):
    url = 'http://noi-test.zzstep.com' + href
    rsp = requests.get(url)
    soup = BeautifulSoup(rsp.text)
    links = soup.find_all('a', href=re.compile(r'contest/0x'))
    prob_set = []
    for link in links:
        prob_set.append(link.get_text())
    
    return prob_set

def main():
    url = 'http://noi-test.zzstep.com/contest?type=1'
    rsp = requests.get(url)
    soup = BeautifulSoup(rsp.text)
    links = soup.find_all('a', href=re.compile(r'contest/0x'))
    for link in links:
        names =get_prob_set(link['href'])
        print(names)
        for name in names[1:]:
            dir_name = os.path.join('Problems', link.get_text(), name)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
                file = open(os.path.join(dir_name, 'solution.cpp'), 'w')
                file.close()

if __name__ == '__main__':
    main()