import argparse

"""
Parse ArgumentParser
"""
parser = argparse.ArgumentParser(description= 'A function that takes two ' +
                                'integers (x and y) and returns a list of'
                                +'numbers between x and y that are divisible' +
                                'by 5 but not by 7.')
parser.add_argument('-n','--number', type=int,
                    help='a decimal number that we want to represent')
parser.add_argument('-b','--base', type=int,
                    help='the base that we want to convert into')
parser.parse_args()
args = parser.parse_args()

def converting_base(x,b):
    """
    a function that takes two integers (x and b) as inputs and returns a
    string that represents the number x in base b
    :param x: a number that we want to represent in a different base
    :param b: a base that we want to convert x into
    :return: a string that represents the number x in base b
    """
    if b <= 1:
        print('Exiting...\nPlease insert a base greater than 1.')
        return None
    output = ""
    exponent = 0
    while b ** exponent < x: #calculating the length
        # print(exponent)
        exponent += 1
    remainder = x
    while remainder != 0:
        quotient = remainder//(b**exponent)
        remainder = remainder%(b**exponent)
        exponent -= 1
        if output == "" and quotient == 0: #removing leading zeroes
            continue
        output += str(quotient)

    while exponent >= 0:
        # print(exponent)
        output+=('0')
        exponent -= 1
    return output
"""
Main Method
"""
if __name__ == '__main__':

    output = converting_base(args.number, args.base)
    print(output)
