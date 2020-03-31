#!/usr/bin/python3
import sys, os

shell_status = True

def shell_loop():
	try:
		while shell_status:
			sys.stdout.write('> ')
			sys.stdout.flush()
			cmd = sys.stdin.readline()
			if cmd == 'c\n':
				os.system('clear')
			elif cmd == 'turn on\n':
				os.system('sudo usb_modeswitch -KW -v 0bda -p 1a2b')
			elif cmd == 'ls\n':
				os.system('ls')
			elif 'python' in cmd:
				os.system(cmd)
			elif cmd == 'date\n':
				os.system('date')
			elif cmd == 'pwd\n':
				os.system('pwd')
			elif cmd == 'exit\n':
				sys.exit(0)
			else:
				print('command not found')
	except KeyboardInterrupt:
		print('\nexiting...')
		sys.exit(0)


def main():
	shell_loop()

if __name__ == '__main__':
	main()
