# SWDV 630 - Object-Oriented Software Architecture
# Prototype base class and Room class inheriting from Prototype

from copy import copy, deepcopy

class Prototype:
    def clone(self):
        return deepcopy(self)
    
    def shallow_clone(self):
        return copy(self)
    
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

    def calculate_total(self, num_days):
        return self._rate * num_days
    
    def __repr__(self):
        return '{' + f'Room {self._room_number}: ${self._rate:.2f}' + '}'

def test():
    room1 = Room(1, 'queen', 150)
    room2 = room1.clone()
    room2.set_room_number(2)

    for room in [room1, room2]:
        print(room)
        print(room._type)
        print()

    print(room1 is room2)    # -> False

if __name__ == '__main__': test()