#!/usr/bin/env python
# -*- coding: utf-8 -*-

# iPhone X Checker
# author - Yu Lin
# https://github.com/yulin12345
# admin@yulin12345.site

import json
import requests
import sys
import threading
import urllib2

def iphone_x_check():

    # Variables
    store = []
    city = []
    pickup = []

    # Search zip code
    zip_code = '11355'

    # iPhone X Models
    silver_64gb = 'MQAR2LL/A'
    space_64gb = 'MQAQ2LL/A'
    silver_256gb = 'MQAV2LL/A'
    space_256gb = 'MQAU2LL/A'
	
    # Alert
    discord_webhook = 'DISCORD WEBHOOK URL'
    slack_webhook = 'SLACK WEBHOOK URL'
    discord_text = 'iPhone X Reservation for ' + zip_code + ' Open. GO GO GO GO GO!'
    slack_text = 'iPhone X Reservation for ' + zip_code + ' Open. GO GO GO GO GO!'
    
    # Link/URL
    url = urllib2.urlopen('https://www.apple.com/shop/retail/pickup-message?pl=true&cppart=TMOBILE/US&parts.0=' + silver_64gb + '&location=' + zip_code)

    # Load URL
    url_object = json.load(url)

    # print("Store Name  -------  City  -------  Pickup")

    # For loop all the stores in the JSON and store as an array
    for i in url_object['body']['stores']:
        store.append(i['storeName'])
        city.append(i['city'])
        pickup.append(i['partsAvailability'][silver_64gb]['pickupSearchQuote'])

        # Ugly format.
        # print(i['storeName'] + '     ' + i['city'] + '     ' + i['partsAvailability'][silver_64gb]['pickupSearchQuote'])

    # No recommended, but better format.
    print('{} {:>15} {:>27}'.format(store[0], city[0], pickup[0]))
    print('{} {:>13} {:>27}'.format(store[1], city[1], pickup[1]))
    print('{} {:>16} {:>27}'.format(store[2], city[2], pickup[2]))
    print('{} {:>16} {:>27}'.format(store[3], city[3], pickup[3]))
    print('{} {:>15} {:>27}'.format(store[4], city[4], pickup[4]))
    print('{} {:>20} {:>26}'.format(store[5], city[5], pickup[5]))
    print('{} {:>13} {:>27}'.format(store[6], city[6], pickup[6]))
    print('{} {:>24} {:>27}'.format(store[7], city[7], pickup[7]))
    print('{} {:>12} {:>27}'.format(store[8], city[8], pickup[8]))
    print('{} {:>10} {:>27}'.format(store[9], city[9], pickup[9]))
    print('{} {:>16} {:>24}'.format(store[10], city[10], pickup[10]))
    print('{} {:>17} {:>28}'.format(store[11], city[11], pickup[11]))
    
    # Use not equal to check if the stores reservation is open. If open, alert using Discord
    while(pickup[0] != "Currently unavailable" or pickup[1] != "Currently unavailable" or pickup[2] != "Currently unavailable" or pickup[3] != "Currently unavailable" or pickup[4] != "Currently unavailable" or pickup[5] != "Currently unavailable" or pickup[6] != "Currently unavailable" or pickup[7] != "Currently unavailable" or pickup[8] != "Currently unavailable" or pickup[9] != "Currently unavailable" or pickup[10] != "Currently unavailable" or pickup[11] != "Currently unavailable"):
	
		# WebHook for Discord alert
		requests.post(discord_webhook, data={'content': discord_text})
		sys.exit()
			
		# WebHook for Slack alert
		requests.post(slack_webhook, json={'text': slack_text}, headers={'Content-Type': 'application/json'})
		sys.exit()
		
    # Run this code every 60 seconds (1 minute)
    threading.Timer(60.0, iphone_x_check).start()

iphone_x_check()