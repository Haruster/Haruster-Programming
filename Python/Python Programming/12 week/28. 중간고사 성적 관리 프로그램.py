# 중간고사 성적 관리 프로그램

scores = {'C/C++' : 'A', 'Java' : 'B+', '모바일' : 'A', '보안' : 'A+', '해킹' : 'A+', '시스템' : 'A+'}

print('#시나리오1 ')
print(scores)

print('#시나리오2 ')
print('Java : ', scores['Java'])
print('시스템 : ', score['시스템'])

print('#시나리오3 ')
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(scores)


print('#시나리오4 ')
scores['Java'] = 'A'
scores['시스템'] = 'A'
print(scores)

print('#시나리오5 ')

for key in scores.keys():

    print(key, '\t:', scores[key])