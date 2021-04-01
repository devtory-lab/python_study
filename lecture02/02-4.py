#튜플
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(t5)

#인덱싱하기
t1 = (1, 2, 'a', 'b')
print(t1)
print(t1[0], t1[3])

#슬라이싱
print(t1[1:])

#튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2)

#튜플 곱하기
print(t2 * 3)

#튜플 길이 구하기
print(len(t2))