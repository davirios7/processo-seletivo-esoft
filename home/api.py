import requests as req


def nomeAleatorio():
  response = req.get('https://gerador-nomes.wolan.net/nome/aleatorio')
  text = response.json()
  nome = list(text)[0]
  sobrenome = list(text)[1]
  nomeSobre = nome + " " + sobrenome
  return nomeSobre