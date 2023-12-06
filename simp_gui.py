#######################################################################################################################################
# Title: simp_gui
# Date Started: 12/5/23
# Date Completed: TBD
# Author: Tony Pescatore
# Description: Simple gui that will be used to build the calculators visuals
#######################################################################################################################################

# imports
import PySimpleGUI as sg

# constants
LENGTH = 300
HEIGHT = 700
BUT_SIZE_MODIFIER = .015

# buttons - all buttons will be created below
# ALL BUTTON COLORS, FONT, AND SIZE ARE TBD ALONG WITH THEME PICKER OPTION
# SYMBOLS ÷, ←

# 0 button
zero_but = sg.Button("0", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 1 button
one_but = sg.Button("1", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 2 button
two_but = sg.Button("2", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 3 button
three_but = sg.Button("3", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 4 button
four_but = sg.Button("4", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 5 button
five_but = sg.Button("5", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 6 button
six_but = sg.Button("6", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 7 button
seven_but = sg.Button("7", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 8 button
eight_but = sg.Button("8", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# 9 button
nine_but = sg.Button("9", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# add button
add_but = sg.Button("+", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# sub button
sub_but = sg.Button("-", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# multiply button
mul_but = sg.Button("x", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# divide button
div_but = sg.Button("÷", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# neg button
neg_but = sg.Button("+/-", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# backspace button
back_but = sg.Button("←", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# clear button
clr_but = sg.Button("clr", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# answer button
ans_but = sg.Button("ans", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# exponent button
exp_but = sg.Button("^", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# ( button
l_par_but = sg.Button("(", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# ) button
r_par_but = sg.Button(")", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# deciaml button
dec_but = sg.Button(".", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# themes button
theme_but = sg.Button("Thm", size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))
# equal button
equ_but = sg.Button("=", bind_return_key = True, size = (int(BUT_SIZE_MODIFIER * LENGTH), int(BUT_SIZE_MODIFIER * LENGTH)))    # when enter is pressed, this button will be pressed

# solo layouts

# display layout

# button layout
but_lay = [ [theme_but, ans_but, clr_but, back_but],
            [l_par_but, r_par_but, exp_but, div_but ],
            [seven_but, eight_but, nine_but, mul_but],
            [four_but, five_but, six_but, sub_but],
            [one_but, two_but, three_but, add_but],
            [neg_but, zero_but, dec_but, equ_but]
    ]

disp_lay = [[sg.Button("test")]

    ]

# frames

# display frame
disp_frame = sg.Frame("", disp_lay, size = (LENGTH, HEIGHT - (LENGTH + LENGTH)), element_justification = "Center")
# button frame
but_frame = sg.Frame("", but_lay, size = (LENGTH, (LENGTH + LENGTH)))

# combined layout
full_lay = [[disp_frame],
            [but_frame]
    ]

# window = sg.Window("TEST", full_lay, size = (lENGTH, HEIGHT), use_custom_titlebar = True)

def main():
    window = sg.Window("TEST", full_lay, size = (LENGTH, HEIGHT), use_custom_titlebar = True)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == 'Personal Information':
            # Set layout to personal info layout or create whole new window
            break
        if event == 'Settings':
            # Set layout to settings or create whole new window
            break
        if event == 'Logout':
            # log user out of app
            break

    window.close()
main()
