# 演習プロジェクト 15.7.1  PDFファイルを復号
# カレントディレクトリ以下のすべてのPDFファイルを復号する

import os
import sys
import PyPDF2

def decrypt_pdf_file(enc, dst, password):
    enc_file = open(enc, 'rb')
    enc_reader = PyPDF2.PdfFileReader(enc_file)
    if enc_reader.isEncrypted:
        if not enc_reader.decrypt(password):
            print('エラー：パスワードが間違っています。スキップします。', enc)
            return False
    else:
        enc_file.close()
        return True

    print('暗号解除中：', enc, '->', dst)
    dst_writer = PyPDF2.PdfFileWriter()
    for page_num in range(enc_reader.numPages):
        dst_writer.addPage(enc_reader.getPage(page_num))
 
    dst_file = open(dst, 'wb')
    dst_writer.write(dst_file)
    dst_file.close()
    enc_file.close()
    return True


def walk_decrypt_pdf_files(folder, password):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.lower().endswith('.pdf'):
                continue
            new_filename = filename.replace('encrypted', 'decrypted')
            if new_filename == filename:
                new_filename = new_filename[:-4] + '_decrypted.pdf'

            filename = os.path.join(foldername, filename)
            new_filename = os.path.join(foldername, new_filename)

            decrypt_pdf_file(filename, new_filename, password)


if len(sys.argv) < 2:
    sys.exit('Usage: python decryptpdf.py password')

password = sys.argv[1]
walk_decrypt_pdf_files('./', password)

