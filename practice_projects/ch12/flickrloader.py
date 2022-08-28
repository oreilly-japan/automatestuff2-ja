# 演習プロジェクト 12.11.2
# Flickrからキーワード検索して、画像をダウンロードする。

import sys
import requests
import bs4
import re
import os

if len(sys.argv) < 2:
    sys.exit('''使い方: python filckrloader.py キーワード ...
例）python flickerloader.py white cat
''')

MAX_IMAGES = 10   # 最大枚数

DIR = 'images'    # 保存先フォルダ
os.makedirs(DIR, exist_ok=True)

# 引数をつなげる
keyword = ' '.join(sys.argv[1:])

# Flickrを検索する
res = requests.get('https://www.flickr.com/search/?text=' + keyword)
res.raise_for_status()

# 解析用にHTMLソースを保存
# with open('flicker.html', 'w', encoding='utf-8') as f:
#    f.write(res.text)

# <div class="photo-list-photo-view">...<img src="img_url">を検索
soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgs = soup.select('.photo-list-photo-view img')

for i in range(min(MAX_IMAGES, len(imgs))):
    img_url = imgs[i].get('src')
    print('https:' + img_url)

    # 画像をダウンロード
    img_res = requests.get('https:' + img_url)
    img_res.raise_for_status()
    img_file = open(os.path.join(DIR, os.path.basename(img_url)), 'wb')
    for chunk in img_res.iter_content(100000):
        img_file.write(chunk)
    img_file.close()

