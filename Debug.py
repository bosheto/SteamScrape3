from urllib.request import urlopen as uOpen

import core

f = open('Dev/testing.txt', 'w')

# Url to page 
# Url to page 
url = 'http://store.steampowered.com/search/?specials=1&os=win&page=1' 

# --Open Url-- 
uClient = uOpen(url)

# copy its contents to html_source var 
html_source = uClient.read()

# --Close Url-- 
uClient.close()

core.scrape(html_source, f) 

f.close()