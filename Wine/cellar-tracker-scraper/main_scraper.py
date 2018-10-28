from scraper_helper import write_to_csv
from wine_info_scraper import scrape_wine
from tasting_note_scraper import scrape_reviews
import time
import requests
from selenium import webdriver


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
        write_to_csv(wines_urls, URL_FILE)
        for wine_url in wines_urls:
            wine_infos = scrape_wine(driver, wine_url)
            reviews = scrape_reviews(driver, wine_url)
            write_to_csv(reviews, TASTING_NOTES_FILE)
            write_to_csv(wine_infos, WINE_DATA_FILE)
            time.sleep(2)


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
    scrape(driver, 3)
