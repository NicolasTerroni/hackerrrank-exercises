def swap_case(s):
    char_list = []
    for i in s:
        if i == i.upper():
            char_list.append(i.lower())
        elif i == i.lower():
            char_list.append(i.upper())
        else:
            char_list.append(i)
    swaped_string = ''.join(char_list)
    return swaped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)