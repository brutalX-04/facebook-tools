from tools.bahan import *
from tools import auth

# --> Info Account
def check():
	try:
		cookie = open('data/account/.cookie.txt','r').read()
		token = open('data/account/.token.txt','r').read()
		get = requests.get('https://graph.facebook.com/v18.0/me?fields=id,name&access_token='+token, cookies={'cookie': cookie}).json()
		name = get['name']
		ids = get['id']
		return name, ids
	except Exception as e:
		print(f'{m}Failled Get Info Account{p}, Wait To Login ...');time.sleep(2)
		login()