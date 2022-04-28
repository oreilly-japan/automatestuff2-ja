import time, sys
indent = 0 # インデントの幅
indent_increasing = True # インデントが増えているかどうか

try:
    while True: # メインのプログラムのループ
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # 0.1秒間止める

        if indent_increasing:
            # インデントを増やす
            indent = indent + 1
            if indent == 20:
                # 方向を変える
                indent_increasing = False
        else:
            # インデントを減らす
            indent = indent - 1
            if indent == 0:
                # 方向を変える
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()
