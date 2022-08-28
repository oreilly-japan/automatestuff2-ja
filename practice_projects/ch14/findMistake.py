# 演習プロジェクト 14.7.3

import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet = ss[0]
for row in range(1, sheet.rowCount):
    data = sheet.getRow(row + 1)
    try:
        beans_per_jar = int(data[0])
        jars = int(data[1])
        total_beans = int(data[2])
        if beans_per_jar * jars != total_beans:
            print(f'{row + 1}行：{beans_per_jar} * {jars} != {total_beans}')
    except:
        break

