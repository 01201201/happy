# 미니 프로젝트
# 삼각형 출력
""" for i in range(1, 6):
    for j in range(6-i):
        print('*',end=(''))
    print('') """
    
""" for i in range(1, 6):
    print("*" * i) """

""" for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(2*(i+1)-1):
        print("*",end="")
    print() """
    
""" for i in range(1,10):
    if i <= 5:
        for j in range(5-i):
            print(" ",end="")
        for j in range(2*i-1):
            print("*",end="")
        print()
    else:
        for j in range(i-5):
            print(" ",end="")
        for j in range((10-i)*2-1):
            print("*",end="")
        print() """
# 5X5 출력

""" list = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
for i in list:
    print(i) """
    
""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = []"""

""" line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j-1)*5) + i
        line.append(num)
    print(line)
    line = [] """
    
""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num += -1
        line.append(num)
    print(line)
    line = [] """
    
# 가위바위보
    
""" import random

def get_computer_choice():
    choices = ["1", "2", "3"]
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif (
        (user_choice == "1" and pcnum == "3") or
        (user_choice == "2" and pcnum == "1") or
        (user_choice == "3" and pcnum == "2")
    ):
        print("승")
        return
    else:
        print("패")
        return


print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요")
chnum = input()

determine_winner(chnum) """

# 파일 처리
 
""" file = open("temp.txt", "w")

file.write("hello")
file.write("world")

file.close() """
""" file = open("C:\\Users\\Catholic\\python\\happy\\temp.txt", "w")
for i in range(100):
    file.write(f'{i}\n')

file.close()
 """
""" file = open("C:\\Users\\Catholic\\python\\happy\\temp.txt", "a")

file.write("hello\n")
file.write("world")

file.close() """

""" f = open("temp.txt", "r")
res = f.read()
print(res)
f.close() """

""" f = open("C:\\Users\\Catholic\\python\\happy\\temp.txt", "r")
res = f.read()
print(res)
f.close() """

""" file = open("temp.txt", "r")
for i in range(102):
    res = file.readline()
    print(res)

file.close() """

""" f = open("temp.txt", "r")
res = f.readlines()
print(res)

f.close() """

""" f = open("temp.txt", "r")
line = f.readlines()
for l in line:
    print(l)
    
f.close() """

f = open("temp.txt", "r")
for line in f :
    print(line)
    
f.close()