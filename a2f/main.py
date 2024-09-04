import os
import re
import sys
import time
import struct
import base64
import binascii
import requests
from Crypto.Cipher import AES
from bs4 import BeautifulSoup as bs
from Cryptodome import Random as RDM
from nacl.public import PublicKey as PK
from nacl.public import SealedBox as SB



# COLOR
p  = '\33[m' 		# DEFAULT
m  = '\x1b[0;91m' 	# RED 
k  = '\033[0;93m' 	# KUNING 
h  = '\x1b[0;92m' 	# HIJAU 


# CALLING
rs = requests.Session()


# CLEAR
def clear():
	if "win" in sys.platform.lower():
		os.system('cls')
	else:
		os.system('clear')


# CLASS BANNER
class banner:
	def __init__(self):
		self.banner()

	def banner(self):
		clear()
		print('┏┓┏┓┳┳┓   ┓\n ┃┃ ┃┃┃┏┓┏┫       © 2023\n┗┛┗┛┛ ┗┗┛┗┻       by%s XMod%s'%(h,p))
		print('*' * 25)


# CLASS MENU
class menu:
	def __init__(self):
		self.menu()

	def menu(self):
		banner()
		print('Pasang A2f Via Input Acc')
		print('Pasang A2f Via File')
		pilih = input('Pilih : ')
		if pilih in ['01','1']:
			print('*' * 25)
			print('Input Acc Contoh [ %semail@gmail.com|password%s ]'%(h,p))
			acc = input('Input Acc : ')
			print('*' * 25)
			cookie().get_cookies(acc)
		elif pilih in ['02','2']:
			print('*' * 25)
			print('Input Lokasi File Contoh [ %s/sdcard/file.txt%s ]'%(h,p))
			lok = input('Input File : ')
			try:
				data = open(lok, 'r').readlines()
				for acc in data:
					print('*' * 25)
					cookie().get_cookies(acc.replace('\n',''))
			except Exception as e:
				print(e)


