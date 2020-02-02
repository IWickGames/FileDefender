import os
import sys
import subprocess
import hashlib
import random
import urllib.request
import base64

def sendReport(errorMessage):
	#Char settings
	pswLen = 20
	errorCode = ''
	charsString = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	chars = []
	chars[:0] = charsString
	#-------------

	pcInformation = subprocess.check_output('systeminfo | findstr /c:"System Type" /c:"Product ID" /c:"System Manufacturer"', shell=True)

	hash_object = hashlib.sha512(pcInformation)
	pcKey = hash_object.hexdigest()

	#Gen random errorCode
	for i in range(0, pswLen):
		numChar = random.randint(0,int(len(chars)-1))
		errorCode += chars[numChar]
	
	#Encode the error message into base64
	bytes = errorMessage.encode('ascii')
	base64_bytes = base64.b64encode(bytes)
	base64_output = base64_bytes.decode('ascii')

	url = 'http://filedefender.us.to/fdErr/id=' + str(pcKey) + '/errCode=' + str(errorCode) + '/error=' + str(base64_output)
	urllib.request.urlretrieve(url)
	
	return errorCode;