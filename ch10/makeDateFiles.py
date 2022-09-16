# renameDates.py 用の年月日ファイルを作成するプログラム
for year in range(1980, 2026, 5):
    for month in range(1, 13):
        for day in range(1, 28, 7):
            us_date = f'{month:02d}-{day:02d}-{year:04d}'
            with open(us_date + '.txt', 'w') as f:
                f.write(us_date)
