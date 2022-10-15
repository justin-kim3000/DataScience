def lect_write(stduent):
    f = open("st_data.txt", 'w')
    for i in range(len(stduent)):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()
