# 05-6 라이브러리

# sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
import sys

print(sys.argv)
print(sys.path)
# sys.exit()

# pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다. 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여 준다.
# import pickle
#
# f = open("test.txt", "wb")
# data = {1: 'Python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()
#
# f = open("test.txt", "rb")
# data = pickle.load(f)
# print(data)

# os : OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.
# import os
#
# print(os.environ)
# print("===============")
# print(os.environ['PATH'])
# print("===============")
# print(os.getcwd())
# print(os.system("dir"))
#
# f = os.popen("dir")
# print(f.read())

# shutil : shutil은 파일을 복사해 주는 파이썬 모듈이다.
# import shutil
#
# shutil.copy("test.txt", "test2.txt")
# print("===============")
# import glob
#
# a = glob.glob("05*")
# print(a)


# tempfile : 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
# import tempfile
#
# filename = tempfile.mkstemp()
# print(filename)

# time : 시간과 관련된 time 모듈에는 함수가 굉장히 많다. 그중 가장 유용한 몇 가지만 알아보자.
import time

print(time.time())
a1 = time.time()
a = time.localtime(a1)
print(a)
b = time.asctime(a)
print(b)
c = time.ctime()
print(c)
d = time.strftime('%x', time.localtime(time.time()))
print(d)
e = time.strftime('%c', time.localtime(time.time()))
print(e)
print("=================")
import calendar

print(calendar.calendar(2021))
calendar.prcal(2015)

calendar.prmonth(2015, 12)

a = calendar.monthrange(2021,4)
print(a)
print("=================")
# random : random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randint에 대해 알아보자.
import random

a = random.random()
print(a)