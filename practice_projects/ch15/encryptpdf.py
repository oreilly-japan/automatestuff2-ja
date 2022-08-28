# 演習プロジェクト 15.7.1  PDFファイルを暗号化
# カレントディレクトリ以下のすべてのPDFファイルを暗号化する

import os
import sys
import PyPDF2

def encrypt_pdf_file(src, enc, password):
    """ PDFファイルを暗号化する
        src=元のPDFファイル名、enc=暗号化PDFファイル名、passwrd=パスワード
        成功すればTrue、エラーならFalseを返す
    """
    print('暗号化中：', src, '->', enc)

    # PDFファイルを開く
    src_file = open(src, 'rb')
    src_reader = PyPDF2.PdfFileReader(src_file)

    # 暗号化済みならエラー
    if src_reader.isEncrypted:
        print('エラー：すでに暗号化されています。', src)
        src_file.close()
        return False

    # 新規のPDF文書
    enc_writer = PyPDF2.PdfFileWriter()
    # ページを追加する
    for page_num in range(src_reader.numPages):
        enc_writer.addPage(src_reader.getPage(page_num))
 
    # PDFファイルを保存
    enc_file = open(enc, 'wb')
    enc_writer.encrypt(password)
    enc_writer.write(enc_file)
    enc_file.close()
    src_file.close()
    return True


def verify_pdf_file(src, enc, password):
    """ 暗号化PDFファイルを照合する。
        src=元のPDFファイル名、enc=暗号化PDFファイル名、passwrd=パスワード
        成功すればTrue、エラーならFalseを返す
    """
    print('検証中：', enc)

    # 暗号化PDFファイルを開く
    enc_file = open(enc, 'rb')
    enc_reader = PyPDF2.PdfFileReader(enc_file)

    # 暗号化されていなければエラー
    if not enc_reader.isEncrypted:
        print('エラー：暗号化されていません。', enc)
        enc_file.close()
        return False

    # パスワードを用いて暗号解除
    if not enc_reader.decrypt(password):
        print('エラー: 暗号を解除できません。', password)
        enc_file.close()
        return False

    # 元ファイルを開く
    src_file = open(src, 'rb')
    src_reader = PyPDF2.PdfFileReader(src_file)

    # ページ数が一致しなければエラー
    if src_reader.numPages != enc_reader.numPages:
        print('エラー：ページ数が異なります。', src, enc)
        enc_file.close()
        src_file.close()
        return False

    # 内容が一致しなければエラー
    for page_num in range(src_reader.numPages):
        src_text = src_reader.getPage(page_num).extractText()
        enc_text = enc_reader.getPage(page_num).extractText()
        if src_text != enc_text:
            print('エラー：ページ内容が異なります。', src, enc)
            enc_file.close()
            src_file.close()
            return False

    enc_file.close()
    src_file.close()
    return True

def walk_encrypt_pdf_files(folder, password):
    """ 指定したフォルダ以下のすべてのPDFファイルを暗号化する。
        folder=開始フォルダ、password=パスワード
    """

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # PDFファイルでなければスキップ
            if not filename.lower().endswith('.pdf'):
                continue

            # ファイル名を src.pdf -> src_encrypted.pdf とする
            new_filename = filename[:-4] + '_encrypted.pdf'

            filename = os.path.join(foldername, filename)
            new_filename = os.path.join(foldername, new_filename)

            # 暗号化し、照合に成功したら、元ファイルを消す
            if encrypt_pdf_file(filename, new_filename, password) \
               and verify_pdf_file(filename, new_filename, password):
                print('削除中：', filename)
                os.unlink(filename)


if len(sys.argv) < 2:
    sys.exit('Usage: python encryptpdf.py password')

password = sys.argv[1]
walk_encrypt_pdf_files('./', password)
