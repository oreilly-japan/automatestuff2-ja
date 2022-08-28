# 演習プロジェクト 8.6.2

import random, time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    # ランダムに2つの数字を選ぶ
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'#{question_number + 1}: {num1} x {num2} = '

    start_time = time.time()

    for _ in range(3):
        while True:
            try:
                answer = int(input(prompt))
                break
            except:
                print('整数を入力してください')

        elapsed_time = time.time() - start_time
        if elapsed_time >= 8:
            print('時間切れ!')
            break

        if answer == num1 * num2:
            print('正解!')
            correct_answers += 1
            break

    else:
        print('回数制限切れ!')

    time.sleep(1) # ユーザーが結果を読めるように小休止

print(f'得点: {correct_answers} / {number_of_questions}')

