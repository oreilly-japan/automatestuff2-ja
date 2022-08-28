# 演習プロジェクト 20.17.1 忙しそうに見せる

import pyautogui
import time

print('''10秒ごとにマウスカーソルを左右に少し動かします。
Ctrl-Cで終了します。''')

try:
    dir = -1
    while True:
        time.sleep(10)
        pyautogui.moveRel(dir, 0)
        dir = - dir

except KeyboardInterrupt:
    print('終了')

