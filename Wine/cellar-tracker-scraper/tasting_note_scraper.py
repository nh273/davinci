def get_tasting_notes(driver, wine_url):
    '''Given wine url, get all available tasting notes'''
    wine_id = wine_url[wine_url.rfind('iWine=')+6:]
    review_url = 'https://www.cellartracker.com/notes.asp?iWine='+wine_id
    driver.get(review_url)
    source = driver.page_source
    soup = BeautifulSoup(r.text)
    display('wine_tasting_soup: '+soup.prettify())
    return wine_id, soup


def parse_tasting_notes(wine_id, soup):
    '''Given BeautifulSoup of tasting notes,
    Parse note & corresponding score'''
    res = []
    notes = soup.findAll('p', itemprop='reviewBody')
    for note in notes:
        review = note.text
        score = note.parent.find('span', itemprop='ratingValue')
        if score:
            score = score.text
        res.append({'wine': wine_id, 'note': review, 'score': score})
    return res
