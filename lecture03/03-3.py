# 03-3 for문
# for 변수 in 리스트(또는 튜플, 문자열):
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print("===============")

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

print("===============")

print("총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.")
marks = [90, 25, 67, 45, 80]
i = 0
for mark in marks:
    i = i + 1
    if mark >= 50:
        print("%d번째 학생의 %d 점수는 합격입니다." % (i, mark))
    else:
        print("%d번째 학생의 %d 점수는 불합격입니다." % (i, mark))

print("===============")

i = 0
for mark in marks:
    i = i + 1
    if mark < 60: continue
    print("%d번째 학생의 %d 점수는 합격입니다." % (i, mark))

print("===============")
print(range(10))

add = 0
for i in range(1, 11):
    add = add + i

print(add)
print("===============")

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번째 학생의 %d 점수는 합격입니다." % (number+1, marks[number]))

print("========구구단======")
for i in range(2, 10):
    for j in range(1, 10):
        print(str(i) + " * " + str(j) + " = "+ str(i*j), end=", ")
    print("")

print("========리스트 내포 for ======")
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

#만약 [1,2,3,4] 중에서 짝수에만 3을 곱하여 담고 싶다
result = [num*3 for num in a if num % 2 == 0]
print(result)


