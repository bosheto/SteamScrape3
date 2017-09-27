from urllib.request import urlopen as uOpen

import core

f = open('Dev/testing.txt', 'w')

page = 1
last_page = 2 

while page < 3:

    # Url to page 
    url = 'http://store.steampowered.com/search/?specials=1&os=win&page=' + str(page)

    # --Open Url-- 
    uClient = uOpen(url)

    # copy its contents to html_source var 
    html_source = uClient.read()

    # --Close Url-- 
    uClient.close()
    # Run only if first page
    if page == 1:
        # set last page 
        last_page = core.get_last_page(html_source) + 1
    
    # Call scrape function from core module giving it the html_source and the file f
    core.scrape(html_source, f) 
    # increment page by 1
    page += 1

f.close()