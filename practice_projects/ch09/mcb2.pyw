# 演習プロジェクト 9.9.1 
# mcb2.pyw - クリップボードのテキストを保存・復元
#
# Usage:
# py.exe mcb2.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
# py.exe mcb2.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb2.pyw list - 全キーワードをクリップボードにコピー
#
# 以下、演習プロジェクトで追加した機能
# py.exe mcb2.pyw delete <keyword> - キーワードに紐づけられたテキストを削除
# py.exe mcb2.pyw delete all - すべてのテキストを削除

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':  # 削除機能
        if sys.argv[2].lower() == 'all':
           mcb_shelf.clear()          # 全削除
        else:
           del mcb_shelf[sys.argv[2]] # 指定したキーワードのテキストを削除
elif len(sys.argv) == 2:
    # キーワード一覧と、内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
else:
    print("""使い方：
py.exe mcb2.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
py.exe mcb2.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
py.exe mcb2.pyw list - 全キーワードをクリップボードにコピー
py.exe mcb2.pyw delete <keyword> - キーワードに紐づけられたテキストを削除
py.exe mcb2.pyw delete all - すべてのテキストを削除
""")

mcb_shelf.close()
