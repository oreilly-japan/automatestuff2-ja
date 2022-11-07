#! python3
# formFiller.py - フォームの自動入力

import pyautogui, time, pyperclip

# pyperclip.write()の代わり
def mywrite(s):
    saved_clipboard = pyperclip.paste()
    pyperclip.copy(s)
    pyautogui.hotkey('ctrl', 'v') # macOSの場合は 'command'
    pyperclip.copy(saved_clipboard)

form_data = [
  {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
   'robocop': 4, 'comments': 'Tell Bob I said hi.'},
  {'name': 'Bob', 'fear': 'bees', 'source': 'amulet',
   'robocop': 4,  'comments': 'n/a'},
  {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
   'robocop': 1,
   'comments': 'Please take the puppets out of the break room.'},
  {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
   'robocop': 5,
   'comments':
     'Protect the innocent. Serve the public trust. Uphold the law.'},
]

pyautogui.PAUSE = 0.5
print('ブラウザウィンドウがアクティブでありフォームが読み込まれていることを確認してください！')

for person in form_data:
    # ユーザーがスクリプトを中断する機会を与える
    print('>>> 5秒間一時停止中。中断するにはCtrl-Cを押してください。<<<')
    time.sleep(5) # ❶

    print(f'{person["name"]}の情報を入力中...')  # ❶
    pyautogui.write('\t' * 4)  # ❷

    # Name欄を入力する
    mywrite(person['name'])  # ❸
    pyautogui.write('\t')  # ❸

    # Greatest Fear(s)欄を入力する
    mywrite(person['fear'])  # ❹
    pyautogui.write('\t')  # ❹

    # Source of Wizard Powers欄を選択する
    n = ['wand', 'amulet',
         'crystal ball', 'money'].index(person['source']) # ❶
    pyautogui.write(['down'] * (n + 1) + ['enter', '\t'], 0.5)  # ❷

    # RoboCop欄を選択する
    robocop = person['robocop'] # ❸
    pyautogui.write([' '] + ['right'] * (robocop-1) + '\t'*2, 0.5)  # ❹

    # Additional Comments欄を入力する
    mywrite(person['comments'])
    pyautogui.write('\t')

    # Submitをクリックする
    time.sleep(0.5) # ボタンが有効になるのを待つ
    pyautogui.press('enter')

    # 次のページが読み込まれるのを待つ
    print('フォームを送信しました。')
    time.sleep(5)

    # Submit another responseリンクをクリックする
    pyautogui.write(['\t', 'enter'], 0.5)

