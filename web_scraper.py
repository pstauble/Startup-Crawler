from bs4 import BeautifulSoup
import requests

url=raw_input("Enter a website to extract the URL's from: ")
title=raw_input("What is the name of the artist you are looking for?")

r=requests.get("http://"+url)

data=r.text

soup=BeautifulSoup(data)

print soup.find_all(title)