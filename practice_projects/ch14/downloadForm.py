# 演習プロジェクト 14.7.1

import ezsheets

ID = '' # ドキュメントのIDを設定してください

ss = ezsheets.Spreadsheet(ID)
sheet = ss[0]
for row in range(sheet.rowCount):
    data = sheet.getRow(row + 1)
    print(data)
