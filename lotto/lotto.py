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
            if randValue not in numlist:
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
                if randValue not in numlist:
                    numlist.append(randValue)
                else:
                    continue
            else:
                break
        numlist.sort()
        print("지금까지 입력한 숫자는 %s입니다." % numlist)
    else:
        print("1부터 45까지의 숫자만 넣어주세요.")

# numlist에 내가 선택한 숫자가 들어있음.
print("내가 선택한 번호: ", numlist)


randPick = []
# 랜덤 숫자 추출
while 1:
    if len(randPick) == 6:
        break

    randValue = random.randint(1, 45)

    if randValue not in randPick:
        randPick.append(randValue)
    randPick = list(set(randPick))
    randPick.sort()

# 마지막에 보너스 값 추가
BonusPick = []
while 1:
    BonusValue = random.randint(1, 45)
    if BonusValue not in randPick:
        BonusPick.append(BonusValue)
        break

# 당첨번호
print("랜덤으로 뽑은 당첨 번호: ", randPick)
print("보너스 값은 :", BonusPick)


# 맞은 갯수 체크
countNum = 0
resNum = []
for i in numlist:
    if i in randPick:
        countNum += 1
        resNum.append(i)

print("일치하는 갯수 : ", countNum)
print("일치하는 값 : ", resNum)


# 결과 나열
