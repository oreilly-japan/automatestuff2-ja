# 演習プロジェクト 4.11.2 コイン投げ連続解析

import random

number_of_streaks = 0

for experiment_number in range(10000):
    # 100個の裏表のリストを作るコード
    results = []
    N = 100
    for i in range(N):
        results.append(random.randint(0, 1))

    # 6連続の裏または表を見つけるコード
    S = 6
    for i in range(N - S):
        s = sum(results[i:i+S])
        if s == 0 or s == S:
            number_of_streaks += 1
            break

print(f'同じ面が6連続出現する確率: {number_of_streaks / 100}%')
