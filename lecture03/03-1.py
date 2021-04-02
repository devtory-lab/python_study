# 03-1 if문
money = True
if money:
    print("택시를 타자")
else:
    print("버스를 타자")


money2 = 2000
if money2 >= 3000:
    print('택시!')
else:
    print('버스!')

print("============")

print("돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라.")
money = 2000
card = True
if money >= 3000 or card:
    print("택시")
else:
    print("버스")

x = [1,2,3]
print(1 in x)
print(1 not in [1, 2, 3])
print('a=', 'a' in ('a', 'b', 'c'))
print('j=', 'j' in ('a', 'b', 'c'))

print("=============")
print("만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라.")
pocket = ['money', 'card', 'cellphone']
if 'money' in pocket:
    print("택시")
else:
    print("버스")

print("=============")
pocket = ['cellphone', 'card']
card = True
if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("걸어가라")

print("==========한줄로===========")
score = 60
message = "success" if score >= 60 else "failure"
print(message)