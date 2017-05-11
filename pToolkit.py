#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, binascii, random, string, hashlib, socket, urllib2

try:
	charset = string.ascii_letters + string.digits + '!@#$%^&*()'
	# creates charset for random password generator

	escape = '\033[1;m'
	blue = '\033[1;34m'
	cyan = '\033[1;36m'
	green = '\033[1;32m'
	grey = '\033[1;30m'
	magenta = '\033[1;35m'
	red = '\033[1;31m'
	white = '\033[1;37m'
	yellow = '\033[1;33m'
	# defines colours 

	platform = sys.platform
	if platform == 'win32' or platform == 'cygwin':
		def clear():
			os.system('cls')

		def banner():
			print cyan + '''
PTOOLKIT
			''' + escape

	else:
		def clear():
			os.system('clear')
			# windows compatability

		def banner():
			print cyan + '''
██████╗ ████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║ ██╔╝██║╚══██╔══╝
██████╔╝   ██║   ██║   ██║██║   ██║██║     █████╔╝ ██║   ██║
██╔═══╝    ██║   ██║   ██║██║   ██║██║     ██╔═██╗ ██║   ██║
██║        ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██╗██║   ██║
╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝
			''' + escape

	clear()
	banner()
	# creates clear function

	def dirScan(target, list):
		try:
			target = target.replace('http://', '')
			target = target.replace('https://', '')
			target = target.replace('/', '')
			target = 'http://' + target + '/'
			# changes target to valid url

			req = urllib2.Request(target)
			resp = urllib2.urlopen(req)
			# checks to see if target is valid

			clear()

			with open(list) as List:
				print 'Scanning... '
				for line in List:
					try:
						currentURL = target + line
						req = urllib2.Request(currentURL)
						resp = urllib2.urlopen(req)
						print currentURL

					except urllib2.HTTPError:
						pass
						# checks every url in list

		except urllib2.URLError:
			clear()
			print 'Invalid URL'
			main()

	def pScan(target, start, end):
		try:
			if 'http://' in target:
				target = target.replace('http://', '')

			elif 'https://' in target:
				target = target.replace('https://', '')

			else:
				pass

			target = socket.gethostbyaddr(target)
			target = str(target[2]).replace('[', '').replace(']', '').replace('\'', '')
			# makes url readable by socket

			clear()
			print 'Scanning... '

			for port in range(start, end + 1):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((target, port))
				# checks to see if port is open

				if result == 0:
					print 'Port %s:     Open' % port

				else:
					print 'Port %s:     Closed' % port

		except socket.gaierror:
			clear()
			print 'Invalid URL'
			main()

		except socket.error:
			clear()
			print 'Invalid URL'
			main()

	def hashGen(string):
		obj = hashlib.sha256(string)
		hash = obj.hexdigest()
		# creates hash

		clear()
		print hash
		main()

	def passGen(length):
		passwd = (''.join(random.choice(charset) for i in range(length)))
		# generates password

		clear()
		print passwd
		main()

	def hexConvert(type, value):
		try:
			if type == 'ascii':
				hexValue = ''
				for letter in value:
					hexValue = hexValue + format(ord(letter), "x") + ' '
					# goes through each letter and converts it to a hex decimal

				print hexValue
				main()

			elif type == 'hex':
				asciiValue = ''
				for dec in value.split():
					asciiValue = asciiValue + dec.decode('hex') + ' '
					# goes the each hex decimal and decodes it to ascii

				print asciiValue
				main()

			else:
				print 'Error'
				main()

		except TypeError:
			print 'Invalid entry'
			main()

	def binConvert(type, value):
		try:
			if type == 'ascii':
				binary = bin(int(binascii.hexlify(value), 16))
				# converts ascii to binary

				print binary
				main()

			elif type == 'binary':
				n = int(value, 2)
				string = binascii.unhexlify('%x' % n)
				# converts binary to ascii

				print string

			else:
				print 'Error'
				main()
				# checks to see if user chose ascii or binary and acts accordingly

		except ValueError:
			print 'Invalid entry'
			main()

	def main():
		print green + '\n(0) Exit'
		print '(1) Clear screen'
		print '(2) Banner'
		print '(3) Binary converter'
		print '(4) Hex converter'
		print '(5) Password generator'
		print '(6) SHA-256 hash generator'
		print '(7) Port scanner'
		print '(8) Directory scanner'

		option = raw_input('\n#> ')
		# asks user for tool to use

		if option == '0':
			clear()
			sys.exit()

		elif option == '1':
			clear()
			main()

		elif option == '2':
			clear()
			banner()
			main()

		elif option == '3':
			clear()
			conType = raw_input('(a)scii or (b)inary: ')
			
			if conType.lower() == 'a':
				string = raw_input('String: ')
				# asks user for string to convert

				clear()				
				binConvert('ascii', string)
				main()

			elif conType.lower() == 'b':
				binary = raw_input('Binary: ')
				# asks user for binary to convert

				clear()
				binConvert('binary', binary)
				main()

			else:
				clear()
				print 'Invalid argument'
				main()
				# checks if user is converting from ascii to binary or vise versa

		elif option == '4':
			clear()
			conType = raw_input('(a)scii or (h)ex: ')

			if conType.lower() == 'a':
				string = raw_input('String: ')

				clear()
				hexConvert('ascii', string)
				main()

			elif conType.lower() == 'h':
				hexString = raw_input('Hex: ')

				clear()
				hexConvert('hex', hexString)
				main()

			else:
				clear()
				print 'Invalid argument'
				main()
				# checks if user is converting from ascii to hex or vise versa

		elif option == '5':
			try:
				clear()
				length = raw_input('Length: ')
				passGen(length)

			except TypeError:
				clear()
				print 'Enter a valid length'
				main()

		elif option == '6':
			clear()
			string = raw_input('String: ')
			hashGen(string)

		elif option == '7':
			try:
				clear()
				target = raw_input('Target: ')
				start = raw_input('Starting port: ')
				end = raw_input('Ending port: ')
				pScan(target, int(start), int(end))

			except ValueError:
				clear()
				print 'Enter a valid port'
				main()

		elif option == '8':
			clear()
			target = raw_input('Target: ')
			dirList = raw_input('Directory list: ')

			if os.path.isfile(dirList) != True:
				clear()
				print 'Invalid wordlist'
				main()

			else:
				pass
				# checks if wordlist exists

			dirScan(target, dirList)

		else:
			clear()
			print 'Invalid argument'
			main()
			# checks what the user entered

	main()

except KeyboardInterrupt:
	sys.exit()
	# makes for clean exit on press of CTRL+C