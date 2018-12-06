from bs4 import BeautifulSoup
import re


def scrape_wine(driver, wine_url):
    '''Scraper for one single wine, getting basic infos'''
    wine_soup = get_wine_soup(driver, wine_url)
    wine_infos = get_wine_infos(wine_soup)
    return wine_infos


def get_wine_soup(driver, wine_url):
    '''Given url for single wine, get content as BeautifulSoup'''
    driver.get(wine_url)
    source = driver.page_source
    soup = BeautifulSoup(source)
    return soup


def get_main_score(soup):
    '''Get wine main score'''
    scorebox = soup.find('div', class_='scorebox')
    s = scorebox.text
    s = s[s.find('CT')+3:]
    s = s[:s.find('\n')]
    return s


def find_href_by_keyword(soup, keyword):
    return soup.find('a', href=re.compile(keyword)).text


def get_wine_infos(soup):
    '''Get basic wine infos from a BeautifulSoup parse'''
    res = {}
    res['title'] = soup.title.text
    res['varietal'] = soup.h2.text
    res['score'] = get_main_score(soup)
    res['country'] = find_href_by_keyword(soup, 'Country')
    res['region_1'] = find_href_by_keyword(soup, 'Region')
    res['region_2'] = find_href_by_keyword(soup, 'SubRegion')
    return [res]
