import random

def rand_name(num):    
    first_name = ['김', '박', '최', '이','성','우','윤','문']
    sec_name = ['길', '성', '동', '영', '정','명','재']
    last_name = ['은', '원', '훈', '혜', '서', '종', '범','우','성','준','인']
    name = []
    for _ in range(num):
        one_name = first_name[random.randrange(0, len(first_name))] + sec_name[random.randrange(
            0, len(sec_name))] + last_name[random.randrange(0, len(last_name))]
        name.append(one_name)
    # print(name)

    for i in name:
        print(i)


def rand_id(num):    
    first_name = ['kim', 'park', 'cho', 'lee']
    sec_name = ['oo', 'ii', 'tt', 'aa', 'ss']
    last_name = ['@naver.com', '@gmail.com', '@hanmail.net', '@yahoo.com']
    name = []
    for i in range(num):
        one_name = first_name[random.randrange(0, len(first_name))] + sec_name[random.randrange(
            0, len(sec_name))] + last_name[random.randrange(0, len(last_name))]
        name.append(one_name)
    # print(name)

    for i in name:
        print(i)
        
def rand_id1(num):    
    first_name = ['kim']
    sec_name = ['oo', 'ii', 'tt', 'aa', 'ss']
    last_name = ['@naver.com', '@gmail.com', '@hanmail.net', '@yahoo.com']
    name = []
    for i in range(1,num+1):
        one_name = first_name[random.randrange(0, len(first_name))] + str(i) + last_name[random.randrange(0, len(last_name))]
        name.append(one_name)
    # print(name)

    for i in name:
        print(i)

def rand_pw(num):    
    first_name = ['kim@', 'p!@a#rk', 'c$!ho', '@l$ee']
    sec_name = ['\@#o', 'i@!i', 't2!t', 'a12#a', '1ss2']
    last_name = ['@21!$', '!!#$', 'asdft', 'wdwm']
    name = []
    for _ in range(num):
        one_name = first_name[random.randrange(0, len(first_name))] + sec_name[random.randrange(
            0, len(sec_name))] + last_name[random.randrange(0, len(last_name))]
        name.append(one_name)
    # print(name)

    for i in name:
        print(i)


def rand_phone(num):    
    first_name = ['kim@', 'p!@a#rk', 'c$!ho', '@l$ee']
    sec_name = ['\@#o', 'i@!i', 't2!t', 'a12#a', '1ss2']
    last_name = ['@21!$', '!!#$', 'asdft', 'wdwm']
    name = []
    for i in range(num):
        one_name = first_name[random.randrange(0, len(first_name))] + sec_name[random.randrange(
            0, len(sec_name))] + last_name[random.randrange(0, len(last_name))]
        name.append(one_name)
    # print(name)

    for i in name:
        print(i)
# rand_name(10)
rand_id1(110)
# rand_pw(10)
# rand_id1(50)