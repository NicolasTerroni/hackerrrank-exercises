def gen_letters_list(letters):
    """Generates the ragnoli rows."""
    letters.reverse()
    row = ""
    for i in letters:
        row = row+str(i)+"-"
    letters.reverse()
    letters.pop(0)
    for i in letters:
        row = row+str(i)+"-"
    row_letters_list = row.split("-")
    row_letters_list.pop()
    return row_letters_list

def print_rangoli(size):
    first_ascii_code = 97
    letters = []
    for i in range(size):
        letters.append(chr(first_ascii_code))
        first_ascii_code+=1
    
    
    second_half_ragnoli = []
    for i in range(len(letters)):
        row = gen_letters_list(letters)
        second_half_ragnoli.append(row)
    
    middle_row = []
    middle_row.append(second_half_ragnoli[0])
    second_half_ragnoli.pop(0)

    for i in second_half_ragnoli:
        middle_row.append(i)

    second_half_ragnoli.reverse()

    final_ragnoli = second_half_ragnoli + middle_row

    width = 4 * size - 3
    for i in final_ragnoli:
        string = ("-".join(i))
        print(string.center(width,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Wrost code that i have made in my life