from tools.bahan import *

try:
	os.listdir('data')
except:
	os.system('mkdir data')
	os.system('mkdir data/account')
	os.system('mkdir data/result')