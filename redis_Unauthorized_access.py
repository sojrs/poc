# -*- coding:utf-8  -*-
import socket
import optparse

def check(hostname,portname):
	s = socket.socket()
	socket.setdefaulttimeout(10)
	host = hostname
	port = portname
	try:
		payload ='\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'.encode()   #info
		s.connect((host,port))
		s.send(payload)
		recvdata = s.recv(1024).decode()
		if 'redis_version' in recvdata:
			print(host+':'+str(port)+'    have redis unauthorized access vuln')
		else:
			print('no redis unauthorized access vuln')
	except Exception as e:
		print(e)
	finally:
		s.close()

def main():
	try:
		parser = optparse.OptionParser(usage='python redis_Unauthorized_access.py -H ip -p port\nps:need python3')
		parser.add_option('-H',dest='host',type='str',help='ip_address please')
		parser.add_option('-p',dest='port',type='int',help='redis_port please')
		(options,args) = parser.parse_args()
		host = options.host
		port = options.port
	except:
		print(parser.usage)
		exit(0)
	check(host, port)

if __name__ == '__main__':
	main()

