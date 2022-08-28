# 演習プロジェクト 14.7.2

import sys
import ezsheets

if len(sys.argv) < 2:
    sys.exit('Usage python convert.py src')

ss = ezsheets.upload(sys.argv[1])
ss.title = ss.title + '.conv'
ss.downloadAsExcel()
ss.downloadAsODS()
ss.downloadAsPDF()
