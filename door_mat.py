if __name__ == '__main__':
    heigth ,width = map(int,input().split())
    string = '.|.'
    middle_mat = ["WELCOME".center(width,'-'),]
    first_half_mat = []
    count = 1
    for i in range(heigth//2):
        first_half_mat.append((string*count).center(width,'-'))
        count+=2
    count = 1

    door_mat = first_half_mat+middle_mat
    first_half_mat.reverse()
    door_mat = door_mat+first_half_mat

    for i in door_mat:
        print(i)