# CLASS ENCRYPT PW - Thank To Yayan 
class encrypt:
	def __init__(self):
		pass

	def password(self, pw):
		try:
			headers = {'authority': 'www.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'dpr': '1', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.4.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
			link = bs(rs.get('https://www.facebook.com/', headers=headers).text, 'html.parser')
			teme = re.search('"__spin_t":(.*?),', str(link)).group(1)
			publ = re.search('"publicKey":"(.*?)",', str(link)).group(1)
			pubk = re.search('"keyId":([0-9]+)', str(link)).group(1)
			rdb = RDM.get_random_bytes(32)
			dpt = AES.new(rdb, AES.MODE_GCM, nonce=bytes([0]*12), mac_len=16)
			dpt.update(str(teme).encode("utf-8"))
			epw, ctg = dpt.encrypt_and_digest(pw.encode("utf-8"))
			sld = SB(PK(binascii.unhexlify(str(publ)))).encrypt(rdb)
			ecp = base64.b64encode(bytes([1,int(pubk),*list(struct.pack('<h', len(sld))),*list(sld),*list(ctg),*list(epw)])).decode("utf-8")
			encp = '#PWD_BROWSER:5:%s:%s'%(teme,str(ecp))
			return encp
		except Exception as e:exit(e)


# CLASS GET COOKIE
class cookie:
    def __init__(self):
        pass

    def get_cookies(self,acc):
        id, pw = acc.split('|')[0], acc.split('|')[1]
        with requests.Session() as ses:
            ses.headers.update({
                'Accept':   'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language':  'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'sec-ch-prefers-color-scheme':  'light',
                'sec-ch-ua':    '"Not.A/Brand";v="8", "Chromium";v="111", "Google Chrome";v="111"',
                'sec-ch-ua-full-version-list':  '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform':   '"Android"',
                'sec-ch-ua-platform-version':   '"10.0.0"',
                'Sec-Fetch-Dest':   'document',
                'Sec-Fetch-Mode':   'navigate',
                'Sec-Fetch-Site':   'same-origin',
                'Sec-Fetch-User':   '?1',
                'Upgrade-Insecure-Requests':    '1',
                'User-Agent':   'Mozilla/5.0 (Linux; Android 10; Redmi 7 Build/QKQ1.191008.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'})
            get = bs(ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text, 'html.parser')
            form = get.find('form', {'method': 'post'})
            header = {
                'initiator':    'https://mbasic.facebook.com',
                'Accept':   'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding':  'gzip, deflate, br',
                'Accept-Language':  'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin':   'https://mbasic.facebook.com',
                'Referer':  'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                'sec-ch-prefers-color-scheme':  'light',
                'sec-ch-ua':    '"Not.A/Brand";v="8", "Chromium";v="111", "Google Chrome";v="111"',
                'sec-ch-ua-full-version-list':  '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform':   '"Android"',
                'sec-ch-ua-platform-version':   '"10.0.0"',
                'Sec-Fetch-Dest':   'document',
                'Sec-Fetch-Mode':   'navigate',
                'Sec-Fetch-Site':   'same-origin',
                'Sec-Fetch-User':   '?1',
                'Upgrade-Insecure-Requests':    '1',
                'User-Agent':   'Mozilla/5.0 (Linux; Android 10; Redmi 7 Build/QKQ1.191008.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
            }
            data = {
                "bi_xrwh":  re.search('name="bi_xrwh" type="hidden" value="(.*?)"', str(form)).group(1),
                "email":    id,
                "jazoest":  re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
                "li":   re.search('name="li" type="hidden" value="(.*?)"', str(form)).group(1),
                "login":    re.search('name="login" type="submit" value="(.*?)"', str(form)).group(1),
                "lsd":  re.search('name="lsd" type="hidden" value="(.*?)"', str(form)).group(1),
                "m_ts": re.search('name="m_ts" type="hidden" value="(.*?)"', str(form)).group(1),
                "pass": pw,
                "try_number":   re.search('name="try_number" type="hidden" value="(.*?)"', str(form)).group(1),
                "unrecognized_tries":   re.search('name="unrecognized_tries" type="hidden" value="(.*?)"', str(form)).group(1)  
            }
            post = ses.post(f"https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=data,headers=header, allow_redirects=False)
            cookies = (";").join([ "%s=%s" % (key, value) for key, value in post.cookies.get_dict().items() ])
            if 'c_user' in cookies:
                print('%sSucces Get Cookies%s'%(h,p))
                auth().authent(cookies)
            elif 'checkpoint' in cookies:
                print('\r%sAccount checkpoint/A2f%s'%(k,p))
            else:
                print('\r%sPassword Wrong%s        '%(m,p))




class auth:
	def __init__(self):
		pass

	# GET ALL DATA
	def authent(self, cookies):
		self.cookies = {'cookie': cookies}
		headers = {'authority': 'www.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'dpr': '1', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.4.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
		get = rs.get('https://accountscenter.facebook.com/password_and_security/two_factor', headers=headers, cookies=self.cookies).text
		self.user = re.search('"ACCOUNT_ID":"(.*?)"', str(get)).group(1);self.haste = re.search('"haste_session":"(.*?)"', str(get)).group(1);self.client = re.search('"client_revision"\:(.*?)\,', str(get)).group(1);self.spin_r = re.search('"__spin_r"\:(.*?)\,', str(get)).group(1);self.spin_t = re.search('"__spin_t"\:(.*?)\,', str(get)).group(1);self.hsi = re.search('"hsi":"(.*?)"', str(get)).group(1);self.dtsg = re.search('"DTSGInitialData"\,\[\]\,{"token":"(.*?)"', str(get)).group(1);self.lsd = re.search('"LSD"\,\[\]\,{"token":"(.*?)"', str(get)).group(1);self.jazoest = re.search('jazoest=(.*?)"', str(get)).group(1);self.client_id = re.search('"clientID":"(.*?)"', str(get)).group(1)
		self.center()


	# HANDLE PASSWORD
	def password(self):
		try:
			self.enc_pw = encrypt().password(pw)
			print('%sSucces Encrypt PWD%s'%(h,p), end='')
		except:
			print('%sFailled Encrypt PWD%s'%(m,p), end='')

		headers = {
			'authority': 'accountscenter.facebook.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'no-cache', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1', 'origin': 'https://accountscenter.facebook.com', 'pragma': 'no-cache', 'referer': 'https://accountscenter.facebook.com/password_and_security/two_factor', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.141", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.141"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"10.0.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-asbd-id': '129477', 'x-fb-friendly-name': 'FXPasswordReauthenticationMutation', 'x-fb-lsd': self.lsd
		}

		data = {
		    'av': self.user,
		    '__user': self.user,
		    '__a': '1',
		    '__req': '19',
		    '__hs': self.haste,
		    'dpr': '1',
		    '__ccg': 'MODERATE',
		    '__rev': self.client,
		    '__s': '',
		    '__hsi': self.hsi,
		    '__dyn': '',
		    '__csr': '',
		    '__comet_req': '5',
		    'fb_dtsg': self.dtsg,
		    'jazoest': self.jazoest,
		    'lsd': self.lsd,
		    '__spin_r': self.spin_r,
		    '__spin_b': 'trunk',
		    '__spin_t': self.spin_t,
		    'fb_api_caller_class': 'RelayModern',
		    'fb_api_req_friendly_name': 'FXPasswordReauthenticationMutation',
		    'variables': '{"input":{"account_id":%s,"account_type":"FACEBOOK","password":{"sensitive_string_value":"%s"},"actor_id":"%s","client_mutation_id":"1"}}'%(self.user, self.enc_pw, self.user),
		    'server_timestamps': 'true',
		    'doc_id': '5864546173675027',
		}

		post = rs.post('https://accountscenter.facebook.com/api/graphql/', cookies=self.cookies, headers=headers, data=data).text
		open('password.txt', 'w').write(post)
		if 'is_reauth_successful":true' in post:
			print('%sPassword Handle Succes%s'%(h,p), end='')
			self.center()
		else:
			print('%sPassword Handle Failled%s'%(m,p))


	# GET OTP FROM TOTP
	def getOTP(self, totp):
		get = rs.get('https://2fa.live/tok/%s'%(totp.replace(' ',''))).text
		token = re.search('"token":"(.*?)"', get).group(1)
		print('|OTP: %s%s%s'%(h,token,p))
		return token


	# GET CODE TOTP
	def center(self):
		headers = {
			'authority': 'accountscenter.facebook.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'no-cache', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1', 'origin': 'https://accountscenter.facebook.com', 'pragma': 'no-cache', 'referer': 'https://accountscenter.facebook.com/password_and_security/two_factor', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.141", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.141"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"10.0.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-asbd-id': '129477', 'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation', 'x-fb-lsd': self.lsd
		}

		data = {
		    'av': self.user,
		    '__user': self.user,
		    '__a': '1',
		    '__req': '1a',
		    '__hs': self.haste,
		    'dpr': '1',
		    '__ccg': 'MODERATE',
		    '__rev': self.client,
		    '__s': '',
		    '__hsi': self.hsi,
		    '__dyn': '',
		    '__csr': '',
		    '__comet_req': '5',
		    'fb_dtsg': self.dtsg,
		    'jazoest': self.jazoest,
		    'lsd': self.lsd,
		    '__spin_r': self.spin_r,
		    '__spin_b': 'trunk',
		    '__spin_t': self.spin_t,
		    'fb_api_caller_class': 'RelayModern',
		    'fb_api_req_friendly_name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
		    'variables': '{"input":{"client_mutation_id":"%s","actor_id":"%s","account_id":"%s","account_type":"FACEBOOK","device_id":"device_id_fetch_datr","fdid":"device_id_fetch_datr"}}'%(self.client_id, self.user, self.user),
		    'server_timestamps': 'true',
		    'doc_id': '9018559631489271',
		}

		post = rs.post('https://accountscenter.facebook.com/api/graphql/', cookies=self.cookies, headers=headers, data=data).text
		open('otp.txt', 'w').write(post)

		if '"success":true' in post:
			self.OTP = re.search('"key_text":"(.*?)"', post).group(1)
			print('TOTP: %s%s%s'%(h,self.OTP,p), end='')
			self.confirm()
		elif '"challenge_type\":\"password\"' in post:
			self.password()
		else:
			print('%sFailled Get TOTP%s'%(m,p))



	# CONFIRM OTP
	def confirm(self):
		headers = {
		    'authority': 'accountscenter.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9,id;q=0.8','cache-control': 'no-cache','content-type': 'application/x-www-form-urlencoded','dpr': '1','origin': 'https://accountscenter.facebook.com','pragma': 'no-cache','referer': 'https://accountscenter.facebook.com/password_and_security/two_factor','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"','sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.141", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.141"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','x-asbd-id': '129477','x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation','x-fb-lsd': self.lsd
		}

		data = {
		    'av': self.user,
		    '__user': self.user,
		    '__a': '1',
		    '__req': '1i',
		    '__hs': self.haste,
		    'dpr': '1',
		    '__ccg': 'GOOD',
		    '__rev': '1008428097',
		    '__s': '',
		    '__hsi': self.hsi,
		    '__dyn': '',
		    '__csr': '',
		    '__comet_req': '5',
		    'fb_dtsg': self.dtsg,
		    'jazoest': self.jazoest,
		    'lsd': self.lsd,
		    '__spin_r': self.spin_r,
		    '__spin_b': 'trunk',
		    '__spin_t': self.spin_t,
		    'fb_api_caller_class': 'RelayModern',
		    'fb_api_req_friendly_name': 'useFXSettingsTwoFactorEnableTOTPMutation',
		    'variables': '{"input":{"client_mutation_id":"%s","actor_id":"%s","account_id":"%s","account_type":"FACEBOOK","verification_code":"%s","device_id":"device_id_fetch_datr","fdid":"device_id_fetch_datr"}}'%(self.client_id, self.user, self.user, self.getOTP(self.OTP)),
		    'server_timestamps': 'true',
		    'doc_id': '6143007815752735',
		}

		post = rs.post('https://accountscenter.facebook.com/api/graphql/', cookies=self.cookies, headers=headers, data=data).text
		open('hasil.txt','w').write(post)

		if 'error_message' in post:
			print('%sOTP incorect%s'%(m,p))
		elif '"success":true' in post:
			print('%sA2f Succes%s'%(h,p))
			self.recovery()


	# GET RECOVERY CODE
	def recovery(self):
		headers = {
		    'authority': 'accountscenter.facebook.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'no-cache', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1', 'origin': 'https://accountscenter.facebook.com', 'pragma': 'no-cache', 'referer': 'https://accountscenter.facebook.com/password_and_security/two_factor', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.141", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.141"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"10.0.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-asbd-id': '129477', 'x-fb-friendly-name': 'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation', 'x-fb-lsd': self.lsd
		}

		data = {
		    'av': self.user,
		    '__user': self.user,
		    '__a': '1',
		    '__req': '1l',
		    '__hs': self.haste,
		    'dpr': '1',
		    '__ccg': 'MODERATE',
		    '__rev': self.client,
		    '__s': '',
		    '__hsi': self.hsi,
		    '__dyn': '',
		    '__csr': '',
		    '__comet_req': '5',
		    'fb_dtsg': self.dtsg,
		    'jazoest': self.jazoest,
		    'lsd': self.lsd,
		    '__spin_r': self.spin_r,
		    '__spin_b': 'trunk',
		    '__spin_t': self.spin_t,
		    'fb_api_caller_class': 'RelayModern',
		    'fb_api_req_friendly_name': 'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation',
		    'variables': '{"input":{"client_mutation_id":"%s","actor_id":"%s","account_id":"%s","account_type":"FACEBOOK","fdid":"device_id_fetch_datr"}}'%(self.client_id ,self.user, self.user),
		    'server_timestamps': 'true',
		    'doc_id': '5278198508948183',
		}

		post = rs.post('https://accountscenter.facebook.com/api/graphql/', cookies=self.cookies, headers=headers, data=data).text
		open('recovery.txt', 'w').write(post)
		if '"success":true' in post:
			all_code = re.search('"recovery_codes"\:\["(.*?)"\]', post).group(1).replace('"','').split(',')
			i = 1
			print('Recovery Code : ')
			for code in all_code:
				print('   %s. %s%s%s'%(i, h, code, p))
				i+=1
		else:
			print('%sFailled Get Recovery Code%s'%(m,p))



menu()