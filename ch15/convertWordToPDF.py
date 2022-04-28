# このスクリプトはWindows専用で、Wordのインストールが必須
import os
import win32com.client
import docx

# ファイル名は絶対パスで指定
word_filename = os.path.join(os.getcwd(), 'your_word_document.docx')
pdf_filename = os.path.join(os.getcwd(), 'your_pdf_filename.pdf')

# docxでWord文書を作成
doc = docx.Document()
doc.add_paragraph('Hello world!')
doc.save(word_filename)

# win32でWordを起動
PDF = 17 # PDF形式の数値コード
word_obj = win32com.client.Dispatch('Word.Application')
# Word文書を開いて、PDF形式で保存
doc_obj = word_obj.Documents.Open(word_filename)
doc_obj.SaveAs(pdf_filename, FileFormat=PDF)
doc_obj.Close()
word_obj.Quit()
