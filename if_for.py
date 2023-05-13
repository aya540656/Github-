# ランダムモジュールを呼び出す
from random import randint

# 1～10の乱数で5以上か未満かを判断する動作を5回繰り返す
def num_judge():
    for i in range(5):
        num = randint(1, 10)
        print(num)
        if num >= 5:
            print("5以上です")
        else:
            print("5未満です")
        print("----------")

num_judge()