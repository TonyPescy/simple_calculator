#######################################################################################################################################
# Title: calculations
# Author: Tony Pescatore
# Description: This will hold all the functions to do all the calculations done
#######################################################################################################################################

# imports
import symbols

# constants
INCREMENT = 1           # used to increment by 1
DBL_INCREMENT = 2       # double increment, used to increment by 2
FIRST_ELEMENT = 0       # used to access the first element

# functions

# remove_str Starts
# Description: adds the two numbers together
# Parameters:   s - String - string that will be modified
#               start - int - number to be start at
#               end - int - number to end at (inclusive)
# Returns:      String - string with desired section removed
def remove_str(s, start, end):
    return (s[:start] + s[end + 1:])

# plus Starts
# Description: adds the two numbers together
# Parameters:   num1 - String - number to be added
#               num2 - String - number to be added
# Returns:      ans - String - added numbers
def plus(num1, num2):
    ans = int(num1) + int(num2)
    return ans

# minus Starts
# Description: subtracts the two numbers
# Parameters:   num1 - String - starting number
#               num2 - String - number to be subtracted
# Returns:      ans - String - subtracted numbers
def minus(num1, num2):
    ans = int(num1) - int(num2)
    return ans

# multiply Starts
# Description: adds the two numbers together
# Parameters:   num1 - String - number to be added
#               num2 - String - number to be added
# Returns:      ans - String - product
def multiply(num1, num2):
    ans = int(num1) * int(num2)
    return ans

# divide Starts
# Description: subtracts the two numbers
# Parameters:   num1 - string - starting number
#               num2 - string - number to do division
# Returns:      ans - string - quotient
def divide(num1, num2):
    ans = int(num1) / int(num2)
    return ans

# exponent Starts
# Description: does calculations for exponents
# Parameters:   num1 - String - starting number
#               num2 - String - exponent
# Returns:      ans - String - product
def exponent(num1, num2):
    ans = int(num1) ** int(num2)
    return ans

# inverse Starts
# Description:  gets inverse of the number
# Parameters:   num1 - String - starting number
#               num2 - String - negative one
# Returns:      ans - String - product
def inverse(num):
    ans = int(num) * -INCREMENT
    return ans

# total_num_of_par Starts
# Description:  gets total number or parenthesis in the equation
# Parameters:   equ - list - equation
# Returns:      pars - int - total number of parenthesis found in the equation
def total_num_of_par(equ):
    pars = 0
    for i in range(len(equ)):
        pars += INCREMENT 
    return pars


