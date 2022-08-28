# 演習プロジェクト 12.11.1
#  Yahoo!メールでメッセージを送る

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

if len(sys.argv) < 3:
    sys.exit('使い方: python 宛先 メッセージ...')

to_address = sys.argv[1]
message = ' '.join(sys.argv[2:])

MY_ADDRESS = 'YOUR_ID' # 書き換えてください
MY_PASSWORD = 'YOUR_PASSWORD' # 書き換えてください

browser = webdriver.Firefox()
browser.get('https://mail.yahoo.co.jp')

time.sleep(5)

# IDの入力
id_input = browser.find_element(By.ID, 'username')
id_input.send_keys(MY_ADDRESS)
next = browser.find_element(By.ID, 'btnNext')
next.click()
# ちょっと待つ。WebDriverWait.until を使うほうがよいが省略。
time.sleep(5)

# パスワードの入力
password_input = browser.find_element(By.NAME, 'passwd')
password_input.send_keys(MY_PASSWORD)
next = browser.find_element(By.ID, 'btnSubmit')
next.click()
time.sleep(15)

# 「作成」ボタンを押す
comp = browser.find_element(By.CSS_SELECTOR,
                            'button[data-cy="composeButton"]')
comp.click()
time.sleep(5)

# To: を入力
to_input = browser.find_element(By.CSS_SELECTOR,
                                'input[data-cy="composeToInput"]')
to_input.send_keys(to_address + '\n')
time.sleep(1)

# 件名を入力
subject_input = browser.find_element(By.CSS_SELECTOR,
                                     'input[data-cy="composeSubjectInput"]')
subject_input.send_keys('自動送信')
time.sleep(1)

# メッセージ本文を入力
message_text = browser.find_element(By.CSS_SELECTOR,
                                    'textarea[data-cy="composeBody"]')
message_text.send_keys(message)
time.sleep(5)

# 「送信」ボタンを押す
send = browser.find_element(By.CSS_SELECTOR,
                            'button[data-cy="composeSendMailButton"]')
send.click()


