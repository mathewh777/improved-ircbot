from modules.ping_reply import ping_reply
from modules.welcome_msg import welcome_msg
from modules.randommusic import randommusicvideo
from modules.randomvideos import randomvideos
from modules.ducksearch import *
from modules.titlething import *
from modules.titlething import *

import re

def commands(s, channel, botnick):
    while True:
        msg = s.recv(1080)
        msg =  msg.decode('utf-8')
        what_to_do= msg.split()
        print(msg)
        #ansers ping
        if msg[:4].lower() == "ping":
            ping_reply(msg, s)
        #welcomes users
        if what_to_do[1] == "JOIN":
            welcome_msg(what_to_do, s, botnick, channel)
        # pretty shit oh well
        if what_to_do[1] == "PRIVMSG":
            if what_to_do[2] == channel:
                if what_to_do[3] == ':!help':
                    help_msg ="!random random videos, !music random music, !search for searching stuff, Also very slow"
                    helpmsg = "PRIVMSG "+channel+" :"+help_msg+"\r\n"
                    help_b =bytes(helpmsg, 'utf-8')
                    s.sendall(help_b)
        #:Cadaver!Cadaver@Clk-7CF111DB', 'PRIVMSG', '#test', ':!welp']
        if what_to_do[1] == "PRIVMSG":
            if what_to_do[2] == channel:
                if what_to_do[3] == ':!music':
                    music = randommusicvideo()
                    music_msg = "PRIVMSG "+channel+" :"+music+"\r\n"
                    s.sendall(music_msg.encode())

        if what_to_do[1] == "PRIVMSG":
            if what_to_do[2] == channel:
                if what_to_do[3] == ':!random':
                    random = randomvideos()
                    random_msg = "PRIVMSG "+channel+" :random links:"+random+"\r\n"
                    s.sendall(random_msg.encode())

        if what_to_do[1] == "PRIVMSG":
            if what_to_do[2] == channel:
                if what_to_do[3] == ':!search':
                    send_results(what_to_do, s)

        if what_to_do[1] == "PRIVMSG":
            if what_to_do[2] == channel:
                if what_to_do[3][:5] == ':http':
                    link_info(what_to_do, s, channel)
                    
        if what_to_do[1] == "PRIVMSG":
            if what_to_do[2] == channel:
                if what_to_do[3][:5] == ':!meme':
                    meme_url = meme_gen()
                    random_msg = "PRIVMSG "+channel+" :meme "+meme_url+"\r\n"
                    s.sendall(random_msg.encode())
                    
         if what_to_do[1] == "PRIVMSG":
            if what_to_do[2] == channel:
                if what_to_do[3][:5] == ':!insult':
                    insult = insult_gen()
                    random_msg = "PRIVMSG "+channel+" :insult "+insult+"\r\n"
                    s.sendall(random_msg.encode())
                    
                       
                     
                    
        
