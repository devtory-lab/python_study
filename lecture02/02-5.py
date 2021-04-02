#딕셔너리 자료형
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic['name'] + ", " + dic['phone'] + ", " + dic['birth'])

#딕셔너리 쌍 추가하기
dic['ttt'] = [1,2,3]
dic[3] = (1,2,3)
print(dic)

#딕셔너리 요소 삭제하기
del(dic[3])
print(dic)

#딕셔너리 만들 때 주의할 사항! key 중복시, 뒷 key만 사용가능하다
a = {1:'a', 2:'b'}
print(a)

#Key 리스트 만들기(keys)
print(dic.keys())

for k in dic.keys():
    print(k, dic.get(k))

list(a.keys())
print(a.values())
print('a.items()=', a.items())

a.clear()
print(a)

#Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))