food = "Python's favorite food is perl"
print(food)

say = "\"Python is very easy.\" he says."
print(say)

multiline = "Life is too short\nYou need python"
print(multiline)

multiline='''
    Life is too short2 \' \" \\
    You need python1\000\000ttt
    '''

print(multiline)

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
print(len(a))

a = "Life is too short, You need Python"
print(a[0], a[12], a[-1])
print(a[0] + a[1] + a[2] + a[3])        #Life
print(a[0:4])                           #Life
print(a[19:])       #You need Python

a = "20010331Rainy"
year = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]
print(year + '-' + month + '-' + day + ' : ' + weather)

b = "Pithun"
print(b + "====>")
b = b[:1] + "y" + b[2:]
b = b[:4] + "o" + b[5:]
print(b)

number = 3
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)

a = "I eat {0} apples".format(3)
print(a)

a = "I eat {0} apples".format("five")
print(a)

a = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(a)

name = "홍길동"
age = 30
a = f"나의 이름은 {name}입니다. 나이는 {age}입니다."
print(a)

d = {"name":"홍길동", "age":30}
a = f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다."
print(a)

a = "hobby"
print(a.count('b'))     #b의 갯수를 돌려준다.

#위치 알려주기1
a = "Python is the best choice"
print(str(a.find('b')) + ", " + str(a.find('k')))

#문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#문자열 나누기(split)
b = "a:b:c:d"
print(b.split(":"))


