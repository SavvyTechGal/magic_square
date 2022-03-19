def print_grid(ms):
    for row in ms:
        for col in row:
            print(col, end=' ')
        print()

def check_sums(square, n, magic_constant) -> bool:
    sum_rows = [sum(i) for i in square]
    sum_cols = [sum(x) for x in zip(*square)]
    first_diag_sum =  sum(square[i][i]for i in range(n))
    second_diag_sum = sum(square[i][n-i-1]for i in range(n))

    for i in sum_rows:
        if i != magic_constant:
            return 'False'

    for i in sum_cols:
        if i != magic_constant:
            return 'False'

    if (first_diag_sum != magic_constant) or (second_diag_sum != magic_constant):
        return 'False'
    
    return 'True'

def create_odd_magic_square(n: int): #n is the length and width of the square
    """
    An odd magic square is defined as a magic squre of odd size: ex: 3x3, 5x5 ect... 
    Where all rows, cols, and diagonals add up to the same number, called the magic constant. 
    Numbers in the square consist of no repeats, and increment from 1 to n*n where n is the length and width of the square. 
    """
    #check if size is odd, if so preceed 
    if (n%2 > 0): #n is odd, so magic square is odd
        square = [[-1 for i in range(n)] for i in range(n)]
        magic_constant = n*((n^2+1)/2) #all rows, cols, and diagonals should add to this number
        curr_col = int(((n+1)/2) -1) #starting position (subtract one because arrays start at 0)
        curr_row = 0
        last_num = n*n
        for num in range(last_num):
            square[curr_row][curr_col] = num

            curr_row-=1
            curr_col+=1
            #if above top row then go to the bottom row same col 
            if curr_row < 0:
                curr_row = n-1 # go to bottom row 

            #if beyond last col then go to the first col same row
            if curr_col > (n-1):
                curr_col = 0
            
            #if occupied go back to previous filled box and place directly below (one row down same col)
            if square[curr_row][curr_col] != -1:
                curr_row += 1
            

        print()
        print_grid(square)
        is_magic_square = check_sums(square, n, magic_constant)
        print(f'For size {n}*{n} with expected magic constant of {int(magic_constant)}: Magic Square is: {is_magic_square}\n')
    #odd size inputted 
    else:
        print(f'\n{n} is not an odd number. Please enter a size that is odd\n')
        
create_odd_magic_square(3)