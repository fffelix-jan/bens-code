from decimal import Decimal, getcontext

userWantsPrec = int(input("How precise do you want pi to be?: "))

def pi(precision):
    getcontext().prec=precision+1
    littleOff = sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
         Decimal(2)/(8*k+4) - 
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range(precision))
    getcontext().prec=precision
    return littleOff

print(pi(userWantsPrec))
