'''
class MyClass():
    pass


first_object = MyClass()
print(type(first_object))

first_object.name = "My first object"
first_object.data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print(first_object.name)
print(first_object.data)


second_object = MyClass()
second_object.name = 'My second object'
second_object.data = {'numer': 89, 'color': 'red', 'numbers': [9, 9, 19, 88, 29, 6, 19, 84]}
second_object.complication = False

print(f'{second_object.name}')
print(f'{second_object.data}\n{second_object.complication}\n\n\n')

class MyClass2():
    def __init__(self):
        print('This is a sequention from f __init__')
    def function_one(self):
        print(f'Sequention {self.show_txt}')

seq = MyClass2()
seq.show_txt = '808 909 606'
seq.function_one()




class User():
    def cheer(self):
        print(f'\n\n\nczesc, jestem {self.name}')

    def say_hello(self, other, other2):
        print(f'Hey {other} and {other2}, I\'m {self.name}')

user = User()
user.name = 'Kleju'
user.cheer()
user.say_hello('Pączek', 'Harry')

#input('wcisnij Enter by zakonczyc')


class Cookie():
    pass

cookie = Cookie()
print(type(cookie))
print(type(cookie) is Cookie)
print(type(cookie) is not Cookie)
print(type(cookie).__name__)


name = 'pIoTr kLeJmEnT i kOOrnI aka sIIvA'


print(name)
print(name.capitalize())
print(name.upper())
print(name.lower())


text = 'Hej {name}, co u Was, wpadacie do {name1}, bedzie gral {name2}'
new_text = text.replace('{name}' , 'Bolek')

print(new_text)

new_text = new_text.replace('{name1}' , 'Berghain')
new_text = new_text.replace('{name2}', 'Dave Clarke')
print(new_text)

class ListOne():
    def list(self):
        list1 = [10, 9, 8, 7, 6, 5 ,4, 3 ,2 ,1 ,0]
        name = 'Kleju'
        x = 10
        if name == 'Kleju':
            list1.append('11')
            print(list1)
list_one = ListOne()
list_one.list()

'''




