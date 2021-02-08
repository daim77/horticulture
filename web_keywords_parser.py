# TODO vstupem funkce bude webova adresa, na ni se hledaji nasledujici tagy:
# TODO title, alt-img, H1, H2, links, strong, em, keywords argument
# TODO vystupem je txt soubor se slovama
# TODO nove href pouzije znovu pro hledani
# TODO maximalni opakovani parseru je pro 100 odkazu

import csv
import os
import requests
from bs4 import BeautifulSoup


def boilsoup(url):
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, "html.parser")
    return soup


def find_title(file_name, soup):
    result = soup.find('title').text
    print(result)
    csv_writer(file_name, result)
    return


def find_h1(soup):
    pass


def find_h2(soup):
    pass


def find_strong(soup):
    pass


def find_em(soup):
    pass


def find_alt_img(soup):
    pass


def find_keywords(soup):
    pass


def find_href(soup):
    pass


def csv_writer(file_name, result):
    path = os.getcwd() + os.sep + 'tables'
    if not os.path.exists(path):
        os.mkdir(path)

    file_name += '.csv'

    try:
        with open(path + os.sep + file_name, mode='a', encoding='utf-8') \
                as csv_file:

            writer = csv.writer(csv_file, delimiter=',')

            for row in result:
                writer.writerow(row)

            print('You are lucky! Data available here:')
            print('=' * 100)
            print(path + os.sep + file_name)
            print('=' * 100)
    except IOError:
        print("I/O error")
    return


def main(file_name, url):
    soup = boilsoup(url)
    find_title(file_name, soup)
    pass


if __name__ == '__main__':
    main('na_luka', 'https://www.naluka.cz')
