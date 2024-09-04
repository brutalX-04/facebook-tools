from tools.bahan import *


# --> Create Encpass
def password(data, pw):
	try:
		teme = re.search('"__spin_t":(.*?),', str(data)).group(1)
		publ = re.search('publicKey:"(.*?)",', str(data)).group(1)
		pubk = re.search('keyId:(.*?)}', str(data)).group(1)
		rdb = RDM.get_random_bytes(32)
		dpt = AES.new(rdb, AES.MODE_GCM, nonce=bytes([0]*12), mac_len=16)
		dpt.update(str(teme).encode("utf-8"))
		epw, ctg = dpt.encrypt_and_digest(pw.encode("utf-8"))
		sld = SB(PK(binascii.unhexlify(str(publ)))).encrypt(rdb)
		ecp = base64.b64encode(bytes([1,int(pubk),*list(struct.pack('<h', len(sld))),*list(sld),*list(ctg),*list(epw)])).decode("utf-8")
		encp = '#PWD_BROWSER:5:%s:%s'%(teme,str(ecp))
		return encp

	except Exception as e:print(e)
