'''
class parameter:
    name='Nyxara'
model=parameter()
print(model.name)
'''
'''
class parameter:
    def __init__(self,name):
        self.name=name
model=parameter('Nyxara Ai')
model2=parameter('Nyxara')
print(model.name)
print(model2.name)
'''
'''
class parameter:
    def __init__(self,name):
        self.name=name
    def display(self):
        print('Model: ',self.name)
model=parameter('Nyxara Ai')
model2=parameter('Nyxara')
print(model.name)
print(model2.name)
model.display()
'''
'''
class parameter:
    def __init__(self,name):
        self.name=name
model=parameter('Nyxara Ai')
model2=parameter('Nyxara Ai')
model.name='Nyxara'
print(model.name)
print(model2.name)
'''
'''
class parameter:
    name='Nyxara Ai'
parameter.name='Nyxara'
model=parameter()
model2=parameter()
print(model.name)
print(model2.name)
'''