from collections import deque
import random
randPick = [9, 14, 34, 35, 41, 42]
countPick = 0

while 1:

    numlist = deque()
    while 1:
        randValue = random.randint(1, 45)
        if len(numlist) < 6:
            if randValue not in numlist:
                numlist.append(randValue)
            else:
                continue
        else:
            break
    print(numlist)
    countPick += 1
    print("지금까지 시도한 횟수 %d" % countPick)

    countNum = 0
    resNum = []
    for i in numlist:
        if i in randPick:
            countNum += 1
            resNum.append(i)
    if countNum == 6:
        print(resNum)
        break
