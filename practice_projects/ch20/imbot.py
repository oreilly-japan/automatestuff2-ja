# 演習プロジェクト 20.17.3  Google Chatの自動操作
#
#  Google Chatを使って複数ユーザにメッセージを送信するプログラム。
#
#  Google Chatのウィンドウを表示した状態で、
#  次のように本プログラムを実行すると、メッセージを送信できます。
#     python imbot.py "メッセージ" ユーザ名1 ...
#  動作中は、マウスを触らないようにしてください。
#

import pyautogui
import pyperclip
import sys
import time

# pyautogui.write()では日本語を入力できないので、
# クリップボード経由でペーストする
def write2(s):
    saved_clipboard = pyperclip.paste()
    pyperclip.copy(s)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy(saved_clipboard)

# ユーザに、メッセージを送信する。
def send_message(user, message):
    # ESCでチャットからフォーカスをはずし、
    # ショートカット '/' を押して検索キーにフォーカス
    pyautogui.write(['esc', '/'], 1)
    # ユーザ名を入力し、↓キーで第1候補を選択
    write2(user)
    time.sleep(1)
    pyautogui.write(['down', 'enter'], 0.5)
    time.sleep(2)
    # メッセージを送信
    print(f'{user}に送信中。')
    write2(message)
    pyautogui.write('\n')
    time.sleep(5)

if len(sys.argv) < 3:
    sys.exit('使い方: python imbot.py "メッセージ" ユーザ名1 ...' )

try:
    # Google Chatのウィンドウを前面に出す。Windowsのみ。
    chat_win = pyautogui.getWindowsWithTitle('Chat')
    chat_win[0].activate()
except:
    print('5秒以内に、Google Chatのウィンドウをクリックしてください')
    time.sleep(5)

message = sys.argv[1]
for user in sys.argv[2:]:
    send_message(user, message)
