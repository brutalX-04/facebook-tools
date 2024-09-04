from tools.bahan import *


# --> Info Provider
def myip():
	try:
		get = requests.get('https://api.myip.com').json()
		ip = get['ip']
		country = get['country']
		return ip,country

	except Exception as e:
		raise e
