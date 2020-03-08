# COMP3201
# by Weiming Chen 201504727

# Assignment 5 - LGP program generation structural intron removal

import random


def printLGP(program):
    operators_set = ['+', '-', '*', '/']
    for i in program:
        if type(i[2]) == str or type(i[3]) == str:
            if type(i[2]) == str:
                print('r' + str(i[0]) + "=" + i[2] + operators_set[i[1]] + 'r' + str(i[3]))
            else:
                print('r' + str(i[0]) + "=" + 'r' + str(i[2]) + operators_set[i[1]] + i[3])
        else:
            print('r' + str(i[0]) + "=" + 'r' + str(i[2]) + operators_set[i[1]] + 'r' + str(i[3]))


def main():
    # setting parameters
    max_prog_length = 6  # 6 instructions in total is the upper limit
    n_calculation_reg = 3  # {r0, r1, r2} and r0 is designated as the output register
    n_input_reg = 2  # {r3, r4}
    n_operators = 4  # {+, -, *, /}
    n_constant = 5  # {1, 2, 3, 4, 5}
    constant_rate = 0.4  # An operand can be a constant with a 40% chance, however, both operands cannot be constants at the same time

    ##### 1. randomly generate an LGP program with no more than [max_prog_length] instructions
    # Hint: an instruction can be represented by a list of 4 elements,
    # i.e., its return register, operator, first and second operands
    # an LGP program is thus a list of instructions

    # student code begins

    program = []
    program_len = random.randint(1, max_prog_length)
    # generate the rest of the instructions
    for i in range(program_len):
        if random.random() > constant_rate:
            op1 = random.randint(0, n_calculation_reg - 1)
            op2 = random.randint(0, n_calculation_reg - 1)
        else:
            cons_op = random.randint(1, 2)
            if cons_op == 1:
                op1 = str(random.randint(1, 5))
                op2 = random.randint(0, n_calculation_reg - 1)
            else:
                op1 = random.randint(0, n_calculation_reg - 1)
                op2 = str(random.randint(1, 5))

        io_reg = random.randint(0, n_calculation_reg - 1)
        operator = random.randint(0, n_operators - 1)
        program.append([io_reg, operator, op1, op2, i])

    # student code ends

    ##### 2. print the LGP program as a list of instructions
    # An instruction should be printed as, for instance r1 = r3 + r0 or r2 = r0 * 5

    print("The randomly generated LGP program is:")

    # student code begins
    printLGP(program)

    # student code ends

    ##### 3. remove a program's structural intron
    program_intron_free = []
    effective_registers = ['r0']
    effective_instruction_indices = []

    # student code begins
    program_reverse = program[::-1]
    for i in range(len(program_reverse)):
        if program_reverse[i][0] == 0:
            r0 = program_reverse[i]
            program_intron_free.append(r0)
            effective_instruction_indices.append(r0[4])
            if type(r0[2]) != str: effective_registers.append('r' + str(r0[2]))
            if type(r0[3]) != str: effective_registers.append('r' + str(r0[3]))
            cur_eff = r0
            for j in range(i + 1, len(program_reverse)):
                ins = program_reverse[j]
                if (type(ins[0]) == type(cur_eff[2]) and ins[0] == cur_eff[2]) or (
                        type(ins[0]) == type(cur_eff[3]) and ins[0] == cur_eff[3]):
                    program_intron_free.append(ins)
                    effective_registers.append('r' + str(ins[0]))
                    effective_instruction_indices.append(ins[4])
                    if type(ins[2]) != str: effective_registers.append('r' + str(ins[2]))
                    if type(ins[3]) != str: effective_registers.append('r' + str(ins[3]))
                    cur_eff = ins
            break
    if len(effective_instruction_indices) == 0:
        effective_registers = []
    else:
        effective_registers = set(effective_registers)
        effective_registers = list(effective_registers)
    # student code ends

    ##### 4. print the structual-intron free LGP program

    # print the indices of the effective instructions
    print("The indices of effective instructions are:", effective_instruction_indices)

    # print the LGP program without structural intron
    print("The LGP program withou any structual intron is:")

    # student code begins
    printLGP(program_intron_free)

    # student code ends


# end of main


main()
