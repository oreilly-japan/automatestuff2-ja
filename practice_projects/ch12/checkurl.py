# 演習プロジェクト 12.11.4

import os
import sys
import requests
import bs4
import re
from urllib.parse import urljoin

if len(sys.argv) != 2:
    sys.exit('使い方: python checkurl.py URL')

DIR = 'files'
os.makedirs(DIR, exist_ok=True)

url = sys.argv[1]

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
# aタグを検索する
links = soup.select('a')

href_set = set()

for link in links:
    # aタグのhref属性を取得する
    href = link.get('href')
    if not href:
        continue

    # リンクが http で始まっていない相対パスのとき、正規化する
    if not href.startswith('http'):
        href = urljoin(url, href)

    # '#ラベル' を削除する
    href = re.sub(r'(#.+)', '', href)

    # 過去にダウンロードしたURLは省く
    if href in href_set:
        continue
    href_set.add(href)

    print(href, end='', flush=True)

    try:
        # リンク先をダウンロード
        res = requests.get(href)
        if res.status_code == 404:
            print(' -> 404 Not Found')
        elif res.status_code == 200:
            # hrefの冒頭の'http(s)://'をとる。
            filename = re.sub(r'^(https?://)', '', href)
            # パスに使えない文字を_に変換してファイル名にする
            filename = re.sub(r'[/~?&+]', '_', filename)
            hfile = open(os.path.join(DIR, filename), 'wb')
            for chunk in res.iter_content(100000):
               hfile.write(chunk)
            hfile.close()
            print(' ->', filename, 'に保存')
    except KeyboardInterrupt:
        print('\n中断しました。')
        break
    except:
        print(' -> Error')
