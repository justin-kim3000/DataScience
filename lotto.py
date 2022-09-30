import random
numlist = []

print("1부터 45까지 숫자를 입력하세요.")
print("랜덤한 숫자 1개를 입력하려면 숫자 77을 입력하세요.")
print("랜덤한 숫자로 선택을 끝내고 싶으면 숫자 20000을 입력하세요.")

# 원하는 숫자 선택
while 1:
    if len(numlist) >= 6:
        break

    value = int(input())

    if 1 <= value <= 45:
        if value not in numlist:
            numlist.append(value)
        numlist.sort()
        print("지금까지 입력한 숫자는 %s입니다." % numlist)

    elif value == 77:
        while 1:
            randValue = random.randint(1, 45)
            if value not in numlist:
                numlist.append(randValue)
                break
            else:
                continue
        numlist.sort()
        print("랜덤 숫자는 %d입니다." % randValue)
        print("지금까지 입력한 숫자는 %s입니다." % numlist)

    elif value == 20000:
        while 1:
            randValue = random.randint(1, 45)
            if len(numlist) < 6:
                if value not in numlist:
                    numlist.append(randValue)
                else:
                    continue
            else:
                break
        numlist.sort()
        print("지금까지 입력한 숫자는 %s입니다." % numlist)
    else:
        print("1부터 45까지의 숫자만 넣어주세요.")

# res = []
# 랜덤 숫자 추출
# while 1:
#     if len(res) == 6:
#         break

#     randValue = random.randint(1, 45)

#     if randValue not in res:
#         res.append(randValue)
#     res = list(set(res))
#     res.sort()
# print(res)
