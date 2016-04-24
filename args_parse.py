#!/usr/local/bin/python3.4

'''
source: https://pymotw.com/2/argparse/
'''

def add(sequence):
    return sum(sequence)

def mul(sequence):
    result = 1
    for i in sequence:
        result = result * i
    return result

if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser()
    parse.add_argument('-a', '--add', nargs='+', dest='add',
                       default=[], type=int, help='will add the numbers passed')
    parse.add_argument('--mul', nargs='+', dest='mul',
                       default=[], type=int, help='will mul the numbers passed')
    args = parse.parse_args()
    dictionary = {
        'add': add,
        'mul': mul
    }
    for key in dictionary.keys():
        if getattr(args, key):
            print(dictionary[key](getattr(args, key)))
