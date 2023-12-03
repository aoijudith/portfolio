import math

def cos(x,n):
    c=0
    for i in range(n):
        coef=(-1)**i
        num=x**(2*i)
        denom=math.factorial(2*i)
        c+=(coef)*((num)/(denom))
    return c
for n in range(10):
    print("Taylor Series:", cos(math.pi/3,n))
    c=cos(math.pi/3,n)-math.cos(math.pi/3)
    print("Error:", c)
  
print("Python value:", math.cos(math.pi/3))
