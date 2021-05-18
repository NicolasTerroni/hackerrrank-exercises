import textwrap

def wrap(string, max_width):
    lst = textwrap.wrap(string,max_width)
    lst = "".join(lst)
    lst = textwrap.fill(lst,max_width)
    return lst

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)