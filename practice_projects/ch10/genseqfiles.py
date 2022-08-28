# 演習プロジェクト 10.8.3 用のファイルを作成する。
#    seqfiles/spam001.txt ～ spam019.txt
# ただし、003, 004, 009 はスキップする。

import os

folder = 'seqfiles'
os.makedirs(folder, exist_ok=True)

for i in range(1, 20):
    if i == 3 or i == 4 or i == 9:
        continue
    filename = 'spam{:03}.txt'.format(i)
    f = open(os.path.join(folder, filename), 'w')
    f.write(str(i))
    f.close()


