from collections import Counter

num_shoes = int(input())
shoes = Counter(map(int, input().split()))
customers = int(input())

income = 0

for i in range(customers):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)
    
#import pdb; pdb.set_trace()