import socket
import threading
import pdb
from mqtt import MQTTClient

PORT = 5050
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(
    socket.AF_INET,         # socket family/category: IPv4
    socket.SOCK_STREAM      # type of socket
)
server.bind(ADDR)

mqttclient = MQTTClient('Name1')


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    json_dic = {}

    while True:
        msg = conn.recv(1024)   # receive byte-array
        if msg:
            #            pdb.set_trace()
            print(f'total byte length: {len(msg)}')
            if len(msg) < 1024:
                print("okay")
    conn.close()


def start():
    mqttclient.start()
    server.listen(1)
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()    # wait for a new connection to come
        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

        # for testing purpose
        # in real server, we will never call join() and break
        thread.join()
        print(f"[STOPPED]")
        break
    mqttclient.stop()


if __name__ == '__main__':
    print("[STARTING] server is starting...")
    start()
