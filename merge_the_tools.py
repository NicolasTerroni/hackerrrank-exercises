def merge_the_tools(string, k):
    while string:
        sub_string = string[:k]
        output = ""
        for i in sub_string:
            if i not in output:
                output+=i
        print(output)
        string = string[k:]
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
