# 演習プロジェクト 10.8.1

import os
import shutil

def walk_copy(folder, ext, dst):
    ''' folder以下にある拡張子がextのファイルを、dstにコピーする
        dstがなければ作成する'''
    os.makedirs(dst, exist_ok=True)
    lower_ext = ext.lower()
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(lower_ext):
                print('Copying', os.path.join(foldername, filename), '->', dst)
                shutil.copy(os.path.join(foldername, filename), dst)

# テスト用
if __name__ == "__main__":
    walk_copy('delicious', '.jpg', 'jpgs')
    walk_copy('delicious', '.txt', 'txts')

