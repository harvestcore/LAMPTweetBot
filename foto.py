#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# Librerías
import tweepy, time, sys, re, json
import urllib.request

# Argumento con la foto
img = str(sys.argv[1])
ip = sys.argv[2]

# Keys de acceso a la cuenta
CONSUMER_KEY = 'YOUR CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR CONSUMER_SECRET'
ACCESS_KEY = 'YOUR ACCESS_KEY'
ACCESS_SECRET = 'YOUR ACCESS_SECRET'

# Autenticación de keys y entrada a la cuenta
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# IP DATA
url = "http://ipinfo.io/{0}/json".format(ip)
url_json = urllib.request.urlopen(url)
data = json.loads(url_json.read().decode())
link_melissa = "http://botperrete.sytes.net"

# Tuit que se publica en @BotPerrete
tuit = "Viva España.\n\nFrom: {0} \n({1}, {2}, {3})\n\n{4}".format(ip, data['city'], data['region'], data['country'], link_melissa)

# Update de la cuenta, tuitea la foto (img)
api.update_with_media(img, tuit)

# print estado
print("[+] {0} - IP: {1} - ({2}, {3}, {4}, {5})".format(time.strftime("%H:%M:%S"), ip, data['city'], data['region'], data['country'], data['org']))
