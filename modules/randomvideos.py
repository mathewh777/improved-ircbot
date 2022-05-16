#random youtube videos
#https://random-ize.com/random-youtube/
#random youtube music videos
#https://amitness.com/shuffle/
from bs4 import BeautifulSoup
import requests

def randomvideos():

    url = "https://random-ize.com/random-youtube/"
    invid = "https://invidiou.site/watch?v="
    youtu = "https://youtube.com/watch?v="

    header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    proxy = {
    'http' : "socks5://127.0.0.1:1337",
    'https' : "socks5://127.0.0.1:1337"
    #proxies=proxy
    }

    page = requests.get(url, proxies=proxy, headers=header, timeout=50, stream=True)
    soup = BeautifulSoup(page.content, 'lxml')
    iframe = soup.find("iframe", allowfullscreen="")
    iframe = iframe.__str__()
    spitted = iframe.split("=")
    url = spitted[4].split()
    if "?max-results" in url[0]:
        return "max results please wait 5 mins";
    else:
        video_number = url[0].split("/")
        links = invid+video_number[4][:11]+" "+youtu+video_number[4][:11]

    return links
