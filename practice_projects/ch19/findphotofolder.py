# 演習プロジェクト 19.7.2 写真フォルダを探す

from PIL import Image
import os

for foldername, subfolders, filenames in os.walk('C:\\'):
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in filenames:
        # ファイル拡張子が.pngでも.jpgでもなければ、次のファイルにスキップする
        if not (filename.lower().endswith('.png') or
                filename.lower().endswith('.jpg')):
            num_non_photo_files += 1
            continue

        try:
            # Pillowを使って画像を開く
            im = Image.open(os.path.join(foldername, filename))
            # 幅と高さが500以上なら
            width, height = im.size
            if width >= 500 and height >= 500:
                # 画像が大きいので写真とみなす
                num_photo_files += 1
            else:
                # 画像は小さいので写真ではないとみなす
                num_non_photo_files += 1
        except Exception:
            num_non_photo_files += 1

    # 半分以上が写真なら、
    # フォルダの絶対パスを表示する
    if num_photo_files > 0 and num_photo_files >= num_non_photo_files:
        print(foldername)
