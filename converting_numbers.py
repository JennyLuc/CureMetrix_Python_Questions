import argparse

def converting_base(x,b):
    """
    a function that takes two integers (x and b) as inputs and returns a
    string that represents the number x in base b
    :param x: a number that we want to represent in a different base
    :param b: a base number that we want to convert x into
    :return: a string that represents the number x in base b
    """
    try:
        x = int(x)
        b = int(b)
    except ValueError:
        print('Exiting... \nPlease input valid integers')

    output = ""
    exponent = 0
    while b ** exponent < x: #calculating the length
        # print(exponent)
        exponent += 1
    remainder = x
    while remainder != 0:

        quotient = remainder//(b**exponent)
        # print('quotient' + str(remainder))
        remainder = remainder%(b**exponent)
        exponent -= 1
        output += str(quotient)

    return output
"""
Main Method
"""
if __name__ == '__main__':
    x = input("Please type in a target number: ")
    y = input("Please type in a base number : ")

    output = converting_base(x,y)
    print(output)


"""
Parse ArgumentParser
"""
parser = argparse.ArgumentParser(description= 'A function that takes two ' +
                                'integers (x and y) and returns a list of'
                                +'numbers between x and y that are divisible' +
                                'by 5 but not by 7.')

parser.parse_args()
