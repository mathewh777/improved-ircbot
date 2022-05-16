from modules.commands import commands
from modules.ping_reply import ping_reply

import socket
import socks
import time

botnick = "memetestbot"
channel = "#bot"

#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1337, True)
#socket.socket = socks.socksocket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('irc.styxnet.tech', 6667))

s.sendall(("USER " + botnick + " " + botnick + " " + botnick + " :boti!"+"\r\n").encode())
time.sleep(4)
s.sendall(("NICK " + botnick+"\r\n").encode())
msg = s.recv(600)
msg = msg.decode('utf-8')


if msg[:4].lower() == "ping":
    ping_reply(msg, s)
time.sleep(4)

s.sendall(("NICK " + botnick+"\r\n").encode())
s.sendall(("JOIN " + channel+"\r\n").encode())
msg = s.recv(1048)
s.recv(1048)

commands(s, channel, botnick)
