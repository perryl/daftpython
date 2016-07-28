#!/usr/bin/python3
import argparse

def reverse(string):
    char_array = list(string) # e.g. ['H', 'e', 'l', 'l', 'o']
    string_length = len(char_array) # e.g. 5
    new_string = []
    while string_length > 0:
        string_length -= 1
        new_string.append(char_array[string_length])
    return ''.join(new_string)

def main():
    parser = argparse.ArgumentParser(description='Reverses contents of a '
                                                 'given string.')
    parser.add_argument('--string', type=str, help='String to be reversed.')
    args = parser.parse_args()
    s = args.string
    rev_str = reverse(s)
    print (rev_str)

if __name__ == "__main__":
    main()
