# 英語からピッグ・ラテンに変換
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = [] # ピッグ・ラテンの単語のリスト
for word in message.split():
    # wordの先頭の英字でないものを分離する
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # wordの末尾の英字でないものを分離する
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]

    # wordがすべて大文字か、先頭のみ大文字かを覚えておく
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower() # 変換のために、すべて小文字にする

    # wordの先頭の子音を分離する
    prefix_consonants = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # wordにピッグ・ラテンの語尾をつける
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

    # 必要ならwordをすべて大文字か、先頭のみ大文字に戻す
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # wordの先頭と末尾にあった英字でない文字を元に戻す
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# 単語のリストをひとつの文字列に連結して表示する
print(' '.join(pig_latin))
