# 04�� ��������
# Q1
# �־��� �ڿ����� Ȧ������ ¦������ �Ǻ��� �ִ� �Լ�(is_odd)�� �ۼ��� ����.
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

is_odd(3)
is_odd(6)


# Q2.
# �Է����� ������ ��� ���� ��� ���� ����� �ִ� �Լ��� �ۼ��� ����.
def avg(*args):
    result = 0
    for i in args:
        result = result + i
    return result / len(args)

avg(1,2,3)
avg(10, 20, 30)


