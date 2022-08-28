# 演習プロジェクト 3.12.1 コラッツ数列を表示

def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1

print('整数を入力してください：')
i = int(input())

while i > 1:
    i = collatz(i)
    print(i)

