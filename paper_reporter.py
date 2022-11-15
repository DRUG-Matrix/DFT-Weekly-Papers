
from requests_html import HTMLSession
from constants import NATURE_SEARCH_URL,SCIENCE_SEARCH_URL
from constants import nature_search_results_selector 
from constants import nature_search_images_selector

session = HTMLSession()
response = session.get(NATURE_SEARCH_URL)
results = response.html.find(nature_search_results_selector)
print(results[0].absolute_links)
images = response.html.find(nature_search_images_selector)
print(images[0].attrs)
