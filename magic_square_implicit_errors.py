def print_grid(ms):
    for row in ms:
        for col in row:
            print(col, end=' ')
        print()

def check_sums(square, n, magic_constant):
    sum_rows = [sum(i) for i in square]
    sum_cols = [sum(x) for x in zip(*square)]
    first_diag_sum =  sum(square[i][i]for i in range(n))
    second_diag_sum = sum(square[i][n-i-1]for i in range(n))

    for i in sum_rows:
        if i != magic_constant:
            print('rows do not equal magic constant')

    for i in sum_cols:
        if i != magic_constant:
            print('cols do not equal magic constant')

    if first_diag_sum != magic_constant:
            print('first diag does not equal magic constant')

    if second_diag_sum != magic_constant:
            print('second diag does not equal magic constant')

def create_odd_magic_square(n: int): #n is the length and width of the square
    """
    An odd magic square is defined as a magic squre of odd size: ex: 3x3, 5x5 ect... 
    Where all rows, cols, and diagonals add up to the same number, called the magic constant. 
    Numbers in the square consist of no repeats, and increment from 1 to n*n where n is the length and width of the square. 
    """
    #check if size is odd, if so preceed 
    if (n%2 > 0): #n is odd, so magic square is odd
        square = [[0 for i in range(n)] for i in range(n)]
        magic_constant = n*((n**2+1)/2) #all rows, cols, and diagonals must add to this number
        curr_col = int(((n+1)/2) - 1) #starting position 
        curr_row = 0
        last_num = n*n
        for num in range(last_num):
            square[curr_row][curr_col] = num + 1

            temp_row = curr_row-1
            temp_col = curr_col+1
            #if above top row then go to the bottom row same col 
            if temp_row < 0:
                temp_row = n-1 # go to bottom row 

            #if beyond last col then go to the first col same row
            if temp_col > (n-1):
                temp_col = 0
            
            #if occupied go back to previous filled box and place directly below (one row down same col)
            if square[temp_row][temp_col] != 0:
                temp_row = curr_row + 1
                temp_col = curr_col
            
            curr_row = temp_row
            curr_col = temp_col

        print_grid(square)
        check_sums(square, n, magic_constant)

        print(f'\nThe magic constant if this magic square is {int(magic_constant)}.')
        # print(f'\nThe row sums are {sum_rows}.\nThe col sums are {sum_cols}.\nThe first diagonal sum is {first_diag_sum}.\nThe second diagonal sum is {second_diag_sum}.\n')
    
    #odd size inputted 
    else:
        print(f'\n{n} is not an odd number. Please enter a size that is odd\n')
        
create_odd_magic_square(3)