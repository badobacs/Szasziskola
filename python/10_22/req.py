# import webbrowser
import requests

r = requests.get('http://szasziskola.hu')

print(r.content)