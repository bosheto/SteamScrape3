# Core functions

'''Contains all core functions for scraping steam'''

#Imports

from bs4 import BeautifulSoup as soup
from bs4 import UnicodeDammit as UniDam
import utils

# Get the program settings from utils module
utils.get_settings()

# Store the output line formagit t from settings in variable line_format
line_format = utils.settings['output_line_format']

# Store separation symbol from settings in variable 
separation_symbol = utils.settings['separation_symbol']

# Replace the % with the separation symbol
line_format = line_format.replace('%', separation_symbol)

# Main Scraping function takes a page source(page) and a file to write to(file_write)
def scrape(page, file_write):

    '''Get the product information from page and write them to file file_write'''
    # Parse page source 
    page_soup = soup(page, 'html.parser')   
    
    # Get the container(div) that houses all the products
    main_container = page_soup.find('div', {'id':'search_result_container'})
    
    #for every link(a) in main_container
    for link in main_container.find_all('a'):

        
        main_link_container = link.find('div', {'class':'responsive_search_name_combined'})
        output_string = line_format

        try:
            test = get_product_name(main_link_container)
        except AttributeError:
            break

        if 'name' in output_string:
            product_name = get_product_name(main_link_container)
            output_string = output_string.replace('name', str(product_name))  
        if 'rating' in output_string:
            product_rating = get_rating(main_link_container)
            output_string = output_string.replace('rating', str(product_rating))
        if 'discount' in output_string:
            product_discount = get_discount(main_link_container)
            output_string = output_string.replace('discount', str(product_discount))
        if 'price' in output_string:
            product_price = get_price(main_link_container)
            output_string = output_string.replace('price', str(product_price))
        if 'link' in output_string:
            product_link = get_link(link)
            output_string = output_string.replace('link', str(product_link))
        
        file_write.write(output_string + '\n')
#Get product name
def get_product_name(container):

    '''Get the name of the product'''
    name_container = container.find('div', {'class':'col search_name ellipsis'})
    name = name_container.find('span', {'class','title'})
    x = UniDam(name.get_text())
    output_string = x.unicode_markup
    return output_string.encode('ascii', 'ignore').decode()
   
#A helper fucntion for get_product_name
def remove_html_tags(string):
    '''Used to prosses problematic product names'''
    string = str(string)
    remove = False
    output_string = ''
    for char in string:
        if char == '<':
            remove = True
        if not remove:
            output_string += char
        if char == '>':
            remove = False
    output_string = output_string.strip()
    return output_string

# Format Rating information
def get_rating(container):
    '''Get the rating information takes a container'''
    rating_container = container.find('div', {'class':'col search_reviewscore responsive_secondrow'})
    
    # Create variables and initialize the to defult values
    word_rating = ''
    procent_rating = ''
    number_of_reviews = 0

    try:
        rating = rating_container.find('span', {'data-store-tooltip':True})
    
        rating_text = rating['data-store-tooltip'] 

        if 'Very Positive' in rating_text:
            word_rating = 'Very Positive'
        elif 'Mostly Positive' in rating_text:
            word_rating = 'Mostly Positive'
        elif 'Positive' in rating_text:
            word_rating = 'Positive'
        elif 'Mixed' in rating_text:
            word_rating = 'Mixed'
        elif 'Negative' in rating_text:
            word_rating = 'Negative'
        elif 'Mostly Negative' in rating_text:
            word_rating = 'Mostly Negative'
        elif 'Very Negative' in rating_text:
            word_rating = 'Very Negative'
    
        rating_text = rating_text.replace('<br>', ' ')
        array = rating_text.split(' ')
    
        for word in array:
            if '%' in word:
                procent_rating = word
                continue
            if ',' in word:
                word = word.replace(',', '')
                number_of_reviews = word
                continue
            if str(word).isdigit():
                number_of_reviews = word
                continue 
        output_string = str(procent_rating) + separation_symbol + str(word_rating) + separation_symbol + str(number_of_reviews)

        return output_string
    except TypeError:
        
        output_string = '0' + separation_symbol + 'NO RATING' + separation_symbol + '0'
        return output_string
# Get product discount
def get_discount(container):
    '''Get the product discount takes a container'''
    discount_container = container.find('div', {'class':'col search_discount responsive_secondrow'})
    discount = discount_container.get_text()
    discount = discount.replace('-', '').strip()
    return discount
# Get product price
def get_price(container):
    '''Get the new and old price of a product'''
    price_container = container.find('div', {'class':'col search_price discounted responsive_secondrow'})
    
    price = remove_html_tags(price_container)

    output_string = ''
    for char in price:
        if not char.isdigit() or not ',':
            output_string += ' '
            continue 
        output_string += char
    output_string = output_string.replace(' ', '.')
    output_string = output_string.replace('...', ' ').strip()
    output_string = output_string.replace(' ', '/')
    price = output_string
    return price
# Get last page
def get_last_page(page):
    '''Get the last page of the list '''
    page_soup = soup(page, 'html.parser')
    
    main_container = page_soup.find('div', {'id':'search_result_container'})
    
    page_container = main_container.find('div', {'class':'search_pagination_right'})
    
    page_number = []

    for link in page_container.find_all('a'):
        try:
            page_number.append(int(link.get_text()))
        except ValueError:
            continue
    
    return int(page_number[-1])

#
def get_link(container):
    product_link = container['href']
    return product_link
 
#
