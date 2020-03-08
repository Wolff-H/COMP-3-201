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

    # random the number of instructions of this program #
    instruction_nums = random.randint(1, max_prog_length)
    # generate the rest of the instructions
    for i in range(instruction_nums):
        if random.random() < constant_rate:
            constant = random.randint(0, n_constant-1)
            if random.random() < 0.5:
                operand1 = constant
                operand2 = "r"+str(random.randint(0, n_calculation_reg + n_input_reg - 1))
            else:
                operand1 = "r"+str(random.randint(0, n_calculation_reg + n_input_reg - 1))
                operand2 = constant
        else:
            operand1 = "r"+str(random.randint(0, n_calculation_reg + n_input_reg - 1))
            operand2 = "r"+str(random.randint(0, n_calculation_reg + n_input_reg - 1))

        register = "r"+str(random.randint(0, n_calculation_reg-1))
        operator = random.randint(0, n_operators-1)

        program.append([i, register, operator, operand1, operand2])


    # student code ends



    ##### 2. print the LGP program as a list of instructions
        # An instruction should be printed as, for instance r1 = r3 + r0 or r2 = r0 * 5

    print("The randomly generated LGP program is:")

    # student code begins
    operators = ['+', '-', '*', '/']
    for instruction in program:
       print(   instruction[1], "=", instruction[3], operators[ instruction[2] ], instruction[4]   )



    # student code ends



    ##### 3. remove a program's structural intron
    program_intron_free = []
    effective_registers = ['r0']
    effective_instruction_indices = []

    # student code begins

    trace = program[::-1]

    # all calculation registers #
    registers = []
    for k in range(n_calculation_reg):
        registers.append("r"+str(k))

    # workflow #
    for i in range( len(trace) ):
        if trace[i][1] == "r0":    # find the first appeared r0 (the most outlet one)
            r0 = trace[i]
            effective_instruction_indices.append(trace[i][0])
            program_intron_free.append(r0)

            if r0[3] in registers:
                effective_registers.append(r0[3])
            if r0[4] in registers:
                effective_registers.append(r0[4])

            for j in range( i+1, len(trace) ):
                newest = program_intron_free[len(program_intron_free)-1]
                instruction = trace[j]
                if instruction[1] in registers and ( instruction[1] == newest[3] or instruction[1] == newest[4] ):
                    effective_registers.append(instruction[1])
                    program_intron_free.append(instruction)
                    effective_instruction_indices.append(instruction[0])
                    effective_registers.append(newest[3])
                    effective_registers.append(newest[4])
            break




    # student code ends



    ##### 4. print the structual-intron free LGP program

    # print the indices of the effective instructions
    print("The indices of effective instructions are:", effective_instruction_indices)

    # print the LGP program without structural intron
    print("The LGP program without any structual intron is:")

    # student code begins
    for instruction in program_intron_free:
       print(   instruction[1], "=", instruction[3], operators[ instruction[2] ], instruction[4]   )



    # student code ends


# end of main


main()
