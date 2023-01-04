from parse_errors import *


def twos_complement(n, bits):
    mask = (1 << bits) - 1
    if n < 0:
        n = ((abs(n) ^ mask) + 1)
    return bin(n & mask)


def register_to_code(register: str):
    register = register.lstrip("$").rstrip(",")
    if register == "sp":
        return 29
    elif register.startswith("s"):
        return 16 + int(register[1])
    elif register.startswith("v"):
        return 2 + int(register[1])
    elif register.startswith("t"):
        return (8 if int(register[1]) < 8 else 16) + int(register[1])
    elif register == "at":
        return 1
    elif register.startswith("a"):
        return 4 + int(register[1])
    elif register.startswith("k"):
        return 26 + int(register[1])
    elif register == "0":
        return 0
    elif register == "gp":
        return 28
    elif register == "fp":
        return 30
    elif register == "ra":
        return 31
    raise UnknownRegisterException


def fill_to(num, length):
    return str(bin(num))[2:].rjust(length, "0")


def string_to_base_alu_operation(rs, rf, rd):
    return fill_to(register_to_code(rs), 5) + \
           fill_to(register_to_code(rf), 5) + \
           fill_to(register_to_code(rd), 5)


OPCODES = {"lw": "100011",
           "sw": "101011",
           "beq": "000100",
           "addi": "001000",
           "andi": "001100",
           "bne": "000101",
           "j": "000010",
           "jal": "000011"}
FUNCTORS = {"add": "100000",
            "sub": "100010",
            "and": "100100",
            "or": "100101",
            "slt": "101010",
            "jr": "001000",
            "jalr": "001001"}

instructions_count = 0
jump_bookmarks = {}


def get_jump_address(value, shift=False):
    if value in jump_bookmarks:
        addr = jump_bookmarks[value]
        if shift:
            addr -= instructions_count + 1
        return addr
    else:
        try:
            return int(value)
        except ValueError:
            raise WrongJumpArgumentException


def write_command(command, file):
    global instructions_count
    opcode = OPCODES.get(command[0], "0" * 6)
    operation = int(opcode, 2)

    if operation == 0:
        if command[0] not in ("jr", "jalr"):
            data = string_to_base_alu_operation(command[2], command[3], command[1]) + \
                   "00000" + FUNCTORS[command[0]]
        elif command[0] == "jalr":
            data = fill_to(register_to_code(command[1]), 5) + "0" * 5 + \
                   fill_to(register_to_code(command[2]), 5) + "0" * 5 + FUNCTORS[command[0]]
        else:
            data = fill_to(register_to_code(command[1]), 5) + \
                   "0" * 15 + FUNCTORS[command[0]]
    elif operation in (35, 43):
        data = fill_to(register_to_code(command[2].split("(")[1][:-1]), 5) + \
               fill_to(register_to_code(command[1]), 5) + \
               twos_complement(int(command[2].split("(")[0]), 16)[2:].rjust(16, "0")
    elif operation in (8, 12, 4, 5):
        imm = int(command[-1]) if operation not in (4, 5) else get_jump_address(command[-1], True)
        data = fill_to(register_to_code(command[2]), 5) + \
               fill_to(register_to_code(command[1]), 5) + \
               twos_complement(imm, 16)[2:].rjust(16, "0")
    elif operation in (2, 3):
        jumping_instruction = get_jump_address(command[1])
        data = str(bin(jumping_instruction))[2:].rjust(26, "0")
    else:
        raise UnknownCommandTypeException

    file.write(f"{opcode}{data}")
    instructions_count += 1


def is_command_jump_bookmark(command):
    return len(command) == 1 and command[0].endswith(":")


def fill_jump_bookmarks(commands):
    commands_count = 0
    for command in commands:
        if is_command_jump_bookmark(command):
            jump_bookmarks[command[0][:-1]] = commands_count
        else:
            commands_count += 1


def process_command(command, file):
    if is_command_jump_bookmark(command):
        return False
    write_command(command, file)
    return True


def read_commands(file):
    e: str
    return list(filter(
        lambda x: len(x),
        [e.split("#")[0].strip().lower().split() for e in file.readlines()]
    ))
