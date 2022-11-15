
from requests_html import HTMLSession

NATURE_SEARCH_URL = "https://www.nature.com/search?q=DFT&date_range=last_7_days&order=relevance"

session = HTMLSession()

response = session.get(NATURE_SEARCH_URL)
# print(response.html.absolute_links)
#search-article-list
#search-article-list > div > ul > li:nth-child(1)
results = response.html.find('#search-article-list > div > ul > li')
print(results[0].absolute_links)

#pictures
#search-article-list > div > ul > li:nth-child(1) > div > article > div.c-card__layout.u-full-height > div.c-card__image > picture
#search-article-list > div > ul > li:nth-child(2) > div > article > div.c-card__layout.u-full-height > div.c-card__image

images = response.html.find(
    '#search-article-list > div > ul > li:nth-child(1) > div > article > div.c-card__layout.u-full-height > div.c-card__image > picture  > img')

print(images[0].attrs)
