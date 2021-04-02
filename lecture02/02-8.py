#02-8 자료형의 값을 저장하는 공간, 변수
a = [1, 2, 3]
print(id(a))

b = a
print(id(b))
print("============")

print(a is b)

a[1] = 4
print(b[1])

from copy import copy
b = copy(a)
print(b, a is b)


