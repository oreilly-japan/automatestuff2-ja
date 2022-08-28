# 演習プロジェクト 6.11.1

def print_table(table_data):
    col_n = len(table_data)
    row_n = len(table_data[0])

    col_width = [0] * col_n
    for c in range(col_n):
        for row in table_data[c]:
            col_width[c] = max(col_width[c], len(row))

    for r in range(row_n):
        for c in range(col_n):
            print(table_data[c][r].rjust(col_width[c]), end=' ')
        print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)

