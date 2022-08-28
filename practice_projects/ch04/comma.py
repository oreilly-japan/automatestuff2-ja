# 演習プロジェクト 4.11.1 カンマ付け

def add_comma(lst):
    if len(lst) <= 0:
        return ''
    if len(lst) == 1:
        return lst[0]
    return ', '.join(lst[:-1]) + ', and ' + lst[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
s = add_comma(spam)
print(s)

