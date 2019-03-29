#!/usr/bin/env python3
# encoding: utf-8

import sys
import re
import urllib
import bs4
import pandas as pd
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://ru.ufpa.br/index.php?option=com_content&view=article&id=7'
url = urllib2.unquote(url).decode('utf8')
beautiful = urllib2.urlopen(url, timeout=3).read()
soup = bs4.BeautifulSoup(beautiful, 'lxml')
# print(soup.prettify())
file = open('ru.html','w')
file.write(soup.prettify('utf8'))
file.close()
# cardapio = re.sub("\n\s*\n*", "\n", soup.tbody.parent.text)
# print(cardapio)
data = []
table = soup.find_all('table')[4]
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
print(data)
