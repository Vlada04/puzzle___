def validate_board(board):
    '''
    Check whether the logic puzzle playing field is ready to start the game.
    The colored cells of each line must\
    contain numbers from 1 to 9 without repetition.

    The colored cells of each column must\
    contain the numbers 1 to 9 without repetition.


    Each block of cells of the same color must\
    contain numbers from 1 to 9 without repetitiion.
    >>> print(validate_board(["**** ****", "***1 ****", "**  3****",\
    "* 4 1****", "     9 5 ", " 6  83  *", "3   4  **", "  8  2***", "  2  ****"]))
    True
    '''
    k = 0
    lst = []
    for i in board:
        for num in range(1, 9):
            if i.count(str(num)) > 1:
                return False

    while k != 9:
        lst1 = [i[k] for i in board]
        lst.append(lst1)
        k += 1
    lst1 = []

    for l in lst:
        for num in range(1, 9):
            if l.count(str(num)) > 1:
                return False
    
    list1 = []
    list2 = []
    list1.append(board[4:])
    for u in list1:
        list2.append(u[0][4:])
        list2.append(u[1][3:])
        list2.append(u[2][2:])
        list2.append(u[3][1:])
        list2.append(u[4][0:])

    list3 = []
    list3.append(lst[4:][0])
    list3.append(lst[4:][1][:-1])
    list3.append(lst[4:][2][:-2])
    list3.append(lst[4:][3][:-3])
    list3.append(lst[4:][4][:-4])

    res_list = zip(list2, list3)
    for i in list(res_list):
        for num in range(1, 9):
            r = i[0].count(str(num))
            R = i[1].count(str(num))
        if r + R > 2:
            return False
    return True
print(validate_board([
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   4  **",
 "  8  2***",
 "  2  ****"
]))