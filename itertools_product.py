from itertools import product

if __name__ == "__main__":
    A = map(int,(input().split(" ")))
    B = map(int,(input().split(" ")))

    lst = list(product(A,B))
    for i in lst:
        print(i,end=" ")