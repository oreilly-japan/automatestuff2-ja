# 演習プロジェクト 10.8.3 連番ファイルの間に隙間を空ける
# 先に python genseqfile.py で、テスト用のファイルを生成しておく。

import os
import re
import shutil

def insert_gap(folder, prefix, before, gap):
    ''' folderの中のprefixから始まる連番ファイルで、
        beforeの前にgapの数の隙間を開け、以降の連番をずらす。
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

    # beforeに指定した連番が存在しなければ例外
    if not before in org_index:
        raise Exception('No sequence number that is spacified by before=' + str(before))

    # 隙間を空ける場所
    before_ind = org_index.index(before)

    # 連番の大きい順にファイル名を変更する
    for n in range(len(org_index) - 1, before_ind - 1, -1):
        # 連番をgap増やした新しいファイル名を作る
        new_filename = prefix + str(org_index[n] + gap).rjust(max_digit_len, '0') + rest
        # 元のファイルと同じなら何もしない
        if new_filename == files[org_index[n]]:
            continue
        # ファイル名を変更する
        print('Rename', os.path.join(folder, files[org_index[n]]), 
              '->', os.path.join(folder, new_filename))
        shutil.move(os.path.join(folder, files[org_index[n]]), 
                    os.path.join(folder, new_filename))

# テスト用
if __name__ == "__main__":
    insert_gap('seqfiles', 'spam', 11, 3)

