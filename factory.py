# SWDV 630 - Object-Oriented Software Architecture
# Factory for producing Person instances

from datetime import date
from person import Guest, Employee, Manager

class PersonFactory:
    
    @classmethod
    def create(cls, type, *args, **kwargs):
        type = type.strip().lower()

        if type == 'guest':
            return Guest(*args, **kwargs)
        elif type == 'employee':
            return Employee(*args, **kwargs)
        elif type == 'manager':
            return Manager(*args, **kwargs)

def test():
    guest = PersonFactory.create('guest', 101, 'Brandon', date.today(), None)
    employee = PersonFactory.create('employee', 20, 'Hannah', date.today(), None) 
    manager = PersonFactory.create('manager', 110, 25, 'Bridgett', date.today(), None)

    for person in [guest, employee, manager]:
        print(type(person))

if __name__ == '__main__': test()