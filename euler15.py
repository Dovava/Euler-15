import math
distance = 20
def fa(n):
    return math.factorial(n)
def calculate(n,k):
    return int(fa(n)/(fa(n-k)*fa(k)))
answer = calculate(distance*2, distance)
print(answer)
