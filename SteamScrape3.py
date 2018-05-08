'''Start file for program'''

# Imports
from urllib.request import urlopen as uOpen
from queue import Queue
from thread_class import Worker
import time
import argparse
import core
import utils


parser = argparse.ArgumentParser()
parser.add_argument('--lastpage', dest='lastpage', help='Specify the last page to scrape', type=int)
parser.add_argument('--exit', dest='exit', help='Close program when done scraping', action='store_true')
args = parser.parse_args()


print('\nSteamScrape3 by bosheto\n')

# Get the program settings from utils module
utils.get_settings()


print('Settings loaded\n')


# Create variable to store page number and set it to 1
page = 1
# Create variable to store last page and set it to 2 

if args.lastpage == None:
    last_page = core.get_last_page()
else:
    last_page = int(args.lastpage)

#Get the curent time and or date using the setting format_seting
time_date = time.strftime(utils.settings['format_settings'])

# Create a filename using output folder setting and time/date setting
filename = utils.settings['output_folder'] + '/SteamSpecial'+ '-' + time_date + '.txt'

# open file 
f = open(filename, 'w')

print('File {} created\n'.format(str(filename)))
start_time = time.time()

print('Number of pages to scrape: ' + str(last_page) + '\n')
print('Scraping....')

q = Queue()

for i in range(4):
    worker = Worker(q,f)
    worker.daemon = True
    worker.start()

for x in range(last_page):
    q.put(str(utils.get_url()) + str(x+1))

q.join()

f.close()

# After looping through all pages close file f

end_time = time.time() - start_time
end_time = "%.2f" % end_time
print()
print('\nDone scraping {0} items in {1} seconds\n'.format(utils.number_of_items ,str(end_time)))

f.close()

print('File {} closed ! \n'.format(str(filename)))
print ('Thank you for using SteamScrape 3 \n')

if not args.exit :
    input('Press Enter to exit')