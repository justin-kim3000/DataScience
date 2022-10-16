# r : read only, r+ : read and write.
# w : write only, w+ : Write and read
# a : append only, a+ : append and read


f = open("st_data.txt", 'a+')
for i in range(10):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

f = open("st_data.txt", 'r')
strings = f.readlines()
print(strings)
f.close()

f = open("st_data.txt", 'w')
memo = f.write("")
print(memo)
f.close()

f = open("st_data.txt", 'r')
strings = f.readlines()
print(strings)
f.close()
