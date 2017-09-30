# SteamScrape3
A tool for scraping Steam

Overview
--------
SteamScrape3 is a simple command line tool for scraping Steam written in Python 3.6.
Im not a pro coder so any advice is welcomed ! 

Current fetures:
-Web Scrape Steams Specials Page
-Write data to txt file
-Chose how many pages to scrape
-Chose what to save(name , discount, price, etc)

Planed fetures:
-Scrape any list of games from Steam not just specials

Usage
------
To start the program simply open a command line window and navigate to the program folder
then type "python SteamScrape3" this will run the program and go through all of the games in the specials category 
and save them to a file named SteamSpecials-[curent time and date].txt in the OUTPUT folder located in the program folder.

You can also pass in command line arguments curently only 2 are available:
--last_page [int] sets the last page you want to scrape to
--exit closes the program after its finished(if not given the program waits for a key press)

