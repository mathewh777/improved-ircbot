import requests


def insult_gen():
  url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
  page = requests.get(url)
  data = page.json()
  return data['insult']
