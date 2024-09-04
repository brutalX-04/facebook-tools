from tools.bahan import *
from tools import setup


# --> Dump Id
def ids():
	try:
		print('─' * 50)
		target = [];idd = 1
		print('Note :\n * Input Id Friendlist Publick')
		print(f' * Use [{h} , {p}] For Dump Multiple Ids\n')
		ids = input('Input Ids : ')
		if ',' in ids:
			[target.append(x) for x in ids.split(',')]
			name = ids.split(',')[0]
		else:
			target.append(ids)
			name = ids

		cookie = open('data/account/.cookie.txt','r').read()
		token = open('data/account/.token.txt','r').read()
		for x in target:
			get = requests.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(x, token), cookies={'cookie': cookie}).json()
			for x in get['friends']['data']:
				try:
					user_id, user_name = x['id'], x['name']
					ida.append(user_id+'|'+user_name)
					print('\rSucces Dump %s%s%s User '%(h, idd, p),end='')
					idd+=1
				except:
					pass
			print('')

		setup.set()

	except Exception as e:
		print('%sFailled Dump%s'%(m, p))
		print(e)


# --> Crack with file
def file():
	try:
		print('─' * 50)
		print('Pemisah harus menggunakan [ | ]')
		path = input('Input file : ')
		try:
			for x in open(path, 'r').readlines():
				ida.append(x.replace('\n',''))

			setting()

		except FileNotFoundError:
			print('%sFile Not Found%s'%(m,p))
			exit()

		except Exception as e:
			raise e

	except Exception as e:
		raise e
