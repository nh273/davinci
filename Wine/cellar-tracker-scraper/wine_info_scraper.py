def get_wine_soup(wine_url):
    '''Given url for single wine, get content as BeautifulSoup'''
    driver.get(wine_url)
    source = driver.page_source
    soup = BeautifulSoup(source)
    display('wine_soup: '+soup.prettify())
    return soup


def strip_white_space(text):
    """Clean up \n, \xa0 and the likes"""
    to_replace = ['\n', '\xa0', '\t']
    for unwanted in to_replace:
        text = text.replace(unwanted, ' ')  # replace with space
    return text


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
