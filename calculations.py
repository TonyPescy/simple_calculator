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
    # new_equ_n = ""              # new equation string to be made after negatives have been changed
    # new_equ_p = ""              # new equation string to be made after negatives have been changed
    # new_equ_md = ""             # new equation string to be made after multiplication and division have been changed
    # new_equ_as = ""             # new equation string to be made after negatives have been changed

    # wait_for_r_par = False      # states if we are waiting for ")"
    # par_result = []             # empty list used if there are any parenthesis in the equation
    # par_equation = ""           # empty string that will store the equation in the parenthesis, used for recursion
    # fin_result = 0              # final result
    # syms = []                   # empty list that will hold the symbols in order.  We use this to do the math on the nums in numbers[]
    # numbers = []                # numbers in the order they appear in the string
    # temp_num = ""               # temp string that is used to store numbers bigger than 1 characters

    # TEMPORARY REMOVAL
    # iterating over string
    # for c in equ:               # for every character in the equation
        
    #     if (c != symbols.ADD and c != symbols.SUB and c != symbols.MUL and c != symbols.DIV and c != symbols.NEG and c != symbols.EXP and c != symbols.L_PAR and c != symbols.R_PAR and c != symbols.EQU):       # checks for any symbols in equation
    #         # not a symbol
    #         temp_num += c
    #     else:                                   # only if c is a symbol
    #         numbers.append(int(temp_num))       # number has been formed and added to number[]
    #         temp_num = ""                       # temp_num reset after it has been appended to numbers list
    #         # NEEDS ERROR CHECKING FOR ALL ERRORS LISTED IN NOTEPAD++
    #         if c != "=":                        # checks if the symbol is not "=", which acts and a terminator for the equation
    #             syms.append(c)                  # if it is not the terminator then add it to symbol list
    #         else:                               # if it is the string terminator, it ends the for loop as the whole string should have been read
    #             break
    
    # # for loop ends
    # for i in range(len(syms)):              # iterates over all of the symbols in the equation
        
    #     # addition
    #     if syms[i] == symbols.ADD:      # if the symbol is "+"
    #         if i == 0:                  # if it is the first pair of numbers
    #             fin_result += plus(int(numbers[i]), int(numbers[i + 1]))
    #         else:
    #             fin_result = plus(fin_result, int(numbers[i + 1]))
    #     # subtraction
    #     if syms[i] == symbols.SUB:      # if the symbol is "-"
    #         if i == 0:                  # if it is the first pair of numbers
    #             fin_result += minus(int(numbers[i]), int(numbers[i + 1]))
    #         else:
    #             fin_result = minus(fin_result, int(numbers[i + 1]))

    #     # multiplication
    #     if syms[i] == symbols.MUL:      # if the symbol is "x"
    #         if i == 0:                  # if it is the first pair of numbers
    #             fin_result += multiply(int(numbers[i]), int(numbers[i + 1]))
    #         else:
    #             fin_result = multiply(fin_result, int(numbers[i + 1]))
    #     # division
    #     if syms[i] == symbols.DIV:      # if the symbol is "÷"
    #         if i == 0:                  # if it is the first pair of numbers
    #                 if (int(numbers[i + 1]) != 0):      # checks for divide by zero error
    #                     fin_result += divide(int(numbers[i]), int(numbers[i + 1]))
    #                 else:
    #                     print("divide by zero error goes here")
    #                     break
    #         else:
    #             if (int(numbers[i + 1]) != 0):
    #                 fin_result = divide(fin_result, int(numbers[i + 1]))
    #             else:
    #                 print("divide by zero error goes here")
    #                 break
        
    #     # exponents
    #     if syms[i] == symbols.EXP:      # if the symbol is "^"
    #         if i == 0:                  # if it is the first pair of numbers
    #             fin_result += exponent(int(numbers[i]), int(numbers[i + 1]))
    #         else:
    #             fin_result = exponent(fin_result, int(numbers[i + 1]))

    # return fin_result

    # local variables
    to_insert = []          # empty list to save the new numbers we will use to build the new equation [new_num, insert_num, old_num]

    # nPEMDAS
    # negatives start
    # only symbol that can be first (except parenthesis, which is special in its own rights) so it has special cases
    for i in range(len(equ)):
        if equ[i] == symbols.NEG:                                               # checks for negative in the equation
            new_num = inverse(equ[i + INCREMENT])
            to_insert.append([new_num, i + DBL_INCREMENT, equ[i + INCREMENT]])  # increments take in account for insert of new_num
    
    for i in range(len(to_insert)):                                             # if there are multiple negative numbers in to_insert it will interate over all of them
        equ.insert(to_insert[i][INCREMENT], to_insert[i][FIRST_ELEMENT])
        # removes all symbols and numbers involved
        equ.remove(symbols.NEG)
        equ.remove(to_insert[i][inverse(INCREMENT)])
    
    to_insert = []                                                              # to_insert list reset
    # negatives end
    
    # parenthesis start
        # PROBS GONNA BE THE HARDEST AND MOST OBNOXIOUS SO WE SHALL DO IT LATER
    # parenthesis end

    # exponents start
    for i in range(len(equ)):
        if equ[i] == symbols.EXP:                                               # checks for negative in the equation
            new_num = exponent(equ[i - INCREMENT], equ[i + INCREMENT])
            to_insert.append([new_num, i + DBL_INCREMENT, equ[i + INCREMENT]])  # increments take in account for insert of new_num
    
    for i in range(len(to_insert)):                                             # if there are multiple negative numbers in to_insert it will interate over all of them
        equ.insert(to_insert[i][INCREMENT], to_insert[i][FIRST_ELEMENT])
        # removes all symbols and numbers involved
        equ.remove(symbols.EXP)
        equ.remove(to_insert[i][inverse(INCREMENT)])
    
    to_insert = []                                                              # to_insert list reset
    # exponents end




def main():                                                                    # [new_num, insert_num, old_num]

    equ = ["2", "^", "2", "3", "^", "3"]
    to_insert = []
 
    # testing
    for i in range(len(equ)):
        if equ[i] == symbols.EXP:                                               # checks for negative in the equation
            new_num = exponent(equ[i - INCREMENT], equ[i + INCREMENT])
            to_insert.append([new_num, i - INCREMENT, i + INCREMENT])  # increments take in account for insert of new_num
    
    for i in range(len(to_insert)):                                             # if there are multiple negative numbers in to_insert it will interate over all of them
        equ.insert(to_insert[i][INCREMENT], to_insert[i][FIRST_ELEMENT])
        # removes all symbols and numbers involved
        equ.remove(symbols.EXP)
        equ.remove(to_insert[i][inverse(INCREMENT)])

main()