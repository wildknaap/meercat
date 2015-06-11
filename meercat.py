#!/usr/local/bin/python
#
# Thu May  2 15:11:20 CEST 2013


import twitter
import argparse
import sys
import pdb


# setup the connection

meercatapi = twitter.Api(consumer_key='<key>',consumer_secret='<secret>',access_token_key='<secret>',access_token_secret='<secret>')


# functions

def tweet():
	global mtweet
	meercatapi.PostUpdate(mtweet)
	return

def direct():
	global mdirect
	meercatapi.PostDirectMessage(mdirect)
	return

def friends():
	mfriends = meercatapi.GetFriends('magnusmeercat')
	print [s.user.name for s in mfriends]
	return


# options

parser = argparse.ArgumentParser(description='Meercat Manor!')
parser.add_argument('-v', '--version', action='version', version='Meercat 0.0.1') 
parser.add_argument('-t', '--tweet', action='store', dest='mtweet',
	help='Tweet message, format: "<text>"')
parser.add_argument('-d', '--direct', action='store', dest='mdirect',
	help='Tweet direct message, format: <test> <user>')
parser.add_argument('-f', '--friends', action='store_const', const=friends,
        help='Get a list of all friends')

results = parser.parse_args()


# tails up!

#pdb.set_trace()

if results.mtweet is not None:
	mtweet = results.mtweet
	tweet()

if results.mdirect is not None:
	mdirect = results.mdirect
	direct()

if results.friends is not None:
        friends()


# EOF
