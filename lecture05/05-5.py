# 05-5 내장 함수
# abs : 절대값
a = abs(3)
b = abs(-3)
c = abs(-1.2)
print(a, b, c)
# all : all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
a = all([1, 2, 3])
b = all([1, 2, 3, 0])
c = all([])
print(a, b, c)
# any : any(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.
a = any([1,2,3,0])
b = any([1,2,3])
c = any([])
print(a,b,c)
# chr : chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
a = chr(97)
b = chr(48)
print(a, b)
# dir : dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다. 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여 주는 예이다
a = dir([1,2,3])
b = dir({'1':'a'})
print(a, b)
# divmod : divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
a = divmod(7, 3)
print(a)
# enumerate : 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# eval : eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다
a = eval('1+2')
b = eval("'hi' + 'a'")
c = eval('divmod(7, 3)')
print(a, b, c)
# filter : filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

def positive2(x):
    return x > 0

print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))
# hex : hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
a = hex(234)
b = hex(3)
print(a, b)
print("=================")
# id : id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print("=================")
# int : int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
a = int('3')
b = int(3.4)
print(a, b)
c = int('11', 2)        #2진수로 표현된 11의 10진수 값은 다음과 같이 구한다.
print(c)
d = int('1A', 16)       #16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
print(d)
print("=================")
# isinstance : isinstance(object, class )는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
class Person: pass
a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))
print("=================")
# len : len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
print(len("python"))
print(len([1,2,3]))
print(len((1, 'a')))
print("=================")
# list : list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
print(list("python"))
print(list((1,2,3,4)))
a = [1,2,3]
b = a
c = list(a)
print(a, b, c)
print(id(a), id(b), id(c))
print("=================")
# map : map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times2(x):
    return x * 2

result = list(map(two_times2, [1,2,3,4,5]))
print(result)

print(list(map(lambda x: x*2, [1,2,3,4,5,6,7,8])))
print("=================")
# max : max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.
print(max([1,2,3]), max('python'))
print("=================")
# min : min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.
print(min([1,2,3]), min('python'))
print("=================")
# oct : 10 --> 8진수
print(oct(34), oct(12345))
print("=================")
# ord : ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
print(ord('a'), ord('0'))
print("=================")
# pow : pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
print(pow(2,2), pow(3,3))
print("=================")
# range : range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
print(list(range(5)), list(range(1,5)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))
print("=================")
# round : round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
print(round(4.6), round(4.4), round(3.14152, 2))
print("=================")
# sorted : sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print(sorted([2,3,5,4,6,1]), sorted(['a', 'c', 'b', 'e', 'd']))
print(sorted('zero'), sorted((3,2,1)))
print("=================")
# str
print(str(3.12), str('hi'), str('hi'.upper()))
print("=================")
# sum
print(sum([1,2,3]), sum((1,2,3,4)))
print("=================")
# tuple : tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
a = tuple('abcd')
b = tuple([1,2,3])
c = tuple((1,2,3,3,3,3))
print(a, b, c)
print("=================")
# type : type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.
print(type(a), type(b), type(sum([1,2,3])))
# zip
a = list(zip([1, 2, 3], [4, 5, 6]))
b = list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
c = list(zip("abc", "def"))
d = list(zip([1, 2, 3], [4, 5, 6], [7, 8]))
print(a)
print(b)
print(c)
print(d)