
for x in range(10):
    print(x, x**2)

my_input = 'hello world'
print(my_input)

#my_name = input('dear world')  # 실행하면 exit로 나갈 수 없음 why? input 함수랑 관련 있음
#print(my_name)

for y in range(10):
    print(y)
    print("위 숫자의 2승은 ?")
    print(y**2)

pocket = [4,6,1,9]
print(pocket)
print(pocket[1])
print(pocket[-1])
pocket.append(7)
print(len(pocket))
print(pocket)
pocket.remove(6)
print(pocket)
pocket.insert(1,3)
print(pocket)
print(pocket.pop(3))
print(pocket)
print(pocket[1:3])
print(pocket[:3])
print(pocket)
pocket_copy = pocket
pocket_copy.append(1)
print(pocket_copy)
print(id(pocket))
print(id(pocket_copy))

a = [1,2,3]
b = [4,5,6]
c = a + b
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))

a.extend(b)
print(a)
print(c)
print(id(a))
print(id(c))

print(a)
del a[0]
print(a)

programming = ['python','qt','c++']
print(programming)

singleton = '안녕하세요',
print(singleton)
print(type(singleton))

empty = ()
print(type(empty))


movie = '슈퍼맨','아이언맨','슈퍼네츄럴'
movie_list = list(movie)
print(type(movie_list))
print(type(movie))

signals = 'blue','yellow','red'

for signal in signals:
    print(signal,len(signal))