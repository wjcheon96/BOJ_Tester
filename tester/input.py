import sys
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
addr = 'https://www.acmicpc.net/problem/'
addr += sys.argv[1]
data = requests.get(addr,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


for i in range(1,10):
    result = "sample-input-"
    result += str(i)
    test = soup.find("pre", {"id" : result})
    if (test != None):
        # buffer = soup.find("pre", {"id" : result}).text
        buffer = test.text
    else:
        break
    result = ""
    filename = "input"
    filename += str(i)
    filename +=".txt"
    f = open(filename, 'w')
    f.write(buffer)
    f.close()
    filename = ""