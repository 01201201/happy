'''
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)
print(x is z)
print(x is not y)
'''
'''
a = 5
b = 5
print(a is b)
print(a is not b)
'''
'''
a = 3
b = 3.0

print(a is b)
print(a is not b)

a = [3, 5, 1]
b = a
print(a is b)
print(a is not b)
'''
'''
a = [3, 5, 1]
b = a
a[0] = 2
print(a is b)
print(a is not b)
print(a, b)
print(a is b)
'''
# x = 2 + 3 * 4
# x = 2 ** 3 ** 2
# x= 10 / 5 / 2
# x = 2 ** (3 ** 2)
# x = 10 % 3 % 2
# x = 1 + 2 > 3 and 4 - 1 < 2
# x = not False and True
# x = not True or False and True
# x = 1 & 2 | 3 ^ 4
# x = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# x = 2 * -3 // 2
# x = 1== 2 != 3
# print(x)

#조건문
'''
x = 10
x = -10
x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
'''
# 짝수, 홀수 구분 조건문 구성
'''
num = 2
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
'''
# 두 수를 비교해서 같은지 비교하는 조건문 구성
'''
a = 2
b = 3
if a == b:
    print("같습니다.")
else:
    print("다릅니다.")
'''
# 문자가 a or b 인지 비교하는 조건문 구성
'''
char = "a"
if char == "a" or char == "b":
    print("'a' 또는 'b' 입니다")
else:
    print("'a'또는 'b'가 아닙니다")
'''
        
# 반복문
# for문
'''
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
     print(fruit)
'''
# 이중 for문 출력
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
for row in my_list:
    for num in row:
        print(num)
'''
# 0 ~ 9까지 출력
'''        
for i in range(10):
     print(i)
'''
# 문자열을 한글자씩 출력
'''
for char in "Python":
    print(char)
'''
# 리스트 요소 반대로 출력 (reserve 이용)
'''
for fruit in reversed(fruits):
    print(fruit)
'''
# 리스트 요소 반대로 출력 (sorted 이용)
'''    
for fruit in sorted(fruits, reverse=True):
    print(fruit)
'''

# 구구단 출력
'''
for i in range(2, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', i * j)
'''
# for ~ else 문
'''
rang = [5, 8, 3, 1, 6]
for i in rang:
    print("element : ", i) 
else :
    print("end process")   
'''    
# 반복문 제어
'''
for i in range(10):
    if i == 7:
        print("break ", i)
        break
    elif i == 1:
        print("continue ", i)
        continue
    else:
        print("pass ", i)
        pass
print(i) 
'''
# while 문
'''
i = 1
while i <= 5:
    print(i)
    i += 1
'''
# 0부터 9까지 출력
'''
i = 0
while i <= 9:
    print(i)
    i += 1
'''
# 문자열을 한 글자씩 출력
'''
str_word = "python"
i = 0

while i < len(str_word):
    print(str_word[i])
    i += 1
'''
# 1부터 10까지의 총합 출력
'''
sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1
print(sum)
'''

# 1에서 100까지의 짝수, 홀수 출력하기

i = 1

while i <= 100:
    if i % 2 == 0:
        print("짝수 : ", i)
    elif i % 2 == 1:
        print("홀수 : ", i)

    i += 1

# 결과값이 무한대로 나왔던 학생입니다. while 1 <= 100: 에서 1을 i로 바꿨더니
# 100까지만 나오기는 하나, 홀수만 출력됩니다.

# 1에서 100까지의 7의 배수만 출력하기
'''
i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1 
'''