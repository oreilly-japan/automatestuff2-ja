#! python3
# quickWeather.py - コマンドラインに指定した地名の天気予報を表示する

import json, requests, sys

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# https://home.openweathermap.org/api_keysから取得したAPIキーを定義しておく
APPID='0123456789abcdef0123456789abcdef'
assert APPID != '', 'APPIDを定義してください。'

# OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
url = ('https://api.openweathermap.org/data/2.5/forecast/daily?'
       + f'q={location}&cnt=3&appid={APPID}')
response = requests.get(url)
response.raise_for_status()

# 生のJSONテキストを見るには次の行のコメントをはずす
#print(response.text)

# JSONデータからPython変数に読み込む
weather_data = json.loads(response.text)

# 整形したJSONテキストを見るには次の2行のコメントをはずす
#import pprint
#pprint.pprint(weather_data)

# 天気予報の情報を表示する
w = weather_data['list']  # ❶
print(f'{location}の現在の天気:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('明日:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('明後日:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


