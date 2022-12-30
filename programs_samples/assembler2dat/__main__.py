from parser import *
import console_arguments
import logging

FORMAT = '[%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    args = console_arguments.parse_arguments()

    try:
        with open(args.input_file, "r") as input_file:
            commands = read_commands(input_file)
    except FileNotFoundError:
        logging.critical(f"File {args.input_file} not found. Please add it to current directory!")
        exit(0)

    with open(args.output_file, "a" if args.append_output_file else "w") as output_file:
        fill_jump_bookmarks(commands)
        for i in range(len(commands)):
            try:
                should_break_line = process_command(commands[i], output_file)
                if i < len(commands) - 1 and should_break_line:
                    output_file.write("\n")
            except Exception as e:
                logging.warning(f"Cannot parse \"{' '.join(commands[i])}\" due to: {e}")
    lines = open(args.output_file).readlines()
    lines[-1] = lines[-1].rstrip('\n')
    open(args.output_file, "w").writelines(lines)
    logging.info("Commands was imported")


if __name__ == "__main__":
    main()
