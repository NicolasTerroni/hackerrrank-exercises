import os
def solve(s):
    words = s.split(" ")
    result = [s.capitalize() for s in words]
    result = " ".join(result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
