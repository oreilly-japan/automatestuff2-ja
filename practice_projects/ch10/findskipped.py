# 演習プロジェクト 10.8.3 連番の飛びを埋める
# 先に python genseqfile.py で、テスト用のファイルを生成しておく。

import os
import re
import shutil

def find_skiped_files(folder, prefix, rename=False):
    ''' folderの中のprefixから始まるファイルの連番の飛びを調べる。
        renameがTrueなら、飛びを埋めるようにファイル名を変更する。
    '''
    files = {}         # { 連番: 元ファイル名 } 
    max_digit_len = 0  # 連番の最大の長さ
    rest = ''          # 残りのファイル名 (例 spam001.txtなら、'.txt')

    # 「prefix 連番 残り」を検索
    pattern = re.compile('^' + prefix + r'(\d+)(.*)')
    for filename in os.listdir(folder):
        mo = pattern.search(filename)
        if not mo:
            continue
        files[int(mo.group(1))] = filename
        max_digit_len = max(max_digit_len, len(mo.group(1)))
        rest = mo.group(2)

    # マッチするファイルがなければ終了
    if len(files) == 0:
        return

    # 連番を小さい順に並べる
    org_index = sorted(files.keys())
    start = org_index[0]
    end = org_index[-1]
    # 連番の飛びを調べる
    for n in range(start, end + 1):
        if not n in files:
            print('Missing', prefix + str(n).rjust(max_digit_len, '0') + rest)

    # 飛びを埋めるようにファイル名を変更する
    if rename:
        for n,ind in enumerate(org_index):
            # 新しいファイル名を作る
            new_filename = prefix + str(start + n).rjust(max_digit_len, '0') + rest
            # 元のファイルと同じなら何もしない
            if new_filename == files[ind]:
                continue
            # ファイル名を変更する
            print('Rename', os.path.join(folder, files[ind]), 
                  '->', os.path.join(folder, new_filename))
            shutil.move(os.path.join(folder, files[ind]), 
                        os.path.join(folder, new_filename))

# テスト用
if __name__ == "__main__":
    find_skiped_files('seqfiles', 'spam')
    find_skiped_files('seqfiles', 'spam', True)

