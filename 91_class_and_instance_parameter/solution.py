class Person:
    name = 'Person'

    def __init__(self, name=None):
        self.name = name

dels = Person('Del')

print('%s name is %s' % (Person.name, dels.name))

nico = Person()
nico.name = 'nico'

print('%s name is %s' % (Person.name, nico.name))