#https://duckduckgo.com/?q=REPLACE&ia=web
#<div class="result__extras__url" bis_skin_checked="1">
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def duck_search(what_to_do):
    get_nick = what_to_do[0]
    get_nick = get_nick.split("!")
    nick = get_nick[0][1:]
    query = what_to_do[4:]
    query = '+'.join(query)
    duck_search = "https://duckduckgo.com/html/?q=REPLACE"
    search_results_ = b''
    header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    proxy = {
    'http' : "socks5://127.0.0.1:1337",
    'https' : "socks5://127.0.0.1:1337"
    }
    search_query = duck_search.replace("REPLACE", query)

    page = requests.get(search_query, proxies=proxy, headers=header)
    soup = BeautifulSoup(page.text, 'lxml')
    for search_results in soup.find_all("a", class_="result__a"):
        search_results_text = search_results.get_text()
        search_results_ += search_results_text.encode('utf-8')
        search_results_ += " ".encode()
        search_results_ += search_results['href'].encode()
        search_results_ += "(9)".encode()


    return nick, search_results_;

def send_results(what_to_do, s):
    nick, duck = duck_search(what_to_do)
    a=duck.decode('utf-8')
    split = a.split("(9)")
    for x in split:
        msg_results = "PRIVMSG " + nick+" :"+x+"\r\n"
        s.sendall(msg_results.encode('utf-8'))

#send_results([':Cadaver!Cadaver@Clk-7CF111DB', 'PRIVMSG','#test', ':!search', 'Stupid', 'shit'])
