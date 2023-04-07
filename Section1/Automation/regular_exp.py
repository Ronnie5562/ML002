import pyperclip 
import argparse

def main(character, number):
    print(character * number)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='A number')
    parser.add_argument('-C', type=str, help='Character to print', default='#')
    args = parser.parse_args()
    main(args.C, args.number)

    print('______________________________________________________________________________________________________')
    print()
    text = pyperclip.paste()
    print(text) # To print out the test which has been copied to the clipboard
