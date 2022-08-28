# 演習プロジェクト 15.7.3 総当たりで暗号解除

import sys
import PyPDF2

if len(sys.argv) < 3:
    sys.exit('Usage: python bfkeysearch.py encrypted.pdf dictionary.txt')

pdf = sys.argv[1]  # 暗号PDFファイル名
dic = sys.argv[2]  # 辞書ファイル名

# PDFファイルを開く。暗号化されていなければ終了
pdf_file = open(pdf, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
if not pdf_reader.isEncrypted:
    sys.exit('エラー: {} は暗号化されていません。'.format(pdf_file))

i = 0
# 辞書ファイルを開いて1行ずつパスワードとして解除を試みる
dic_file = open(dic, 'r')
for key in dic_file:
    # 前後の空白や改行文字をとり、小文字化する
    key = key.strip().lower()
    if pdf_reader.decrypt(key):
        print('パスワードは', key)
        break
    # 大文字化する
    key = key.upper()
    if pdf_reader.decrypt(key):
        print('パスワードは', key)
        break

    if i % 1000 == 0:
        print(key)
    i += 1

else:
    print('パスワードが見つかりませんでした。')
    # for～else は、breakでループから抜けず最後まで繰り返した場合に実行される。

