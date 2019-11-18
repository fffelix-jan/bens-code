from decimal import *
from decimal import Decimal as dec
print("Max")
max = int(input())
getcontext().prec = max
x = dec(0)
a = dec(0)
pi = dec(0)
while max > x:
    a = dec((dec(1) / dec(16) ** dec(x)) * (dec(4) / (dec(8) * x + dec(1)) - dec(2) / (dec(8) * x + dec(4)) - dec(1) / (dec(8) * x + dec(5)) - dec(1) / (dec(8) * x + dec(6))))
    pi = a + dec(pi)
    x = int(x) + 1
    print(pi)
print(len(pi))


