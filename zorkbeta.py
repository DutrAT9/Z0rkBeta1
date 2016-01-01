import socket
import sys

print('''##########################################################
# [+] AUTOR:        Gabriel Dutra                        #
# [+] EMAIL:        gabrieldutra-08outlook.com           #
# [+] GITHUB:       https://github.com/gabrielD9         #
# [+] FACEBOOK:     https://fb.com/gabriel.dutra.47884754#
##########################################################''')
def is_port_open(host, port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host, port))
	except socket.error:
		return False
	return True

for port in range(21, 3306):
	if is_port_open(sys.argv[1], port):
		print("{}  <<Porta aberta".format(port))

print("*/*/*/*/*/*/*/FINALIZADO/*/*/*/*/*/*/*/*/*")
print("*/*/*/*/*/*/*/FINALIZADO/*/*/*/*/*/*/*/*/*")
print("*/*/*/*/*/*/*/FINALIZADO/*/*/*/*/*/*/*/*/*")
print("*/*/*/*/*/*/*/FINALIZADO/*/*/*/*/*/*/*/*/*")
