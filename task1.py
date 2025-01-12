# initialisation
import time
n, m = input().split()  # n - rows number, m - pax number
seats_beg = []
n = int(n)
m = int(m)
x_beg = 0
left_x = 0
right_x = 0
left_seats = []
right_seats = []
j = 0
check = False
for i in range(n):
    seats_beg.append(list(input()))


start = time.time()


def get_inform():
    global seats_beg, left_x, right_x, left_seats, right_seats, n, x_beg
    for i in range(n):
        left_x += seats_beg[i][:3].count('X')
    for i in range(n):
        right_x += seats_beg[i][3:].count('X')
    x_beg = left_x + right_x
    for i in range(n):
        left_seats.append(seats_beg[i][:3])
        right_seats.append(seats_beg[i][:3])

get_inform()

# impossible situations
if m > (6 * n - x_beg):
    print('Impossible')
    print(time.time() - start)
    check = True
# if (x_beg % 2 != m % 2) and check == False:
#     print('Impossible')
#     print(time.time() - start)
#     check = True

# task 1
if m == 0 and check == False:
    if left_seats == right_seats:
        for i in range(n):
            print(''.join(seats_beg[i]))
        print(time.time() - start)
    else:
        print('Impossible')
        print(time.time() - start)
        check = True

# task 2
r = 0
if x_beg == 0 and check == False:
    if m % 2 == 0:
        while m != 0:
            if (r + 1) > n:
                check = True
                break
            if (m // 2) % 3 == 0:
                for i in range(0, 6):
                    seats_beg[r][i] = 'X'
                m -= 6
                r += 1
            elif (m // 2) % 2 == 0:
                for i in range(0, 2):
                    seats_beg[r][i] = 'X'
                for i in range(4, 6):
                    seats_beg[r][i] = 'X'
                m -= 4
                r += 1
            else:
                seats_beg[r][0] = 'X'
                seats_beg[r][5] = 'X'
                m -= 2
                r += 1
        if check == False:
            for i in range(n):
                print(''.join(seats_beg[i]))
            print(time.time() - start)
        else:
            print('Impossible')
            print(time.time() - start)
            check = True
    else:
        print('Impossible')
        print(time.time() - start)
        check = True

# task 3
if m == 1 and check == False:
    if abs(left_x - right_x) == 1 and x_beg != n * 6:
        i = 0
        while check != True or i < n:
            for j in range(3):
                if left_seats[i][j] != right_seats[i][5 - j]:
                    check = True
                    ch_val1 = i
                    ch_val2 = j
                    break
            i += 1
        if check == True:
            x_beg[ch_val1][ch_val2] = 'X'
            for i in range(n):
                print(''.join(seats_beg[i]))
            print(time.time() - start)
        else:
            print('Impossible')
            print(time.time() - start)
    else:
        print('Impossible')
        print(time.time() - start)

# taask 4
if x_beg == 1 and check == False:
    if m % 2 == 1:
        if (m - 1) < (n - 1) * 6:
            norm_arr = ['.'] * 6
            for i in range(n):
                if x_beg[i] != norm_arr:
                    ch_index = x_beg[i].index('X')
                    ch_row = i
                    x_beg[i][5 - ch_index] = 'X'
                    m -= 1
                    break
            r = 0
            while m != 0:
                if (r + 1) > n:
                    check = True
                    break
                if r == ch_row:
                    pass
                elif (m // 2) % 3 == 0:
                    for i in range(0, 6):
                        seats_beg[r][i] = 'X'
                    m -= 6
                    r += 1
                elif (m // 2) % 2 == 0:
                    for i in range(0, 2):
                        seats_beg[r][i] = 'X'
                    for i in range(4, 6):
                        seats_beg[r][i] = 'X'
                    m -= 4
                    r += 1
                else:
                    seats_beg[r][0] = 'X'
                    seats_beg[r][5] = 'X'
                    m -= 2
                    r += 1
            if check == True:
                x_beg[ch_val1][ch_val2] = 'X'
                for i in range(n):
                    print(''.join(seats_beg[i]))
                print(time.time() - start)
        else:
            print('Impossible')
            print(time.time() - start)
    else:
        print('Impossible')
        print(time.time() - start)
