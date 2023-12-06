#######################################################################################################################################
# Title: calculations
# Author: Tony Pescatore
# Description: This will hold all the functions to do all the calculations done
#######################################################################################################################################

# imports
import symbols

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

# plus Starts
# Description: adds the two numbers together
# Parameters:   num1 - int - number to be added
#               num2 - int - number to be added
# Returns:      answer - int - added numbers
def plus(num1, num2):
    ans = num1 + num2
    return ans

# minus Starts
# Description: subtracts the two numbers
# Parameters:   num1 - int - starting number
#               num2 - int - number to be subtracted
# Returns:      answer - int - subtracted numbers
def minus(num1, num2):
    ans = num1 - num2
    return ans

# plus Starts
# Description: adds the two numbers together
# Parameters:   num1 - int - number to be added
#               num2 - int - number to be added
# Returns:      answer - int - product
def multiply(num1, num2):
    ans = num1 * num2
    return ans

# divide Starts
# Description: subtracts the two numbers
# Parameters:   num1 - int - starting number
#               num2 - int - number to do division
# Returns:      answer - int - quotient
def divide(num1, num2):
    ans = num1 / num2
    return ans

# calc_input Starts
# Description: calculates the equation from the users input
# Parameters:   equ - String - user inputted equation from calculator buttons
# Returns:      fin_list - List - [fin_result, number of chars left in string]
#               fin_result - the solved equation  ----  number of chars left in string can be checked to ensure all was solved
def calc_input(equ):
    # local variables
    wait_for_r_par = False      # states if we are waiting for ")"
    par_result = []             # empty list used if there are any parenthesis in the equation
    par_equation = ""           # empty string that will store the equation in the parenthesis, used for recursion
    fin_result = 0              # final result
    equ_len = len(equ)          # variable with length of the equation
    syms = []                   # empty list that will hold the symbols in order.  We use this to do the math on the nums in numbers[]
    numbers = []                # numbers in the order they appear in the string
    temp_num = ""               # temp string that is used to store numbers bigger than 1 characters

    # iterating over string
    for c in equ:               # for every character in the equation
        
        if (c != symbols.ADD and c != symbols.SUB and c != symbols.MUL and c != symbols.DIV and c != symbols.NEG and c != symbols.EXP and c != symbols.L_PAR and c != symbols.R_PAR and c != symbols.EQU):       # checks for any symbols in equation
            # not a symbol
            temp_num += c
        else:                                   # only if c is a symbol
            numbers.append(int(temp_num))       # number has been formed and added to number[]
            temp_num = ""                       # temp_num reset after it has been appended to numbers list
            # NEEDS ERROR CHECKING FOR ALL ERRORS LISTED IN NOTEPAD++
            if c != "=":                        # checks if the symbol is not "=", which acts and a terminator for the equation
                syms.append(c)                  # if it is not the terminator then add it to symbol list
            else:                               # if it is the string terminator, it ends the for loop as the whole string should have been read
                break
    
    # for loop ends
    for i in range(len(syms)):              # iterates over all of the symbols in the equation
        
        if syms[i] == symbols.ADD:    # if the symbol is "+"
            fin_result += plus(int(numbers[i]), int(numbers[i + 1]))
            # replace the second number with the new number, so that old numbers are not repeated in the equation
            numbers.pop(i)
            numbers.insert(i + 1, fin_result)

        if syms[i] == symbols.SUB:    # if the symbol is "+"
            fin_result += minus(int(numbers[i]), int(numbers[i + 1]))
            # replace the second number with the new number, so that old numbers are not repeated in the equation
            numbers.pop(i)
            numbers.insert(i + 1, fin_result)


    return fin_result




def main():
    # temp = int("5")
    # temp2 = int("10")
    # sym_ls = ["+"]

    # if sym_ls[0] == "+":
    #   temp3tot = plus(temp, temp2)

    # print(temp3tot)

    print(calc_input("5+10+15="))
    print(calc_input("20-10="))
    print(calc_input("40+10+50="))

main()