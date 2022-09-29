import random

numlist = []
res = []

# while 1:
#     if len(numlist) == 6:
#         break

#     value = int(input())

#     if 1 <= value <= 45:
#         if value not in numlist:
#             numlist.append(value)
#         numlist = list(set(numlist))
#         numlist.sort()
#         print("입력한 숫자는 %s입니다." % numlist)
#     else:
#         print("1부터 45까지의 숫자만 넣어주세요.")
# print(numlist)
numlist = [1, 3, 6, 28, 34, 44]

while 1:
    if len(res) == 6:
        break

    randValue = random.randint(1, 45)

    if randValue not in res:
        res.append(randValue)
    res = list(set(res))
    res.sort()
print(res)
