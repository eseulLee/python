### tuple
'''
1. 소괄호() 사용
2. 데이터 수정, 추가 삭제 불가
3. indexing O
'''
A_tup = ('aa', 'bb', 'cc', 'dd')
print(A_tup)
print(type(A_tup))
print('indexing - ', A_tup[1], A_tup[-3])

### list
'''
1. 대괄호[] 사용
2. 데이터 수정, 추가 삭제 가능
3. indexing & slicing O
4. +,* 가능(리스트 자체로 연산) /,- 연산 X
'''
A_lst = ['aa', 'dd', 'cc', 'bb']
print(A_lst)
print(type(A_lst))
print('indexing - ', A_lst[2], A_lst[-4])
print('slicing  - ', A_lst[1:3])

# list 사칙연산
print(A_lst + A_lst) # list 뒤에 이어 붙음
print(A_lst * 3) # list 3번 반복
# print(A_lst - A_lst) -- error

# 데이터 수정
A_lst[2] = 'hello'
print(A_lst)

# 데이터 삭제
del A_lst[2]
print(A_lst)

# 데이터 추가
A_lst.append('ee')
print(A_lst)

# 내가 원하는 위치에 데이터 추가
A_lst.insert(2, 'cc')
print(A_lst)
A_lst.insert(0, 'ee')
print(A_lst)

# 데이터 개수 세기
print(A_lst.count('ee'))

# 데이터 지정해서 삭제
A_lst.remove('ee')
print(A_lst)  # remove : 가장 앞에 위치한 해당 데이터 삭제됨

# 가장 마지막에 있는 값 삭제
A_lst.pop()
print(A_lst)

# 데이터 정렬 ( sort 사용시 변수값에 즉시 반영되므로 주의 )
A_lst.sort()
print(A_lst)

### dictionary
'''
1. key, value 쌍으로 이루어져 있음
2. 중괄호 {} 사용, key:value 쌍 구분 기호는 세미콜론(,)
3. 데이터 수정, 추가 삭제 가능
4. 순서 존재 X , key 값으로 접근 
'''

A_dict = {'first'  : 'aa',
          'second' : 'dd',
          'third'  : 'cc',
          'forth'  : 'bb'}
print(A_dict)
print(type(A_dict))

# key 로 value 가져오기
print(A_dict['second'])

# 데이터 추가
A_dict['fifth'] =  'ff'
print(A_dict)

# 데이터 수정 : 동일 키 존재하는 경우 마지막 추가된 키:값만 살아남아 결론적으로 데이터 수정 발생
A_dict['fifth'] = 'ee'
print(A_dict)

# 데이터 삭제
del A_dict['second']
del A_dict['forth']
del A_dict['fifth']
print(A_dict)

A_dict['second'] = 'hello'
print(A_dict)

### set
'''
1. 중복된 데이터 없음
2. 데이터 간 순서 없음
3. set(), 중괄호{} 사용
'''
hello = set("hello")
hi = set(['h','i'])
print(hello, hi) # hello 의 경우, l 이 중복되므로 한개 삭제됨

# 교집합 연산
intersection01 = hello.intersection(hi)
print(intersection01)
intersection02 = hello & hi
print(intersection02)

# 합집합 연산
union01 = hello.union(hi)
print(union01)
union02 = hello | hi
print(union02)

# 차집합 연산 : 순서에 유의
diff01 = hello.difference(hi)
print(diff01)
diff02 = hello - hi
print(diff02)
diff03 = hi.difference(hello)
print(diff03)
diff04 = hi - hello
print(diff04)

# 원소 추가 > 순서 없으므로 임의의 위치에 들어가게 된다!
hello.add('!')    # 하나의 원소 추가
print(hello)

hello.update(['w','o','w'])  # 여러 개의 원소 한꺼번에 추가
print(hello)      # w 두개여서 하나만 들어가게 됨

hello.remove('w')  # 원소 삭제
print(hello)