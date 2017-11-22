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
	
    print('Script currently working its magic.')
	
    while(url_object['body']['noSimilarModelsText'] != "No iPhone X models are available for pickup today at nearby Apple Store locations. Please check back later."):
		
		# WebHook for Discord alert
		requests.post(discord_webhook, data={'content': discord_text})
		sys.exit()
			
		# WebHook for Slack alert
		requests.post(slack_webhook, json={'text': slack_text}, headers={'Content-Type': 'application/json'})
		sys.exit()
		
    # Run this code every 60 seconds (1 minute)
    threading.Timer(60.0, iphone_x_check).start()
	
iphone_x_check()