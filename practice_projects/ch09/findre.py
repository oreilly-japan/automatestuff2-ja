# 演習プロジェクト 9.9.3

import os
import sys
import re

if len(sys.argv) < 2:
    sys.exit('使い方：python findre.py 正規表現パターン')

pattern = re.compile(sys.argv[1])

for filename in os.listdir('./'):
    if not filename.lower().endswith('.txt'):
        continue
    # テキストファイルを開く。文字コードはUTF-8とする。
    # シフトJISコードの場合は、encoding='shift_jis'としてください。
    txt_file = open(filename, 'r', encoding='utf-8')
    for line in txt_file:
        mo = pattern.search(line)
        if mo:
            print(filename, ':',  line, end='')
    txt_file.close()

