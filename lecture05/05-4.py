try:
    f = open("새파일.txt", "r")
    f.close()
except:
    print("error")
print("=============")

try:
    a = 4 / 0
except ZeroDivisionError as e:
    print(e)
print("=============")

try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e, "!!!\n")
print("=============")

# try:
#     age=int(input('나이를 입력하세요: '))
# except:
#     print('입력이 정확하지 않습니다.')
# else:
#     if age <= 18:
#         print('미성년자는 출입금지입니다.')
#     else:
#         print('환영합니다.')

print("=============")

class Bird:
    def fly(self):
        raise NotImplementedError
#
# class Eagle(Bird):
#     pass
#
# eagle = Eagle()
# eagle.fly()

class Eagle2(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle2()
eagle.fly()
print("=======")

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
    
print(say_nick('천사'))
print(say_nick('바보'))

try:
    say_nick('천사2')
    say_nick('바보')
except MyError:
    print("허용되지 않는 별명입니다.")