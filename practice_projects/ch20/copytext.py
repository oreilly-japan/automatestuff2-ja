# 演習プロジェクト 20.17.2  メモ帳からのテキストコピー（Windowsのみ）

import sys
import pyautogui
import pyperclip

notepad_windows = pyautogui.getWindowsWithTitle('メモ帳')
if not notepad_windows:
    sys.exit('メモ帳が見つかりませんでした')

win = notepad_windows[0]
win.activate()
pyautogui.click(win.left + 100, win.top + 100)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
text = pyperclip.paste()
print(text)
