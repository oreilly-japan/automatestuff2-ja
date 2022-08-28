# 演習プロジェクト 9.9.2 作文ジェネレータ（英語版）

import sys
import re

if len(sys.argv) < 2:
    sys.exit('Usage: sentence_generator.py src.txt')

# テキストファイルをすべて読み込む
src_file = open(sys.argv[1], 'r')
src_data = src_file.read()
src_file.close()

# 置き換える文字列
pattern = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')

while True:
    # 出現順にユーザに問い合わせる
    mo = pattern.search(src_data)
    if not mo:
        break

    # プロンプトを表示して、入力を受け付ける。
    print('Enter a', end='')
    # ADJECTIVE と ADVERB の場合は、冠詞を an にする
    if mo.group(1)[0] == 'A':
        print('n', end='')
    repl = input(mo.group(1).lower() + ': ')

    # ひとつだけ置換する
    src_data = src_data.replace(mo.group(1), repl, 1)

# 置換結果を画面に表示する
print(src_data, end='')

# テキストファイルに保存する
dst_file = open(sys.argv[1] + '.generated.txt', 'w')
dst_file.write(src_data)
dst_file.close()

