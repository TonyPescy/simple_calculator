#######################################################################################################################################
# Title: simp_gui
# Date Started: 12/5/23
# Date Completed: TBD
# Author: Tony Pescatore
# Description: Simple gui that will be used to build the calculators visuals
#######################################################################################################################################

# imports
import PySimpleGUI as sg

# buttons - all buttons will be created below
# ALL BUTTON COLORS, FONT, AND SIZE ARE TBD ALONG WITH THEME PICKER OPTION
# SYMBOLS ÷, ←

# 0 button
zero_but = sg.Button("0")
# 1 button
one_but = sg.Button("1")
# 2 button
two_but = sg.Button("2")
# 3 button
three_but = sg.Button("3")
# 4 button
four_but = sg.Button("4")
# 5 button
five_but = sg.Button("5")
# 6 button
six_but = sg.Button("6")
# 7 button
seven_but = sg.Button("7")
# 8 button
eight_but = sg.Button("8")
# 9 button
nine_but = sg.Button("9")
# add button
add_but = sg.Button("+")
# sub button
sub_but = sg.Button("-")
# multiply button
mul_but = sg.Button("x")
# divide button
div_but = sg.Button("÷")
# neg button
neg_but = sg.Button("+/-")
# backspace button
back_but = sg.Button("←")
# clear button
clr_but = sg.Button("clr")
# answer button
ans_but = sg.Button("ans")
# exponent button
exp_but = sg.Button("^")
# ( button
l_par_but = sg.Button("(")
# ) button
r_par_but = sg.Button(")")
# deciaml button
dec_but = sg.Button(".")
# themes button
theme_but = sg.Button("Thm")
# equal button
equ_but = sg.Button("=", bind_return_key = True)    # when enter is pressed, this button will be pressed

