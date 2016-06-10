#/usr/bin/env python
# coding:UTF-8

import requests
ACCESS_TOKEN = 'your access token'

def sentYo(username,body):
	print(ACCESS_TOKEN)
	return requests.post("http://api.justyo.co/yos/",data={'access_token':ACCESS_TOKEN,'username':username,'text':body})


if __name__ == '__main__':
	with open('msg.txt','r') as file:
		for row in file:
			print(row,end="")
		print('');


	username = input('Scan user barcode...')
	
	while(username != ''):
		r = sentYo(username,'Yo from Barcode!!!!')
		
		if r.status_code != 200:
			print(r.text)

		username = input('Scan user barcode...')

		
