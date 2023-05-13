from random import randint

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