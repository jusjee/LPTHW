#!/usr/bin/python
import requests, json, os

# discovery = 'https://sparta.sonynei.net'
# login_data = {'username':"test", 'password':"test"}
# headers = {'content-type': 'application/json'}

# r = requests.post("%s/auth/login" % discovery,data=json.dumps(login_data), headers=headers, verify=False)

# chggrps = [ 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 97, 98 ] 
headers = {'content-type': 'application/json'}
#for x in chggrps:
#	print x
r = requests.get('https://sparta.sonynei.net/rest/v1/Changegroups/83', auth=('jgonzales', os.environ['PASSWD']), headers=headers)
print r.json()
# if r.status_code != 200 or 'sparta-auth' not in r.cookies:
#       log.error('Login failed')
#       sys.exit(1)

#cookies = {'sparta-auth': r.cookies['sparta-auth']}
#print cookies
# print r.json()
