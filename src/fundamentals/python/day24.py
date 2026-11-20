'''
class parameter:
    def __init__(self):
        self.__name='Nyxara'
model=parameter()
model.__name='Nyxara Ai'
print(model.__name)
print(model._parameter__name) 
print(model.__dict__)
'''
'''
class parameter:
    def __init__(self):
        self._name='Nyxara'
model=parameter()
model._name='Nyxara Ai'
print(model._name)
'''

class parameter:
    def __init__(self):
        self.name='Nyxara'
model=parameter()
model.name='Nyxara Ai'
print(model.name)