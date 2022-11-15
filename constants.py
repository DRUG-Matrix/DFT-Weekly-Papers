import time

mon_start, year_start = time.localtime().tm_mon, time.localtime().tm_year
mon_end,  year_end = (mon_start + 1) % 12, ( (mon_start + 1) // 12 ) + year_start

NATURE_SEARCH_URL = "https://www.nature.com/search?q=DFT&date_range=last_7_days&order=relevance"

SCIENCE_SEARCH_URL = f"https://www.science.org/action/doSearch?field1=AllField&text1=" \
                     "DFT&field2=AllField&text2=&publication=&Ppub=" \
                     "&AfterMonth={mon_start}&AfterYear={year_start}&BeforeMonth={mon_end}&BeforeYear={year_end}"

nature_search_results_selector = '#search-article-list > div > ul > li'
nature_search_images_selector = ' #search-article-list > div > ul > li:nth-child(1) > div > article > div.c-card__layout.u-full-height > div.c-card__image > picture  > img')
