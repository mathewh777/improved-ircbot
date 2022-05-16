import time

def ping_reply(msg, s):
    msg = msg.split(":")
    pong = 'PONG :'+msg[1]
    time.sleep(2)
    s.sendall(pong.encode())
