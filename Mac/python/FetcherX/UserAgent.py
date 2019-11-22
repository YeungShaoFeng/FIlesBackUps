#! usr/bin/env
# -*- conding : utf-8 -*-

import re

headers_str = '''
Host: app.fetcherx.com
Connection: keep-alive
Accept: application/json, text/plain, */*
Authorization: U2FsdGVkX1/RYr0yU+l9X9SziyAH/EdPgZch5RVtv69+oKrG93xGsYiexrXurKZP
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
Content-Type: application/json
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://app.fetcherx.com/rss/ff1f152dad6ae34bd9bee68e786b1ea5
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: _ga=GA1.2.1982932786.1569031957; _gid=GA1.2.864363111.1572070323; _gat_gtag_UA_60788452_17=1
'''

pattern = '^(.*?): (.*)$'
for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))
print()