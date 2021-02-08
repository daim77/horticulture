# TODO nove href pouzije znovu pro hledani
# TODO maximalni opakovani parseru je pro 100 odkazu

import os
import requests
from bs4 import BeautifulSoup


def boilsoup(url):
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, "html.parser")
    return soup


def find_title(file_name, soup):
    title_result = soup.find_all('title')
    result = [item.text for item in title_result]
    txt_writer(file_name, result)
    return


def find_h1(file_name, soup):
    h1_result = soup.find_all('h1')
    result = [item.text for item in h1_result]
    txt_writer(file_name, result)
    return


def find_h2(file_name, soup):
    h2_result = soup.find_all('h2')
    result = [item.text for item in h2_result]
    txt_writer(file_name, result)
    return


def find_strong(file_name, soup):
    strong_result = soup.find_all('strong')
    result = [item.text for item in strong_result]
    txt_writer(file_name, result)
    return


def find_em(file_name, soup):
    em_result = soup.find_all('em')
    result = [item.text for item in em_result]
    txt_writer(file_name, result)
    return


def find_alt_img(soup):
    pass


def find_keywords(file_name, soup):
    try:
        meta_result = soup.find(attrs={'name': 'keywords'})
        result = list(meta_result['content'])
        txt_writer(file_name, result)
    except:
        return
    return


def find_href(soup):
    pass


def txt_writer(file_name, result):
    path = os.getcwd() + os.sep + 'tables'
    if not os.path.exists(path):
        os.mkdir(path)

    file_name += '.txt'

    try:
        with open(path + os.sep + file_name, mode='w', encoding='utf-8') \
                as txt_file:
            for item in result:
                txt_file.writelines(' ' + item)
    except IOError:
        print("I/O error")
    return


def main(file_name, url):
    soup = boilsoup(url)
    find_title(file_name, soup)
    find_h1(file_name, soup)
    find_h2(file_name, soup)
    find_strong(file_name, soup)
    find_em(file_name, soup)

    find_keywords(file_name, soup)


if __name__ == '__main__':
    main('na_luka', 'https://www.naluka.cz')
    main('pereny_org', 'https://pereny.org')
