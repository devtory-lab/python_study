# 04-3 파일 읽고 쓰기
f = open("새파일.txt", 'w')
f.close()
print("======================")

f = open("새파일.txt", "w")
for i in range(1, 11):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()
print("======================")

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
f = open("새파일.txt", "r")
line = f.readline()
print(line)
f.close()
print("======================")

f = open("새파일.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
print("======================")

# readlines 함수 사용하기 ==> 전체를 리스트로
f = open("새파일.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
print("======================")

# read 함수 사용하기 ==> 전체를 문자열로
f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()
print("======================")

# 파일에 새로운 내용 추가하기
f = open("새파일.txt", "a")
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()
print("======================")

# with문과 함께 사용하기
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
print("======================")

import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=" ")