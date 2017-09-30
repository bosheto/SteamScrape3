'''Start file for program'''

# Imports
from urllib.request import urlopen as uOpen
import time
import core
import utils

print('\nSteamScrape3\n')

# Get the program settings from utils module
utils.get_settings()

print('Settings loaded\n')
# Create variable to store page number and set it to 1
page = 1
# Create variable to store last page and set it to 2 
last_page = 2

#Get the curent time and or date using the setting format_seting
time_date = time.strftime(utils.settings['format_settings'])

# Create a filename using output folder setting and time/date setting
filename = utils.settings['output_folder'] + '/SteamSpecial'+ '-' + time_date + '.txt'

# open file 
f = open(filename, 'w')
print('File {} created\n'.format(str(filename)))
start_time = time.time()

static_url = utils.get_url()
print(static_url)
# loop until page is less than last page
while page < last_page:

    # Url to page 
    url = static_url + str(page)
    
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
        print('Number of pages:' + str(last_page))

    # Call scrape function from core module giving it the html_source and the file f
    core.scrape(html_source, f) 
    # increment page by 1
    
    page += 1
# After looping through all pages close file f

end_time = time.time() - start_time
end_time = "%.2f" % end_time

print('\nDone scraping {0} items in {1} seconds\n'.format(utils.number_of_items ,str(end_time)))

f.close()

print('File {} closed ! \n'.format(str(filename)))
print ('Thank you for using SteamScrape 3 \n')
