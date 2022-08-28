# 演習プロジェクト 8.6.1

import pyinputplus as pyip

PRICES = {
    '小麦パン': 100,
    '白パン': 110,
    'サワー種': 120,
    'チキン': 200,
    'ターキー': 250,
    'ハム': 300,
    '豆腐': 280,
    'チェダー': 100,
    'スイス': 150,
    'モツァレラ': 180,
    'mayo': 10,
    'mustard': 10,
    'lettuce': 50,
    'tomato': 30,
}

def sandwich_maker():
    bread = pyip.inputMenu(('小麦パン', '白パン', 'サワー種'),
                           prompt='パンを選んでください\n',
                           numbered=True)
    protain = pyip.inputMenu(('チキン', 'ターキー', 'ハム', '豆腐'),
                             prompt='タンパク質を選んでください\n',
                             numbered=True)
    cheese = None
    if pyip.inputYesNo('チーズは必要ですか？') == 'yes':
        cheese = pyip.inputMenu(('チェダー', 'スイス', 'モツァレラ'),
                                prompt='チーズを選んで下さい\n',
                                numbered=True)
    mayo = pyip.inputYesNo('マヨネーズは必要ですか？') == 'yes'
    mustard = pyip.inputYesNo('カラシは必要ですか？') == 'yes'
    lettuce = pyip.inputYesNo('レタスは必要ですか？') == 'yes'
    tomato = pyip.inputYesNo('トマトは必要ですか？') == 'yes'
    numbers = pyip.inputInt('いくつ要りますか？', min=1)

    print('-' * 10)
    price = PRICES[bread]
    print(f'パン: {bread} {PRICES[bread]}円')
    price += PRICES[protain]
    print(f'タンパク質: {protain} {PRICES[protain]}円')
    if cheese:
        price += PRICES[cheese]
        print(f'チーズ: {cheese} {PRICES[cheese]}円')
    if mayo:
        price += PRICES['mayo']
        print(f'マヨネーズ: {PRICES["mayo"]}円')
    if mustard:
        price += PRICES['mustard']
        print(f'カラシ: {PRICES["mustard"]}円')
    if lettuce:
        price += PRICES['lettuce']
        print(f'レタス: {PRICES["lettuce"]}円')
    if tomato:
        price += PRICES['tomato']
        print(f'トマト: {PRICES["tomato"]}円')

    print(f'小計: {price}円')
    print(f'個数: {numbers}個')
    print(f'合計: {price * numbers}円')

sandwich_maker()
