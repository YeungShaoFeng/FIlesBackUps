from re import compile as re_compile
from requests import get as requests_get
from xml.dom.minidom import parse
import xml.dom.minidom


def getXML():
    url = "http://app.fetcherx.com/sitemap.xml"

    r = requests_get(url)

    r.encoding = r.apparent_encoding

    with open("sitemap.xml", "w") as f:
        f.write(r.text)


def getLocs():
    DOMTree = parse(r'./sitemap.xml')
    collection = DOMTree.documentElement
    urls = collection.getElementsByTagName('url')
    links = []

    for url in urls:
        links.append(url.getElementsByTagName('loc')[0].childNodes[0].data)

    return links


def main():
    locs = getLocs()
    with open('./urls.json')
    print(locs)

https://app.fetcherx.com/post/bookmark/DzqZ3r8qg
if __name__ == '__main__':
    main()
