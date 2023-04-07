import argparse
import configparser
import sys

# The ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in Microsoft Windows INI files.

def main(number, other_number, output):
    result = number * other_number
    print(f'The result is {result}', file=output)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Multiplies two integers', usage="%(prog)s [OPTIONS]")
    parser.add_argument('-n1', type=int, help='A number', default=1)
    parser.add_argument('-n2', type=int, help='The other number', default=1)
    parser.add_argument('-A', '--Author', help="Author's name", action='store_true')
    parser.add_argument('-C', '--config', type=argparse.FileType('r'), help='Config file')
    parser.add_argument('-O', '--output', type=argparse.FileType('w'), help='output file', default=sys.stdout)

    # NOTE: The argeparse module allows us to define files as parameters, with the argparse.FileType type and opens them automatically.


    #print(parser)
    args = parser.parse_args()
    #print(args)
    if args.Author:
        print("Author's name: Ronald Abimbola")
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])
    main(args.n1, args.n2, args.output)

# run the code with 'python3 prepare_task_step1.py -C config.ini -O result.txt'

