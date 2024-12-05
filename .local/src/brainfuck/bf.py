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

src_in = ""
with open(file, "r") as f:
    src_in = f.read()

# strip source
src = ""
for c in src_in:
    if c in "+-><.,[]":
        src += c

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

while pc < len(src):
    ins = src[pc]

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

                pc += 1
                if pc >= len(src) or pc < 0:
                    print("Error: unmatched brackets")
                    exit()
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

                pc -= 1
                if pc >= len(src) or pc < 0:
                    print("Error: unmatched brackets")
                    exit()
        else:
            lvl -= 1

    pc += 1

