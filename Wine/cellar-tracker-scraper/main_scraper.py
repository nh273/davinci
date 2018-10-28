from scraper_helper import write_to_csv, random_sleep
from wine_info_scraper import scrape_wine
from tasting_note_scraper import scrape_reviews
import time
import requests
from selenium import webdriver
import numpy.random as nrand


MAIN_URL = 'https://www.cellartracker.com/list.asp'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
DIR = '../data/cellar-tracker-scrape/'
URL_FILE = DIR + 'wines_url.csv'
WINE_DATA_FILE = DIR + 'cellar_tracker_wine_data.csv'
TASTING_NOTES_FILE = DIR + 'cellar_tracker_reviews.csv'


def scrape(driver, max_page):
    '''Master function that handles the actual scraping'''
    for page_number in range(1, max_page):
        winelist_url = get_wine_list_url(page_number)
        wines_urls = get_wines_url(driver, winelist_url)
        write_to_csv(['url'], [{'url': url} for url in wines_urls],
                     URL_FILE)
        while wines_urls:
            wine_url = nrand.choice(wines_urls)
            wines_urls.remove(wine_url)
            random_sleep()
            wine_info = scrape_wine(driver, wine_url)
            random_sleep()
            reviews = scrape_reviews(driver, wine_url)
            write_infos_to_csv(wine_info)
            write_reviews_to_csv(reviews)
            random_sleep()


def write_infos_to_csv(wine_info):
    '''Write reviews to csv'''
    fields = ['title', 'varietal', 'score', 'country', 'region_1', 'region_2']
    write_to_csv(fields, wine_info, WINE_DATA_FILE)


def write_reviews_to_csv(wine_reviews):
    fields = ['wine', 'note', 'score']
    write_to_csv(fields, wine_reviews, TASTING_NOTES_FILE)


def get_wine_list_url(page_number):
    '''Parse URL of page of list of wines, given page number'''
    payload = {'Table': 'List',
               'iUserOverride': 0,
               'O': 'Quantity DESC',
               'page': page_number}
    r = requests.get(MAIN_URL, params=payload, headers=HEADERS)
    if r.status_code == 200:
        return r.url
    else:
        print(r.status_code)
        print(r.text)
        return ''


def get_wines_url(driver, wine_list_url):
    '''Get list of wines urls given an url of a page of
    wine list'''
    url_list = []
    driver.get(wine_list_url)
    wines = driver.find_elements_by_class_name('more')
    for wine in wines:
        url_list.append(wine.get_attribute('href'))
    return url_list


if __name__ == '__main__':
    driver = webdriver.Chrome(
        '/usr/local/Caskroom/chromedriver/2.41/chromedriver')
    scrape(driver, 201)
    driver.quit()
