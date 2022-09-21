def encrypt(text, key):
	list = list(text)
	
	text_encrypted = ''

	for i in list:
		ord_c = (ord(i) - ord('A') + key) % 26
		
		text_encrypted += chr(ord_c + ord('A'))
	
	return text_encrypted

def decrypt(text, key):
	list = list(text)
	
	text_descriptografado = ''

	for i in list:
		ord_c = (ord(i) - ord('A') - key) % 26
		
		text_descriptografado += chr(ord_c + ord('A'))

	return text_descriptografado

print(encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23))
print(decrypt('XYZABCDEFGHIJKLMNOPQRSTUVW', 23))