import pyautogui, time
time.sleep(5)  # ❶ 
pyautogui.click()  # お絵かきアプリをクリックしてフォーカスする ❷
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # 右へ移動 ❸
    distance = distance - change  # ❹ 
    pyautogui.drag(0, distance, duration=0.2)   # 下へ移動 ❺
    pyautogui.drag(-distance, 0, duration=0.2)  # 左へ移動 ❻
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # 上へ移動
