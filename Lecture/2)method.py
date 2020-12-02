a = 'Hello World'

#length
print('a의 길이 : ',len(a))

#index
print('a의 4번째 문자 : ',a[1])
print('a의 4번째 문자 : ',a[2:5])

#repeat
print('a의 2번 반복 : ',(a + ' ') * 2)

#format
print('format :  {} {} {} {}'.format('egoing',1,'Hello',2))

#name placeholder
print('format :  {name} {age} {name} {age}'.format(name = 'Hello', age = 1))