#originally forked from mahej/udp_server.py
import logging
import socket

log = logging.getLogger('tcp_server')
port=1232
host='127.0.0.1'
def tcp_server(host=host, port=port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    log.info("Listening on tcp %s:%s" % (host, port))
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        data = conn.recv(128*1024)
        #(data, addr) = s.recvfrom(128*1024)
        yield data


FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)

for data in tcp_server():
    log.debug("%r" % (data,))