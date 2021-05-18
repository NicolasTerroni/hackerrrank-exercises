if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    isdigit = False
    islower = False
    isupper = False
    for i in range(len(s)):
        if s[i].isalnum():
            alnum = True
        if s[i].isalpha():
            alpha = True
        if s[i].isdigit():
            isdigit = True
        if s[i].islower():
            islower = True
        if s[i].isupper():
            isupper = True
    print(alnum)
    print(alpha)
    print(isdigit)
    print(islower)
    print(isupper)