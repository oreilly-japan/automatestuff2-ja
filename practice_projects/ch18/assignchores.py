# 演習プロジェクト 18.10.1
# ・雑用を作業員にランダムに割り当てる
# ・前回と同じ作業を割り当てないようにする
#
# なお、1週間に1回、自動実行するスケジューリングは実装していない。
# タスクスケジューラやcronなど、外部のプログラムでスケジュール実行
# する必要がある。

import smtplib
from email.header import Header
from email.mime.text import MIMEText
import shelve
import random
import sys

SMTP_SERVER = 'YOUR_SMTP'     # SMTPサーバアドレスを設定
SMTP_PORT = 587               # SMTPサーバポート番号を設定
MY_ADDRESS = 'YOUR_ADDRESS'   # IDを設定
MY_PASSWORD = 'YOUR_PASSWORD' # パスワードを設定

SUBJECT = '作業指示'
MESSAGE = 'あなたの作業は{}です。'

# 雑用リスト
chores = ['皿洗い', 'トイレ掃除', '掃除機掛け', '犬の散歩']

# 作業員のメールアドレス　（雑用と同じ数が必要）
addresses = ['worker1@mailer', 'worker2@mailer',
             'worker3@mailer', 'worker4@mailer']

assert len(chores) == len(addresses), '雑用リストと送り先アドレスは同じ数である必要があります。'
assert len(addresses) >= 1, '雑用リストと送り先アドレスは1つ以上必要です。'
assert len(addresses) == len(set(addresses)), '送り先アドレスは重複してはいけません。'

def send_mail(to_address, chore):
    """ to_address に雑用choreをメールする """
    message = MESSAGE.format(chore)
    print('送信中', to_address, message)

    charset = 'iso-2022-jp'
    msg = MIMEText(message, 'plain', charset)
    msg['Subject'] = Header(SUBJECT.encode(charset), charset)

    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(MY_ADDRESS, MY_PASSWORD)
    smtp_obj.sendmail(MY_ADDRESS, to_address, msg.as_string())
    smtp_obj.quit()


# 雑用が1つのときは、メールを送っておしまい
if len(chores) == 1:
    send_mail(addresses[0], chores[0])
    sys.exit()

# 雑用割り当て
assign = {}
# 前回の雑用割り当て記録
last_assign = shelve.open('last_assign')

while True:
    # 割り当てのやりなおしに備えてコピーを作って作業
    rest_chores = list(chores)
    rest_addresses = list(addresses)

    # 残りがひとつになるまで、ランダムに割り当て
    while len(rest_chores) > 1:
        chore = random.choice(rest_chores)
        address = random.choice(rest_addresses)

        # 前回と同じなら、やりなおし
        if address in last_assign and last_assign[address] == chore:
            continue

        # 割り当て
        assign[address] = chore
        rest_chores.remove(chore)
        rest_addresses.remove(address)

    # 最後のひとつが前回と同じなら、最初からやりなおし
    chore = rest_chores[0]
    address = rest_addresses[0]
    if address in last_assign and last_assign[address] == chore:
        assign = {}
        continue

    # うまく割り当てられたらループを抜ける
    assign[address] = chore
    break


# 割り当てに成功したら、ひとりずつメールし、記録する
for address in sorted(assign.keys()):
    send_mail(address, assign[address])
    last_assign[address] = chore

# 記録を保存する
last_assign.close()

