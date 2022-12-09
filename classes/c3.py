import random
class MyList(list):                           # inherits from list  [list has 11 functions]
    def shuffle(self):
        random.shuffle(self)

    def get_random(self):
        return random.choice(self)

    
# object

a=MyList([12,121,3,34,1,567,56])
a.sort()
print(a)
a.shuffle()
print(a)
print('random item from list=', a.get_random())