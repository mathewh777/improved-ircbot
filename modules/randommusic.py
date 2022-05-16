# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

def randommusicvideo():
    url = "https://randommusicvideos.com/category/genre/track/"
    youtube_search = "https://invidiou.site/search?q="


    header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    proxy = {
    'http' : "socks5://127.0.0.1:1337",
    'https' : "socks5://127.0.0.1:1337"
    #proxies=proxy
    }

    TAG_RE = re.compile(r'<[^>]+>')
    page = requests.get(url, proxies=proxy, headers=header, timeout=50, stream=True)
    soup = BeautifulSoup(page.content, 'lxml')
    title= soup.find('h3', class_="heading").get_text()
    song_title=title.replace("\n","").replace("\t", "").replace(" ", "+")

    page = requests.get(youtube_search+song_title, proxies=proxy, headers=header, timeout=50, stream=True)
    soup = BeautifulSoup(page.content, 'lxml')
    x=soup.find('div',class_="pure-u-1 pure-u-md-1-4")
    video_tags = x.__str__()
    video_tags_spitted = video_tags.split("\"")
    #video watch v? thing
    watch_link = video_tags_spitted[5]
    #time
    time_video  = TAG_RE.sub('',video_tags_spitted[16])
    time_video = time_video.replace(">", "").replace("\n\n\n<a href=", "")
    #title
    title = TAG_RE.sub('',video_tags_spitted[18].strip()).replace(">", "")
    title = title.replace("<a href=", "").replace("<p style=", "").replace("\n", "")
    #date
    date = TAG_RE.sub('',video_tags_spitted[36].strip()).replace(">", "")
    date = date.replace("\n<div class=", "")
    #views
    views = TAG_RE.sub('',video_tags_spitted[40].replace("\n", "").strip())
    views = views.replace(">","").replace(" ", "")

    youtube_url = "https://youtube.com"+watch_link
    invidiou_url= "https://invidiou.site"+watch_link

    format_Str = '{} {} {} {} {} {} '.format(youtube_url, invidiou_url, title,  time_video, views, date)

    return format_Str
