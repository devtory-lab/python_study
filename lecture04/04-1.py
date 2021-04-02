def add(a, b):
    return a + b

print(add(1,2))
print("=============")
def say():
    return "hi"

a = say()
print(a)
print("=============")

def add2(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

add2(1,2)
a1 = add2(1, 3)
print(a1)           #==> none
print("=============")

# arguments
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

a1 = add_many(1,2,3,4,5, 6, 7, 8, 9, 10)
print(a1)
a2 = add_many(2,3,4,5,6)
print(a2)
print("=============")

#arguments
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


a1 = add_mul("add", 1,2,3,4,5,6,7,8,9,10)
print(a1)
a2 = add_mul("mul", 1,2,3,4,5,6,7,8,9,10)
print(a2)
print("=============")

#키워드 파라미터 kwargs ( keyword arguments)==> 딕셔너리, key:value 형태로 변환
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=-1)
print_kwargs(name='foo', age=3)
print("=============")

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, False)

print("================")

# SyntaxError: non-default argument follows default argument
# def say_myself2(name, man=True, old):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
#
# say_myself2("박응용", 27)

#lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)
print("================")



print("================")



print("================")



print("================")



print("================")

