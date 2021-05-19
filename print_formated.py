def print_formatted(number):
    last_binary_length =  len(bin(number)[2:])

    for i in range(1,number+1):
        print(str(i).rjust(last_binary_length),end=" ")
        print(str(oct(i)[2:]).rjust(last_binary_length),end=" ")
        print(str(hex(i)[2:].upper()).rjust(last_binary_length),end=" ")
        print(str(bin(i)[2:]).rjust(last_binary_length))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
