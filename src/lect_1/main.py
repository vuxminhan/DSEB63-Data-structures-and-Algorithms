class CreditCard:
    def __init__(self, customer, bank, account, balance, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._balance = balance
        self._limit = limit

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_balance(self):
        return self._balance

    def charge(self, amount):
        if (self._balance + amount) > self._limit:
            print("You have exceeded spending limit")
        else:
            self._balance += amount
            print(f"Your current balance is {self._balance}")

    def makepayment(self, amount):
        if (self._balance >= amount):
            self._balance -= amount
            print(f"Your current balance is {self._balance}")
        else:
            print("Your balance is not sufficient")


#
# m = CreditCard('Minh',"vietin","1234567",10000, 1000000)
# m.charge(100)
# m.makepayment(10000)

class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def __add__(self, other):
        return Vector(self._x + other.getx(), self._y + other.gety())

    def __sub__(self, other):
        return Vector(self._x - other.getx(), self._y - other.gety())

    def __mul__(self, other):
        return Vector(self._x * other.getx() + self._x * other.gety(), self._y * other.getx() + self._y * other.gety())

    def __pow__(self, power, modulo=None):
        return Vector(self._x * power, self._y * power)

    def __repr__(self):
        return f"({self._x},{self._y})"


a = Vector(2, 3)
b = Vector(1, 1)
scalar = 3
c = a ** 3
d = a+b
e = a-b
f = a*b
print(repr(c))
print(repr(e))
print(repr(d))
print(repr(f))