# calc_input Starts
# Description: calculates the equation from the users input
# Parameters:   equ - List - user inputted equation from calculator buttons
#               length_of_equ_before - int - number representing the length of the equation
# Returns:      fin_list - List - [fin_result, number_of_chars]
#               fin_result - the solved equation  ----  number_of_chars of equation entered 
def calc_input(equ, length_of_equ_before):
    # local variables
    to_insert = []          # empty list to save the new numbers we will use to build the new equation
    sym_count = 0           # variable to count how much a symbol occurs
    n_n_count = 0           # variable to count how much new numbers there are
    num_of_l_par = 0        # number of left parenthesis set to 0 as none are found
    num_of_r_par = 0        # number of right parenthesis set to 0 as none are found

    # PnEMDAS
    # parenthesis start
    # for i in range(len(equ)):
    #     if equ[i] == symbols.L_PAR:     # starting parenthesis
    #         count = i + INCREMENT       # initializes count to position of first 
    #         new_equ = []

    #         while equ[count] != symbols.R_PAR:  # while the parenthesis are not closed
    #             new_equ.append(equ[count])          # creating a new list from within the parenthesis
    #             count += INCREMENT
    #             print(count)
        
    #         print(new_equ)
    #         solved_new_equ = calc_input(new_equ)        # uses new list and recursion to solve equation in the parenthesis
    #         print(solved_new_equ[FIRST_ELEMENT])

    #         equ.insert(i, solved_new_equ[FIRST_ELEMENT])
    #         for n in range(count):                      # removes all charcters involved in parenthesis and it equation to make room for the insert of the solved equation
    #             equ.pop(i - DBL_INCREMENT)

    #         equ.insert(i, solved_new_equ[FIRST_ELEMENT])
    #         if equ[i - INCREMENT] != symbols.ADD or equ[i - INCREMENT] != symbols.SUB or equ[i - INCREMENT] != symbols.MUL or equ[i - INCREMENT] != symbols.DIV or equ[i - INCREMENT] != symbols.EXP:       # if any of the symbols are not in front of the parenthesis
    #             equ.insert(i - INCREMENT, symbols.MUL)  # inserts multiplication symbol so that calculator knows what to do
            
    #         if equ[i - DBL_INCREMENT] != symbols.ADD or equ[i - DBL_INCREMENT] != symbols.SUB or equ[i - DBL_INCREMENT] != symbols.MUL or equ[i - DBL_INCREMENT] != symbols.DIV or equ[i + DBL_INCREMENT] != symbols.EXP:   # if any of the symbols are not behind the parenthesis
    #             equ.insert(i + DBL_INCREMENT, symbols.MUL)  # inserts multiplication symbol so that calculator knows what to do

    #         else:           # if there are symbols before and after the parenthesis
    #             continue    # continues to interate through the rest of string

    for i in range(len(equ)):

        tot_par_pairs = total_num_of_par(equ)       # gets total number of parernthesis

        if equ[i] == symbols.L_PAR:
            num_of_l_par += INCREMENT   # increments number of left parenthesis
        elif equ[i] == symbols.R_PAR:
            num_of_r_par += INCREMENT   # increments number of right parenthesis

        if num_of_l_par == num_of_r_par and num_of_l_par != 0:    # found the ending point of parenthesis at i
            start_ind = equ.index(symbols.L_PAR)
            new_equ = equ[start_ind + INCREMENT:i]

            print(str(new_equ) + "THIS IS THE PARENTHESIS NUM" + str(num_of_l_par))

            # if num_of_l_par == INCREMENT:  
            #     # to_insert = [new_num, number_of_nums_to_remove, starting_index, ending_index]
            #     temp_solved = calc_input(new_equ, len(new_equ))
            #     print("THIS IS TEMP SOLVED", temp_solved)

            #     indices = i - start_ind
            #     print("THIS IS INDICES", indices)
            #     for n in range(len(temp_solved[0])):
            #         equ.pop(n)

            #     equ.insert(indices, temp_solved[0])
            #     print("TEST", equ)

            # else:
            #     temp_solved = calc_input(new_equ, len(new_equ))
            #     print("THIS IS TEMP SOLVED (ELSE)", temp_solved)


            
        

    # parenthesis end

    # negatives start
    # second symbol as it must be done before all others to avoid issues with symbols be treated as ints
    # to_insert = [new_num, insert_num, old_num]
    for i in range(len(equ)):
        if equ[i] == symbols.NEG:                                               # checks for negative in the equation
            new_num = inverse(equ[i + INCREMENT])
            to_insert.append([new_num, i + DBL_INCREMENT, equ[i + INCREMENT]])  # increments take in account for insert of new_num
    
    for i in range(len(to_insert)):                                             # if there are multiple negative numbers in to_insert it will interate over all of them
        equ.insert(to_insert[i][INCREMENT], to_insert[i][FIRST_ELEMENT])
        # removes all symbols and numbers involved
        equ.remove(symbols.NEG)
        equ.remove(to_insert[i][inverse(INCREMENT)])
    
    # resets
    to_insert = []                                                              # to_insert list reset
    # negatives end

    # exponents start
    # to_insert = [new_num, index_of_num1, index_of num2]
    for i in range(len(equ)):
        if equ[i] == symbols.EXP:                                           # checks for exponent in the equation
            new_num = exponent(equ[i - INCREMENT], equ[i + INCREMENT])
            n_n_count += 1                                                  # counts the new number
            sym_count += 1                                                  # counts the symbols
            to_insert.append([new_num, i - INCREMENT, i + INCREMENT])       # fills to_insert with new_num, and the numbers on either side of the symbol

    # below removes all that have been solved in the equation, all that remains are the rest of the equation and the symbols
    for i in range(n_n_count):
        if n_n_count >= 0:
            n_n_count = n_n_count - 1

            equ.pop((to_insert[n_n_count][INCREMENT]))                      # removes the number in front of the "^"
            equ.pop((to_insert[n_n_count][DBL_INCREMENT]) - INCREMENT)      # removes the number after the "^", takes in account that the last num was just removed
    # removes all symbols and inserts new number
    for i in range(sym_count):
        temp_ind = equ.index(symbols.EXP)                       # gets index to replace at
        equ.pop(temp_ind)                                       # pops symbol
        equ.insert(temp_ind, to_insert[i][FIRST_ELEMENT])       # inserts new number
    
    # resets
    to_insert = []  # to_insert list reset
    n_n_count = 0   # n_n_count reset
    sym_count = 0   # sym_count reset
    # exponents end

    # multiplication/division starts
    for i in range(len(equ) - INCREMENT):
        if equ[i] == symbols.MUL:                                                           # checks for mutliplication in the equation
            new_num = multiply(equ[i - INCREMENT], equ[i + INCREMENT])
            n_n_count += 1                                                                  # counts the new number
            sym_count += 1                                                                  # counts the symbols
            to_insert.append([new_num, i - INCREMENT, i + INCREMENT, symbols.MUL])          # increments take in account for insert of new_num
        if equ[i] == symbols.DIV:                                                           # checks for division in the equation
            new_num = divide(equ[i - INCREMENT], equ[i + INCREMENT])
            n_n_count += 1                                                                  # counts the new number
            sym_count += 1                                                                  # counts the symbols
            to_insert.append([new_num, i - INCREMENT, i + INCREMENT, symbols.DIV])          # increments take in account for insert of new_num

    # below removes all that have been solved in the equation, all that remains are the rest of the equation and the symbols
    for i in range(n_n_count):
        if n_n_count >= 0:
            n_n_count = n_n_count - 1

            equ.pop((to_insert[n_n_count][INCREMENT]))                      # removes the number in front of the symbol
            equ.pop((to_insert[n_n_count][DBL_INCREMENT]) - INCREMENT)      # removes the number after the symbol, takes in account that the last num was just removed
    # removes all symbols and inserts new number
    for i in range(sym_count):
        temp_sym = to_insert[i][inverse(INCREMENT)]                 # gets symbol of operation
        if temp_sym == symbols.MUL:                                 # if it is "x"
            temp_ind = equ.index(symbols.MUL)                       # gets index to replace at
            equ.pop(temp_ind)                                       # pops symbol
            equ.insert(temp_ind, to_insert[i][FIRST_ELEMENT])       # inserts new number

        else:                                                       # if it is "÷"
            temp_ind = equ.index(symbols.DIV)                       # gets index to replace at
            equ.pop(temp_ind)                                       # pops symbol
            equ.insert(temp_ind, to_insert[i][FIRST_ELEMENT])       # inserts new number

    # resets
    to_insert = []  # to_insert list reset
    n_n_count = 0   # n_n_count reset
    sym_count = 0   # sym_count reset
    # multiplication/division ends

    # addition/subtraction starts
    for i in range(len(equ)):
        if equ[i] == symbols.ADD:                                                           # checks for addition in the equation
            new_num = plus(equ[i - INCREMENT], equ[i + INCREMENT])
            n_n_count += 1                                                                  # counts the new number
            sym_count += 1                                                                  # counts the symbols
            to_insert.append([new_num, i - INCREMENT, i + INCREMENT, symbols.ADD])          # increments take in account for insert of new_num
        if equ[i] == symbols.SUB:                                                           # checks for subtraction in the equation
            new_num = minus(equ[i - INCREMENT], equ[i + INCREMENT])
            n_n_count += 1                                                                  # counts the new number
            sym_count += 1                                                                  # counts the symbols
            to_insert.append([new_num, i - INCREMENT, i + INCREMENT, symbols.SUB])          # increments take in account for insert of new_num

    # below removes all that have been solved in the equation, all that remains are the rest of the equation and the symbols
    for i in range(n_n_count):
        if n_n_count >= 0:
            n_n_count = n_n_count - 1

            equ.pop((to_insert[n_n_count][INCREMENT]))                      # removes the number in front of the symbol
            equ.pop((to_insert[n_n_count][DBL_INCREMENT]) - INCREMENT)      # removes the number after the symbol, takes in account that the last num was just removed
    # removes all symbols and inserts new number
    for i in range(sym_count):
        temp_sym = to_insert[i][inverse(INCREMENT)]                 # gets symbol of operation
        if temp_sym == symbols.ADD:                                 # if it is "+"
            temp_ind = equ.index(symbols.ADD)                       # gets index to replace at
            equ.pop(temp_ind)                                       # pops symbol
            equ.insert(temp_ind, to_insert[i][FIRST_ELEMENT])       # inserts new number

        else:                                                       # if it is "-"
            temp_ind = equ.index(symbols.SUB)                       # gets index to replace at
            equ.pop(temp_ind)                                       # pops symbol
            equ.insert(temp_ind, to_insert[i][FIRST_ELEMENT])       # inserts new number

    # resets
    to_insert = []  # to_insert list reset
    n_n_count = 0   # n_n_count reset
    sym_count = 0   # sym_count reset
    # addition/subtraction ends

    fin_result = [str(equ), length_of_equ_before]   # coverts final result into a string for display
    
    return fin_result

def main():                                                                    # [new_num, index_of_num1, index_of num2]

    # local variables
    to_insert = []          # empty list to save the new numbers we will use to build the new equation
    sym_count = 0           # variable to count how much a symbol occurs
    n_n_count = 0           # variable to count how much new numbers there are
    num_of_l_par = 0        # number of left parenthesis set to 0 as none are found
    num_of_r_par = 0        # number of right parenthesis set to 0 as none are found

    equ = ["10" "+", "(", "(", "10" , "+", "20", ")", "+", "(", "30", "+", "10", ")", ")"]

    calc_input(equ, len(equ))

main()