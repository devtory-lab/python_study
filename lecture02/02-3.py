#리스트의 인덱싱
a = [1, 2, 3, 4, 5]
print(a[0])
print(a[0:2])

#중첩 리스트 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

#리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

#리스트 반복하기(*)
print(a * 3)

#리스트 길이구하기
print("#리스트 길이구하기")
print(len(a))

#리스트에서 값 수정하기
a[2] = 4
print(a)

#del 함수 사용해 리스트 요소 삭제하기
del a[1]
print(a)

del a[1:]
print(a)

#리스트에 요소 추가(append)
a.append(2)
a.append(3)
a.append(4)
print(a)

a.append([1,2,3,4])
print(a)

#리스트 정렬(sort)
a = ['a', 'c', 'b']
a.sort()
print(a)
print(a.index('a'))
print(a.index('c'))

#위치 반환(index)
a = [1, 2, 3, 4, 5]
print(a.index(2))
print(a.index(1))

#리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.sort()
print(a)

print("#리스트 요소 제거(remove)")
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
print(a.count(1))

#확장
a = [6, 8, 7]
a.extend([4, 5])
print(a)
b = [1, 2, 3]
a.extend(b)
a.sort()
print(a)

