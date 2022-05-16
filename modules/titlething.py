import re
import requests
from bs4 import BeautifulSoup

#def link_info(what_to_do, s, channel):
def link_info(what_to_do, s, channel):
    what_to_do = ' '.join(what_to_do)
    proxy = {
    'http' : "socks5://127.0.0.1:1337",
    'https' : "socks5://127.0.0.1:1337"
    }
    header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    url =  re.findall("https?[:\/\/.*\.+](?!\.onion|\.onion)[^\s]{2,}", what_to_do)
    try:
        for a_url in url:
          print(a_url)
          url = ''.join(a_url)
          html= requests.get(url,proxies=proxy, headers=header, timeout=10)
          soup = BeautifulSoup(html.content, 'html.parser')
          for x in soup.find_all('title', text=True):
              if x == None:
            	  pass
              else:
                 url = x.get_text()
                 url = url.replace('\n', ' ').replace('\r',' ')
                 url = url.replace(".onion", "")
                 urlmsg = "PRIVMSG "+channel+" :"+url+"\r\n"
                 #print(url)
                 s.sendall(urlmsg.encode('utf-8'))
    except:
        pass
