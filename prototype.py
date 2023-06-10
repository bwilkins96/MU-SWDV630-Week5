# SWDV 630 - Object-Oriented Software Architecture
# Prototype base class and Room class inheriting from Prototype

# I also made a PrototypeFactory class

from copy import copy, deepcopy

class Prototype:
    """Prototype base class with methods for producing deep and shallow clones"""
    
    def clone(self):
        """Returns a deep clone of self"""
        return deepcopy(self)
    
    def shallow_clone(self):
        """Returns a shallow clone of self"""
        return copy(self)
    
class PrototypeFactory:
    """Prototype factory class that holds a registry of cloneable instances"""

    def __init__(self):
        """Sets up a PrototypeFactory instance with a registry"""
        self._registry = {}

    def register(self, key, obj):
        """Registers a Prototype instance to registry[key]"""
        if isinstance(obj, Prototype):         
            self._registry[key] = obj
            return True
        
        return False

    def get(self, key):
        """Returns a deep clone of the instance at registry[key]"""
        return self._registry[key].clone()
    
    def shallow_get(self, key):
        """Returns a shallow clone of the instance at registry[key]"""
        return self._registry[key].shallow_clone()
    
class Room(Prototype):
    def __init__(self, room_num, type, rate):
        self._room_number = int(room_num)
        self._type = type
        self._rate = float(rate)
        self._unavailable_dates = {}

    def get_room_number(self):
        return self._room_number
    
    def set_room_number(self, room_num):
        self._room_number = int(room_num)

    def get_type(self):
        return self._type

    def calculate_total(self, num_days):
        return self._rate * num_days
    
    def __repr__(self):
        return '{' + f'Room {self._room_number}: ${self._rate:.2f}' + '}'

def test():
    # Direct cloning
    room1 = Room(1, 'queen', 150)
    room2 = room1.clone()
    room2.set_room_number(2)

    # Cloning via a PrototypeFactory instance
    room_factory = PrototypeFactory()
    room_factory.register('queen', room1)
    room3 = room_factory.get('queen')
    room3.set_room_number(3)

    for room in [room1, room2, room3]:
        print(room)
        print(room.get_type())
        print()

    print(room1 is room2)    # -> False
    print(room1 is room3)    # -> False

if __name__ == '__main__': test()