#! python3
# countdown.py - シンプルなカウントダウンスクリプト

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

# カウントダウン後に音声ファイルを再生する
subprocess.run(['start', 'alarm.wav'], shell=True)
