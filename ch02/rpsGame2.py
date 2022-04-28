import random, sys

print('ROCK, PAPER, SCISSORS')

# 次の変数に、勝ち、負け、引き分けの数を記録する
wins = 0
losses = 0
ties = 0

MOVE_NAMES = ('ROCK', 'PAPER', 'SCISSORS')
MOVE_CHARS = 'rpsq'

while True: # メインのゲームループ
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # プレーヤーの入力ループ
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = MOVE_CHARS.find(input())
        if player_move >= 3:
            sys.exit() # プログラムを終了する
        if player_move >= 0:
            break # 入力ループを抜ける
        print('Type one of r, p, s, or q.')

    # プレーヤーの入力した手を表示する
    print(MOVE_NAMES[player_move] + ' versus...')

    # コンピューターの手を表示する
    computer_move = random.randint(0, 2)
    print(MOVE_NAMES[computer_move])

    # 勝ち／負け／引き分けを表示し記録する
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move + 1) % 3 == computer_move:
        print('You lose!')
        losses += 1
    else:
        print('You win!')
        wins += 1
