from tools.bahan import *


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


# --> Login
# Thanks to rozhak for methode get token
def login():
	try:
		banner()
		cookie = input('Input Cookie : ')
		with requests.Session() as rsn:
			rsn.headers.update({
				'Accept-Language': 'id,en;q=0.9',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
				'Referer': 'https://www.instagram.com/',
				'Host': 'www.facebook.com',
				'Sec-Fetch-Mode': 'cors',
				'Accept': '*/*',
				'Connection': 'keep-alive',
				'Sec-Fetch-Site': 'cross-site',
				'Sec-Fetch-Dest': 'empty',
				'Origin': 'https://www.instagram.com',
				'Accept-Encoding': 'gzip, deflate'
			})
			response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cookie})
			if '"access_token":' in str(response.headers):
				token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
				open('data/account/.token.txt', 'w').write(token)
				open('data/account/.cookie.txt', 'w').write(cookie)
				print('%sLogin Succes%s'%(h, p))
				exit()

			else:
				print('%sFailled Get Token%s'%(m, p))
				exit()

	except Exception as e:
		exit()