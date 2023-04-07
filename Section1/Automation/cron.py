import argparse
import sys
from datetime import datetime
import configparser


def main(number, other_number, output):
    result = number * other_number
    print(f'[{datetime.utcnow().isoformat()}] The result is {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-C', '--config', type=argparse.FileType('r'), help='config file', default='/etc/automate.ini')
    parser.add_argument('-O', dest='output', type=argparse.FileType('a'), help='output file', default=sys.stdout)

    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])

    main(args.n1, args.n2, args.output)

# The {formatter_class=argparse.ArgumentDefaultsHelpFormatter} parameter automatically adds information about default values when printing the 
# help using the -b argument.

# run the code with 'python3 cron.py -C config.ini -O result.txt'
# if you need to obtain boolean values, do not use bool(string) because it will return true irrespective of the string. Use config.get_boolean
# (string) instead.