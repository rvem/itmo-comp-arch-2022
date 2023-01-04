import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='MIPS Assembler to bytecode compiler. Supports only limited commands set, which are needed for '
                    'comp-arch HW3 (toy processor). For more information see: '
                    '"https://github.com/rvem/itmo-comp-arch-2022".',
    )
    parser.add_argument('-o', '--output', type=str, dest="output_file", default="instructions.dat",
                        help='output file name')
    parser.add_argument('-a', '--append', dest="append_output_file", default=False, action='store_true',
                        help='flag, showing weather clear output file or not (whether append in the end of file or '
                             'rewrite)')
    parser.add_argument('input_file', nargs='?', type=str, default="commands.asm", help='input file name')

    return parser.parse_args()
