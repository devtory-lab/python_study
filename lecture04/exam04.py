# 04장 연습문제
# Q1
# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

is_odd(3)
is_odd(6)


# Q2.
# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
def avg(*args):
    result = 0
    for i in args:
        result = result + i
    return result / len(args)

avg(1,2,3)
avg(10, 20, 30)


