# SWDV 630 - Object-Oriented Software Architecture
# Stay class and Proxy for Stay class

from datetime import date

class Stay:
    def __init__(self, room, start, end): 
        self._room = room
        self._checked_in = False
        self._start = start
        self._end = end

    def checked_in(self):
        return self._checked_in

    def check_in(self):
        self._checked_in = True
        self._start = date.today()

    def check_out(self):
        self._checked_in = False
        self._end = date.today()

class StayProxy:
    _total_count = 0
    _checked_in_count = 0

    def __new__(cls, *args):
        instance = object.__new__(cls)
        cls.incr_total()
        return instance

    def __init__(self, stay):
        self._stay = stay

    def check_in(self):
        self._stay.check_in()
        self.incr_checked_in()

    def check_out(self):
        self._stay.check_out()
        self.decr_checked_in()

    @classmethod  
    def get_total(cls):
        return cls._total_count
    
    @classmethod
    def get_checked_in(cls):
        return cls._checked_in_count

    @classmethod
    def incr_total(cls):
        cls._total_count += 1

    @classmethod
    def decr_total(cls):
        cls._total_count -= 1

    @classmethod
    def incr_checked_in(cls):
        cls._checked_in_count += 1

    @classmethod
    def decr_checked_in(cls):
        cls._checked_in_count -=1
    
    def __getattr__(self, name):
        return getattr(self._stay, name)

    def __del__(self):
        if self._stay.checked_in():
            self.check_out()

        self.decr_total()

def test():
    proxy_list = []

    for i in range(20):
        proxy = StayProxy(Stay(i, None, None))
        proxy.check_in()
        proxy_list.append(proxy)

    print(StayProxy.get_total())               # -> 20 
    print(StayProxy.get_checked_in(), '\n')    # -> 20

    for i in range(10):
        proxy_list[i].check_out()

    print(StayProxy.get_total())               # -> 20 
    print(StayProxy.get_checked_in(), '\n')    # -> 10

    del proxy_list[10:15]

    print(StayProxy.get_total())               # -> 15 
    print(StayProxy.get_checked_in())          # -> 5

if __name__ == '__main__': test()