#!/usr/bin/python
import requests, json, os
from getpass import getpass, getuser

chggrps = [ 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 97, 98 ] 
headers = {'content-type': 'application/json'}
USERNAME = getuser()
PASSWD = getpass()

chgrp_dict = {}
for x in chggrps:
#	print x
	r = requests.get('https://sparta.sonynei.net/rest/v1/Changegroups/%s' % x, auth=(USERNAME, PASSWD), headers=headers)
	chgrp_dict[x] = r.json()
	print chgrp_dict[x]["name"],":",chgrp_dict[x]["patchlevels"]["name"]
	#print r.json()

#print chgrp_dict[83]["name"]
#print chgrp_dict[83]["patchlevels"]["name"]
#parsed_json = json.loads(chgrp_dict)
#print(parsed_json['name'])
