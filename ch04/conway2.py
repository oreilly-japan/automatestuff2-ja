# Conwayのライフゲーム
import random, time, copy
WIDTH = 60
HEIGHT = 20

# セルを格納するリストのリストを作成
next_cells = []
for y in range(HEIGHT):
    raw = [] # 新しい列を作成
    for x in range(WIDTH):
        if random.randint(0, 1) == 0:
            raw.append('#') # 生きたセルを追加
        else:
            raw.append(' ') # 死んだセルを追加
    next_cells.append(raw) # next_cells は列のリストのリスト

while True: # メインプログラムループ
    print('\n\n\n\n\n') # ステップ間を改行で分ける
    current_cells = copy.deepcopy(next_cells)

    # current_cellsを表示
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[y][x], end='') # # かスペースを表示
        print() # 行末で改行

    # 現在のセルに基づき次のステップのセルを計算
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # 隣接座標を取得
            # `% WIDTH`により left_coord を0とWIDTH - 1の間の値にする
            left_coord  = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # 生きた隣接セルの数をカウント
            num_neighbors = 0
            if current_cells[above_coord][left_coord] == '#':
                num_neighbors += 1 # 左上が生きたセル
            if current_cells[above_coord][x] == '#':
                num_neighbors += 1 # 上が生きたセル
            if current_cells[above_coord][right_coord] == '#':
                num_neighbors += 1 # 右上が生きたセル
            if current_cells[y][left_coord] == '#':
                num_neighbors += 1 # 左が生きたセル
            if current_cells[y][right_coord] == '#':
                num_neighbors += 1 # 右が生きたセル
            if current_cells[below_coord][left_coord] == '#':
                num_neighbors += 1 # 左下が生きたセル
            if current_cells[below_coord][x] == '#':
                num_neighbors += 1 # 下が生きたセル
            if current_cells[below_coord][right_coord] == '#':
                num_neighbors += 1 # 右下が生きたセル

            # Conwayのライフゲームのルールに基づきセルを設定
            if current_cells[y][x] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                # 生きたセルに隣接する生きたセルが2個か3個
                next_cells[y][x] = '#'
            elif current_cells[y][x] == ' ' and num_neighbors == 3:
                # 死んだセルに隣接する生きたセルが3個
                next_cells[y][x] = '#'
            else:
                # その他の場合は死んだセルになる
                next_cells[y][x] = ' '
    time.sleep(1) # ちらつきを防ぐため1秒待つ
