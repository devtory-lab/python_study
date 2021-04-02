#집합 자료형
s1 = set([3,2,1])
print(s1)

s2 = set("Hello")
print(s2)

#집합 자료형의 특징
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).

l2 = list(s2)
print(l2)
print(l2[0])

t1 = tuple(s1)
print(t1)
print("===============")

#교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print("교집합", s1 & s2, s1.intersection(s2))
print("합집합", s1 | s2, s1.union(s2))
print("차집합", s1 - s2, s1.difference(s2), s2.difference(s1))

#값 1개 추가하기(add)
s1 = set([1,2,3,4])
s1.add(5)
print(s1)

#값 여러 개 추가하기(update)
s1.update([6,7,8])
print(s1)

#특정 값 제거하기(remove)
s1.remove(8)
print(s1)