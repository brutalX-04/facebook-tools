# Author  : brutalx
# Created : 16-april-2024


# Module
from tools import check, auth, ipCheck, dump, asyncFb
from tools.bahan import *



# --> Menu
def menu():
	banner()
	acc = auth.check()
	infoIp = ipCheck.myip()

	print('Name     : %s%s%s'%(h,acc[0],p))
	print('Ids      : %s%s%s'%(h,acc[1],p))
	print('Ip       : %s%s%s'%(u,infoIp[0],p))
	print('Country  : %s%s%s'%(u,infoIp[1],p))
	print('─' * 50)
	print('1. Start crack with dump')
	print('2. Start crack with file')
	print('0. Log Out\n')
	pilih = input('Input : ')

	if pilih in ['01','1']:
		dump.ids()

	elif pilih in ['02','2']:
		dump.file()

	elif pilih in ['0','00']:
		os.system('rm data/account/.token.txt')
		os.system('rm data/account/.cookie.txt')


# --> Running Script
if __name__ == '__main__':
	menu()