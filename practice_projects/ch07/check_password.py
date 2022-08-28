# 演習プロジェクト 7.18.2

import re

# 強いパスワードならTrue、そうでなければFalseを返す
def check_password(password):
    if len(password) < 8:  #8文字以上
        return False
    if not re.search(r'[a-z]', password): #小文字を含む
        return False
    if not re.search(r'[A-Z]', password): #大文字を含む
        return False
    if not re.search(r'[0-9]', password): #数字を含む
        return False
    return True

# テスト用
if __name__ == "__main__":
    passwords = ['abcdehA1', 'abcdeA1', '', '        ',
                 'abcdefgh', 'abcdefgA', 'abcdefg1',
                 'ABCDEFGH', 'ABCDEFGa', 'ABCDEFG1',
                 '12345678', '1234567a', '1234567A']
    for p in passwords:
        print(p + ':' + str(check_password(p)))

