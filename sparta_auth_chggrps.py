#!/usr/bin/python
import requests, json, os
from getpass import getpass, getuser

lines = [ "C1", "D1", "D2", "D3", "E1", "H1", "H2", "L1", "Q1", "Q2", "P1", "P2" ]
chggrps = [ 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 97, 98 ] 
headers = {'content-type': 'application/json'}
USERNAME = getuser()
PASSWD = getpass()

for x in chggrps:
	print x
	r = requests.get('https://sparta.sonynei.net/rest/v1/Changegroups/%s' % x, auth=(USERNAME, PASSWD), headers=headers)
	print r.json() 
