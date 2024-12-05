"""
A Brainfuck interpreter by me :)
- TM365
"""

import sys
import os.path

if len(sys.argv) < 2:
    print("Brainfuck file required as an argument.")
    exit()

file = sys.argv[1]

if not os.path.isfile(file):
    print(f"{file} is not a file.")
    exit()

src = ""
with open(file, "r") as f:
    src = f.read()

# check for unmatched brackets
bracket_lvl = 0
for c in src:
    if c == "[":
        bracket_lvl += 1
    elif c == "]":
        bracket_lvl -= 1

if bracket_lvl != 0:
    print("Error: unmatched brackets")
    exit()

TAPE_SIZE = 1024
tape = [0] * TAPE_SIZE
tp = 0
pc = 0
lvl = 0
input_buffer = ""

line = 1
char = 1
cmd = ""
next = 0
jmp = 0
while pc < len(src):
    ins = src[pc]

    if ins not in "+-><.,[]":
        pc += 1
        char += 1
        if src[pc] == "\n":
            line += 1
            char = 0
        continue

    if lvl == jmp and ins == "]" and tape[tp] == 0:
        jmp = 0

    if next == 0 and jmp == 0:
        cmd = input(f"{line},{char} {ins}? ")
        if cmd == "n":
            next = 1
        elif len(cmd) > 0 and cmd[0] == "n":
            try:
                next = int(cmd[1:])
            except ValueError:
                print("Error: expected number after 'n'")
        elif cmd == "exit":
            exit()
        elif cmd == ".":
            byte = tape[tp]
            pch = repr(chr(byte))
            print(f"{tp}: {byte:>3} {pch}")
        elif len(cmd) > 0 and cmd[0] == ".":
            try:
                ptp = int(cmd[1:]) % TAPE_SIZE
                byte = tape[ptp]
                pch = repr(chr(byte))
                print(f"{ptp}: {byte:>3} {pch}")
            except ValueError:
                print("Error: expected number after '.'")
        elif cmd == "lvl":
            print(f"lvl: {lvl}")
        elif cmd == "l":
            lc = pc
            while lc >= 0 and src[lc] != "\n":
                lc -= 1
            lc += 1
            while lc < len(src) and src[lc] != "\n":
                print(src[lc], end="")
                lc += 1
            print()
        elif cmd == "]" and lvl > 0:
            jmp = lvl
        elif cmd == "c":
            next = -1
        elif cmd == "help" or cmd == "h":
            print("""
=== Help
n       next instruction
n<N>    conitnue for <N> instructions
c       conitnue until end
.       print tape data at current location
.<N>    print tape data at location <N>
]       continue to untill current loop exits
l       print line
lvl     print jmp lvl
exit    exit debugger
h
help    print this message
""")
        continue

    if next != 0:
        next -= 1

    if ins == "+":
        tape[tp] = (tape[tp] + 1) % 256
    elif ins == "-":
        tape[tp] = (tape[tp] - 1) % 256
    elif ins == ">":
        tp = (tp + 1) % TAPE_SIZE
    elif ins == "<":
        tp = (tp - 1) % TAPE_SIZE
    elif ins == ".":
        print(chr(tape[tp]), end="")
    elif ins == ",":
        if not input_buffer:
            input_buffer = input() + "\n"
        byte = ord(input_buffer[0])
        input_buffer = input_buffer[1:]
        tape[tp] = byte
    elif ins == "[":
        if tape[tp] == 0:
            # jump after a matching ]
            jl = lvl
            pc += 1
            while not (src[pc] == "]" and lvl == jl):
                if src[pc] == "[":
                    lvl += 1
                elif src[pc] == "]":
                    lvl -= 1

                char += 1
                if src[pc] == "\n":
                    line += 1
                    char = 0

                pc += 1
                if pc >= len(src) or pc < 0:
                    print("Error: unmatched brackets")
                    exit()
            char += 1
            if src[pc] == "\n":
                line += 1
                char = 0
        else:
            lvl += 1
    elif ins == "]":
        if tape[tp] != 0:
            # jump after a matching [
            jl = lvl
            pc -= 1
            while not (src[pc] == "[" and lvl == jl):
                if src[pc] == "]":
                    lvl += 1
                elif src[pc] == "[":
                    lvl -= 1

                char -= 1
                if src[pc] == "\n":
                    line -= 1
                    char = 0

                pc -= 1
                if pc >= len(src) or pc < 0:
                    print("Error: unmatched brackets")
                    exit()
            char -= 1
            if src[pc] == "\n":
                line -= 1
                char = 0
        else:
            lvl -= 1

    pc += 1

    char += 1
    if src[pc] == "\n":
        line += 1
        char = 0

