if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

scores = [i for i in list(arr)]
scores.sort(reverse=True)
champion = int(scores[0])
try:
    runner_up = [i for i in scores if i != champion][0]
except IndexError:
    runner_up = champion
print(runner_up)