#! python3
# formFiller.py - フォームの自動入力

import pyautogui, time

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
              'robocop': 4, 'comments': 'Tell Bob I said hi.'},
             {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
              'comments': 'n/a'},
             {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
              'robocop': 1,
              'comments': 'Please take the puppets out of the break room.'},
             {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
             'robocop': 5,
              'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
             ]

pyautogui.PAUSE = 0.5
print('ブラウザウィンドウがアクティブでありフォームが読み込まれていることを確認してください！')

for person in form_data:
    # ユーザーがスクリプトを中断する機会を与える
    print('>>> 5秒間一時停止中。中断するにはCtrl-Cを押してください。<<<')
    time.sleep(5) # ❶

    print(f'{person["name"]}の情報を入力中...')  # ❶
    pyautogui.write(['\t', '\t'])  # ❷

    # Name欄を入力する
    pyautogui.write(person['name'] + '\t')  # ❸

    # Greatest Fear(s)欄を入力する
    pyautogui.write(person['fear'] + '\t')  # ❹

    # Source of Wizard Powers欄を選択する
    if person['source'] == 'wand':  # ❶
        pyautogui.write(['down', 'enter', '\t'], 0.5)  # ❷
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)

    # RoboCop欄を選択する
    if person['robocop'] == 1:  # ❸
        pyautogui.write([' ', '\t', '\t'], 0.5)  # ❹
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)

    # Additional Comments欄を入力する
    pyautogui.write(person['comments'] + '\t')

    # Submitをクリックする
    time.sleep(0.5) # ボタンが有効になるのを待つ
    pyautogui.press('enter')

    # 次のページが読み込まれるのを待つ
    print('フォームを送信しました。')
    time.sleep(5)

    # Submit another responseリンクをクリックする
    pyautogui.write(['\t', 'enter'], 0.5)

