# 演習プロジェクト 17.12.1 ストップウォッチプログラム改造版
# 本文では、rjust() を用いるというヒントが記載されていますが、
# f文字列のフォーマットを使うほうが簡単です。

import time
import pyperclip

# プログラムの説明を表示する
print('Enterを押すと開始します。その後、Enterを押せば経過時間を表示します。Ctrl-Cで終了します。')
input()                    # Enterを押すと開始
print('スタート')
start_time = time.time()   # プログラムと最初のラップの開始時間
last_time = start_time
lap_num = 1

# ラップタイムを計測する
try:
    while True:
        input()
        now = time.time()

#        #rjust()を使う場合。ただし1桁のときにずれるバグがある。
#        lap_time = str(round(now - last_time, 2)).rjust(5, ' ')
#        total_time = str(round(now - start_time, 2)).rjust(6, ' ')
#        s = 'ラップ #{}: {} ({})'.format(lap_num, total_time, lap_time)

        lap_time = now - last_time
        total_time = now - start_time
        s = f'ラップ #{lap_num:2}: {total_time:5.2f} ({lap_time:6.2f})'

        last_time = now  # ラップタイムをリセット
        lap_num += 1

        print(s, end='')
        #クリップボードにコピー
        pyperclip.copy(s)

except KeyboardInterrupt:
    # Ctrl-C例外を処理してエラーメッセージを表示しないようにする
    print('\n終了.')

