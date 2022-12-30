import logging


FORMAT = '[%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def twos_complement(n, bits):
    mask = (1 << bits) - 1
    if n < 0:
        n = ((abs(n) ^ mask) + 1)
    return bin(n & mask)


def register_to_code(register: str):
    register = register.lstrip("$").rstrip(",")
    if register.startswith("s"):
        return 16 + int(register[1])
    elif register.startswith("v"):
        return 2 + int(register[1])
    elif register.startswith("t"):
        return (8 if int(register[1]) < 8 else 16) + int(register[1])
    elif register.startswith("a"):
        return 4 + int(register[1])
    elif register.startswith("k"):
        return 26 + int(register[1])
    elif register == "0":
        return 0
    elif register == "ra":
        return 31
    raise ValueError


def fill_to(chisl, lenght):
    return str(bin(chisl))[2:].rjust(lenght, "0")


def string_to_base_alu_operation(rs, rf, rd):
    return fill_to(register_to_code(rs), 5) + \
           fill_to(register_to_code(rf), 5) + \
           fill_to(register_to_code(rd), 5)


opcodes = {"lw": "100011",
           "sw": "101011",
           "beq": "000100",
           "addi": "001000",
           "andi": "001100",
           "bne": "000101",
           "j": "000010",
           "jal": "000011"}

functs = {"add": "100000",
          "sub": "100010",
          "and": "100100",
          "or": "100101",
          "slt": "101010",
          "jr": "001000"}


with open("commands.txt") as file:
    commands = list(filter(lambda x: len(x), [e.strip().lower().split() for e in file.readlines()]))


# Если не хотите чистить файл instructions.dat - удалите строки 68-69
with open("instructions.dat", "w"):
    pass
for i in range(len(commands)):
    command = commands[i]
    try:
        opcode = opcodes.get(command[0], "0" * 6)
        operation = int(opcode, 2)
        if operation == 0:
            if command[0] != "jr":
                data = string_to_base_alu_operation(command[2], command[3], command[1]) + \
                       "00000" + functs[command[0]]
            else:
                data = fill_to(register_to_code(command[1]), 5) + \
                       "0" * 15 + functs[command[0]]
        elif operation in (35, 43):
            data = fill_to(register_to_code(command[2].split("(")[1][:-1]), 5) +\
                   fill_to(register_to_code(command[1]), 5) +\
                   twos_complement(int(command[2].split("(")[0]), 16)[2:].rjust(16, "0")
        elif operation in (8, 12, 5, 4):
            data = fill_to(register_to_code(command[2]), 5) + \
                   fill_to(register_to_code(command[1]), 5) + \
                   twos_complement(int(command[-1]), 16)[2:].rjust(16, "0")
        elif operation in (2, 3):
            data = str(bin(int(command[1])))[2:].rjust(26, "0")
        else:
            raise ValueError
        with open("instructions.dat", "a") as file:
            file.write(f"{opcode}{data}" + ("\n" if i < len(commands) - 1 else ""))
    except Exception:
        logging.warning(f"Something went wrong during processing command {' '.join(command)}")
logging.info("Commands was imported")
