#encoding: utf-8
import requests
from lxml import etree
import json

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}
response = requests.get("https://movie.douban.com/cinema/nowplaying/pingxiang/",headers=headers)

text = response.text

parser = etree.HTML(text)

lis = parser.xpath("//li[@data-category='nowplaying']")

movies = []
for li in lis:
    movie = {}
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    img = li.xpath(".//img/@src")[0]
    movie['title'] = title
    movie['score'] = score
    movie['director'] = director
    movie['actors'] = actors
    movie['img'] = img
    movies.append(movie)

with open("movies.json",'w',encoding='utf-8') as fp:
    json.dump(movies,fp,ensure_ascii=False)



