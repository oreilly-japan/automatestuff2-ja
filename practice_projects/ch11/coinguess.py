# 演習プロジェクト 11.8.1

# プログラムを実行してみると、「裏」「表」を入力してもはずれになってしまいます。
# コインには裏か表かの2通りしかないので、両方ともはずれるのはおかしいです。
# 調べてみると、元のコードには、次の2つのバグがあります。
# 1. toss には0か1の値が入りますが、guessにはユーザが入力した文字列
# （'裏'か'表'）が入っているので、一致することはない。
# 2. 2回目のユーザ入力の値をチェックしていない。
# そこで、ユーザ入力を処理するget_input()という関数を作ります。
# 裏か表が入力されたら、0か1をそれぞれ返します。
# それ以外の文字列が入力されると、質問を繰り返します。

import random

def get_input():
    while True:
        print('コインの表裏を当ててください。表か裏を入力してください：')
        guess = input()
        ind = ('裏', '表').index(guess)
        if ind >= 0:
            return ind

toss = random.randint(0, 1) # 0は裏、1は表

guess = get_input()
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = get_input()
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')
