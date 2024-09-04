# --> Module
import os
import re
import sys
import time
import json
import random
import struct
import base64
import requests
import binascii
from Crypto.Cipher import AES
from datetime import datetime
from bs4 import BeautifulSoup as bs
from Cryptodome import Random as RDM
from nacl.public import PublicKey as PK
from nacl.public import SealedBox as SB
from concurrent.futures import ThreadPoolExecutor


# --> Color
p  = '\33[m' 		# DEFAULT
m  = '\x1b[0;91m' 	# RED 
k  = '\033[0;93m' 	# KUNING 
h  = '\x1b[0;92m' 	# HIJAU 
u  = "\033[0;35m"   # UNGU
a  = "\033[1;30m"   # ABU


# --> Calback
timeNow      = str(datetime.now()).split(' ')[0]
resultNameOk = 'Ok-%s.txt'%(timeNow)
resultNameCp = 'Cp-%s.txt'%(timeNow)
devices      = []
loop         = 1
ida          = []
ok           = 0
cp           = 0
[devices.append('"%s"'%(x.replace('\n',''))) for x in open('tools/device.txt','r').readlines()]


# -- > Banner
def banner():
	os.system('clear')
	print(f'{h}_____________________  {k}                      __     \n{h}\_   _____/\______   \ {k}          ___________|  | __ \n{h} |    __)   |    |  _/ {u} ______{k} _/ ___\_  __ \  |/ / \n{h} |     \    |    |   \ {u}/_____/{k} \  \___|  | \/    <  \n{h} \___  /    |______  / {u}       {k}  \___  >__|  |__|_ \ \n{h}     \/            \/  {k}             \/           \/ {p} ')
	print('─' * 50)
