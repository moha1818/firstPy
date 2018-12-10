numberone = 7
guess = 0
print("文字游戏")
while numberone != guess:
    guess = int(input("请输入你猜的数组："))

    if guess == numberone:
        print("bingo")
    elif guess > numberone:
        print("数字大了")
    elif guess < numberone:
        print("数字小了")