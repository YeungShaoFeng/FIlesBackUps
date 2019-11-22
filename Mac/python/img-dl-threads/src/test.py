from bs4 import BeautifulSoup
from requests import get as requests_get

url = 'https://www.xicidaili.com/nn/1'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
try:
    r = requests_get(url=url, headers=headers)
    r.raise_for_status
except:
    raise
soup = BeautifulSoup(r.text, 'lxml')

tds = soup.find_all('td')

proxies = {}

for i in range(len(tds)//10):
    i_10 = i * 10
    ip = tds[i_10 + 1].string
    port = tds[i_10 + 2].string
    if(ip and port):
        proxies[i] = {
            'http' : 'http://' + ip + ':' + port,
            'https' : 'https://' + ip + ':' + port
        }
print()