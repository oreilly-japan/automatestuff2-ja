#! python3

# docx2pdf.py file1.docx file2.docx ...
#    docxファイルからプライバシー情報を削除して保存
#    pdfファイルに変換して保存
#    docxファイル名はフルパスで与えること
import sys
import os
import win32com.client

if len(sys.argv) < 2:
    input('使い方：docx2pdf.exeにdocxファイルをドラッグ＆ドロップ'
          'してください。複数のファイルも対応可能です。\n'
          'Enterキーを押してください。')
    sys.exit()

wdFormatPDF = 17
wdRDIAll = 99

word_obj = win32com.client.Dispatch('Word.Application')

for word_filename in sys.argv[1:]:
    if not word_filename.endswith('.docx'):
        continue
    print(f'開いています：{word_filename}')
    doc_obj = word_obj.Documents.Open(word_filename)
    doc_obj.RemoveDocumentInformation(wdRDIAll)
    print(f'文書情報を削除しています：{word_filename}')
    doc_obj.Save()
    pdf_filename = word_filename[:-5] + '.pdf'
    print(f'PDFに変換しています：{pdf_filename}')
    doc_obj.SaveAs(pdf_filename, FileFormat=wdFormatPDF)
    doc_obj.Close()

word_obj.Quit()

input('終了しました。Enterキーを押してください。')
