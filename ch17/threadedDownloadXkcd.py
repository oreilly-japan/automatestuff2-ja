#! python3
# threadedDownloadXkcd.py - XKCDコミックをマルチスレッドでダウンロードする

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)       # ./xkcdにコミックを保存 ❶

def download_xkcd(start_comic, end_comic):  # ❷
    for url_number in range(start_comic, end_comic):  # ❸
        # ページをダウンロードする
        print(f'ページをダウンロード中 https://xkcd.com/{url_number}...')
        res = requests.get(f'https://xkcd.com/{url_number}')  # ❹
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')     # ❺

        # コミック画像のURLを見つける
        comic_elem = soup.select('#comic img')   # ❻
        if comic_elem == []:
            print('コミック画像が見つかりませんでした。')
        else:
            comic_url = 'https:' + comic_elem[0].get('src')  # ❼
            # 画像をダウンロードする
            print(f'画像をダウンロード中 {comic_url}...')
            res = requests.get(comic_url)        # ❽
            res.raise_for_status()

            # 画像を./xkcdに保存する
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

# `Thread`オブジェクトを生成して開始する
download_threads = []            # 全Threadオブジェクトのリスト
for i in range(0, 140, 10):      # 14回ループし、14個のスレッドを生成
    start = i
    end = i + 9
    if start == 0:
        start = 1 # 0番はないので、1にする。
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# すべてのスレッドが終了するのを待つ
for download_thread in download_threads:
    download_thread.join()
print('完了')

