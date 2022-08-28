# 演習プロジェクト 9.9.2 作文ジェネレータ（日本語版）

import sys
import re

if len(sys.argv) < 2:
    sys.exit('''使い方: python jsentence_generator.py src.txt
src.txtの文字コードはUTF-8
''')

# テキストファイルをすべて読み込む
src_file = open(sys.argv[1], 'r', encoding='utf-8')
src_data = src_file.read()
src_file.close()

# 置き換える文字列
pattern = re.compile(r'(形容詞|名詞|動詞|形容動詞|副詞)')

while True:
    # 出現順にユーザに問い合わせる
    mo = pattern.search(src_data)
    if not mo:
        break

    # プロンプトを表示して、入力を受け付ける。
    repl = input(mo.group(1).lower() + 'を入力してください: ')

    # ひとつだけ置換する
    src_data = src_data.replace(mo.group(1), repl, 1)

# 置換結果を画面に表示する
print(src_data, end='')

# テキストファイルに保存する
dst_file = open(sys.argv[1] + '.generated.txt', 'w', encoding='utf-8')
dst_file.write(src_data)
dst_file.close()

