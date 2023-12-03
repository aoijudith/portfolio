import math

def solution1(a,b,c):
    ans1, ans2=(-b+(b**2-4*a*c)**0.5)/(2*a), (-b-(b**2-4*a*c)**0.5)/(2*a)
    return ans1, ans2

for n in range(10):
    s1n1=solution1(1,1,10**(-n))
    print("n=",n, s1n1)
