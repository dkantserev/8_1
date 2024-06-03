pets={}
b=1
def addPet(name,type,agr,o):
	Pet=dict(type=type,age=age,owner=o)
	
	pets[name]=Pet
def yearOrYears(age):
	r=''
	if age%10 ==1:
		r='год'
	elif age%10<5:
		r='года'
	else:
		r='лет'
	return r
while(b!=0):
	
    print('name pet')
    name=input()
    print('type')
    type=input()
    print('age')
    age=int(input())
    print('owner')
    owner=input()
    addPet(name,type,age,owner)
    print('Add another pet?.Enter 1. Enter 0 if not then')
    b=int(input())

for i in pets.keys():
	print('Это {type} по кличке "{name}". Возраст питомца: {age} {f}. Имя владельца: {owner}'.format(type=pets.get(i)['type'],name=i,age=pets.get(i)['age'],f=yearOrYears(pets.get(i)['age']),owner=pets.get(i)['owner']))
