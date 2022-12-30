from parser import *
import logging

INPUT_FILE = "commands.txt"
OUTPUT_FILE = "instructions.dat"
CLEAR_OUTPUT_FILE = True

FORMAT = '[%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    try:
        with open(INPUT_FILE, "r") as input_file:
            commands = read_commands(input_file)
    except FileNotFoundError:
        logging.critical("File commands.txt not found. Please add it to currant directory!")
        exit(0)

    with open(OUTPUT_FILE, "w" if CLEAR_OUTPUT_FILE else "a") as output_file:
        for i in range(len(commands)):
            try:
                should_break_line = process_command(commands[i], output_file)
                if i < len(commands) - 1 and should_break_line:
                    output_file.write("\n")
            except ParserException:
                logging.warning(f"Something went wrong during processing command {' '.join(commands[i])}")
    logging.info("Commands was imported")


if __name__ == "__main__":
    main()
 
