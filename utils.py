#Util functions

'''Utility functions'''

# This dict holds all the settings for the program
settings = {'format_settings':'', 'output_folder':'', 
'output_line_format':'', 'separation_symbol':'', 'sort_by':''}

number_of_items = 0

# Get the settings from settings.txt
def get_settings():
    '''Get values from settings file'''
    # Open settings.txt
    settings_file = open('settings.txt', 'r')
    # Store all lines in file in lines array
    lines = settings_file.readlines()
    # Loop through each line in array lines 
    for line in lines:
        # Remove white space from line
        line = str(line).strip()
        # If line starts with # than line is comment so skip 
        if line.startswith('#'):
            continue
        # Set output folder to value from settings file
        set_setting_value(line, 'OUTPUT_FOLDER', 'output_folder')
        # Set date/time format to value from settings file
        set_setting_value(line, 'DATE/TIME_FORMAT', 'format_settings')
        # Set output line format to value from settings file
        set_setting_value(line, 'OUTPUT_FORMAT', 'output_line_format')
        # Set separation symbol to value from settings file
        set_setting_value(line, 'SEPARATION_SYMBOL', 'separation_symbol')
        # Set sorting option
        set_setting_value(line, 'SORT_BY', 'sort_by')
    # Close settings.txt
    set_sorting()
    settings_file.close()
#Set setting values helper function of get_settings()
def set_setting_value(line, setting_name, setting_value):
    '''Set a setting to value from file line'''
    # Check if setting name is in the line
    if setting_name in line:
        # If true get setting value
        settings[setting_value] = line.replace(setting_name, '').replace('=', '').strip()
#
def get_url():
    url = ''
    if settings['sort_by'] != '':
        url = 'http://store.steampowered.com/search/?sort_by={}&os=win&specials=1&page='.format(settings['sort_by'])
    else:
        url = 'http://store.steampowered.com/search/?specials=1&page='
    return url
#
def set_sorting():
    sorting_option = settings['sort_by'].lower()
    if sorting_option == 'released':
        settings['sort_by'] = 'Released_DESC'
    elif sorting_option == 'name':
        settings['sort_by'] = 'Name_ASC'
    elif sorting_option == 'price_asc':
        settings['sort_by'] = 'Price_ASC'
    elif sorting_option == 'price_des':
        settings['sort_by'] = 'Price_DESC'
    elif sorting_option == 'reviews':
        settings['sort_by'] = 'Reviews_DESC'
    else:
        settings['sort_by'] = ''
