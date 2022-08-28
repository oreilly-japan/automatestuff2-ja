# 演習プロジェクト 13.14.4  テキストからスプレッドシートへ変換
# ソースのテキストファイルは、gentxtfiles.py で作成してください。

import openpyxl
import os

# 新規のスプレッドシートを作る
new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

n = 0
for filename in sorted(os.listdir('.')):
    # 拡張子が.txtでなければスキップ
    if not filename.lower().endswith('.txt'):
        continue
    # ファイルごとに列番号を1,2,3,...と増やしていく
    n += 1
    text_file = open(filename, 'r', encoding='utf-8')
    # ファイルを開いて行に追加する
    for m,line in enumerate(text_file):
        new_sheet.cell(column=n, row=m + 1).value = line.strip()
    text_file.close()

# Excelファイルを保存する
new_wb.save('texts.xlsx')
