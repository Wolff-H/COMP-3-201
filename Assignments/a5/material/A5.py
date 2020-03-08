# COMP3201
# by Ting Hu

# Assignment 5 - LGP program generation structural intron removal

import random

def main():

    # setting parameters
    max_prog_length = 6     # 6 instructions in total is the upper limit
    n_calculation_reg = 3   # {r0, r1, r2} and r0 is designated as the output register
    n_input_reg = 2         # {r3, r4}
    n_operators = 4         # {+, -, *, /}
    n_constant = 5          # {1, 2, 3, 4, 5}
    constant_rate = 0.4     # An operand can be a constant with a 40% chance, however, both operands cannot be constants at the same time


    ##### 1. randomly generate an LGP program with no more than [max_prog_length] instructions
        # Hint: an instruction can be represented by a list of 4 elements,
        # i.e., its return register, operator, first and second operands
        # an LGP program is thus a list of instructions

    program = []

    # student code begins



    # student code ends



    ##### 2. print the LGP program as a list of instructions
        # An instruction should be printed as, for instance r1 = r3 + r0 or r2 = r0 * 5

    print("The randomly generated LGP program is:")

    # student code begins




    # student code ends



    ##### 3. remove a program's structural intron
    program_intron_free = []
    effective_registers = ['r0']
    effective_instruction_indices = []

    # student code begins




    # student code ends



    ##### 4. print the structual-intron free LGP program

    # print the indices of the effective instructions
    print("The indices of effective instructions are:", effective_instruction_indices)

    # print the LGP program without structural intron
    print("The LGP program withou any structual intron is:")

    # student code begins




    # student code ends


# end of main


main()
