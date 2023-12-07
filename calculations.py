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

# test strings
TEST0 = "5+5"
TEST1 = "5+10+5"
TEST2 = "10-5"
TEST3 = "15-5-5"
TEST4 = "20-30"
TEST5 = "10x10"
TEST6 = "n5x10"
TEST7 = "100/10"
TEST8 = ""

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

# calc_input Starts
# Description: calculates the equation from the users input
# Parameters:   equ - List - user inputted equation from calculator buttons
# Returns:      fin_list - List - [fin_result, number of chars left in string]
#               fin_result - the solved equation  ----  number of chars left in string can be checked to ensure all was solved
def calc_input(equ):
    # local variables
    to_insert = []          # empty list to save the new numbers we will use to build the new equation
    sym_count = 0           # variable to count how much a symbol occurs
    n_n_count = 0           # variable to count how much new numbers there are

    # nPEMDAS
    # negatives start
    # only symbol that can be first (except parenthesis, which is special in its own rights) so it has special cases
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
    
    # parenthesis start
        # PROBS GONNA BE THE HARDEST AND MOST OBNOXIOUS SO WE SHALL DO IT LATER
    # parenthesis end

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
    for i in range(len(equ)):
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


def main():                                                                    # [new_num, index_of_num1, index_of num2]

    equ = ["(", "33", "+", "67", ")"]
    to_insert = []
    n_n_count = 0
    sym_count = 0
 
    # testing

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

    print(equ)

main()