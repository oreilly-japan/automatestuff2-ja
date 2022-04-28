import random, sys

print('ROCK, PAPER, SCISSORS')

# 次の変数に、勝ち、負け、引き分けの数を記録する
wins = 0
losses = 0
ties = 0

while True: # メインのゲームループ
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # プレーヤーの入力ループ
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit() # プログラムを終了する
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # 入力ループを抜ける
        print('Type one of r, p, s, or q.')

    # プレーヤーの入力した手を表示する
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # コンピューターの手を表示する
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # 勝ち／負け／引き分けを表示し記録する
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1

