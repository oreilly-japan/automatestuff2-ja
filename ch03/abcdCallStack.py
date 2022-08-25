def a():
    print('a() starts')
    b()  # ❶ 
    d()  # ❷ 
    print('a() returns')

def b():
    print('b() starts')
    c()  # ❸ 
    print('b() returns')

def c():
    print('c() starts')  # ❹ 
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()  # ❺ 
