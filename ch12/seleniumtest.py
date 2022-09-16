from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
    print(f'そのクラス名を持つ要素 <{elem.tag_name}>を見つけた！')
except:
    print('そのクラス名を持つ要素は見つからなかった。')
