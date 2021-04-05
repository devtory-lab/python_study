a = list(filter(lambda x: x > 0, [1,-2,3,-5,8,-3]))
print(a)

print("==============")
print(hex(234))
print(int('0xea', 16))

print("============Q6=============")
a = [1,2,3,4]
b = list(map(lambda x: x*3, a))
print(b)

print("============Q7============")
a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a), min(a), " = ", max(a) + min(b))

print("============Q8============")
a = round(17 / 3, 4)
print(a)

print("============Q9============")
import sys
numbers = sys.argv[1:]
result = 0
for i in numbers:
    result += int(i)
print(result)
