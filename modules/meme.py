import requests

def meme_gen():
  url = "http://meme-api.herokuapp.com/gimme"
  page = requests.get(url)
  data = page.json()
  return data['url']
