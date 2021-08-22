import argparse

"""
Parse ArgumentParser
"""
# description =

parser = argparse.ArgumentParser(description= 'A function that takes two ' +
                                'integers (x and y) and returns a list of'
                                +'numbers between x and y that are divisible' +
                                'by 5 but not by 7.')
parser.add_argument('-l','--lower_limit', type=int,
                    help='lower limit of the range')
parser.add_argument('-u','--upper_limit', type=int,
                    help='upper limit of the range')
parser.parse_args()
args = parser.parse_args()

def divisible_five_not_seven(x,y):
    """
    A function that takes two integers (x and y) and returns a list of numbers
    between x and y that are divisible by 5 but not by 7.
    :param x: a number where the range would be greater than
    :param y: a number where the range would be less than
    :return: a list of numbers between x and y that are divisible by
    5 but not by 7
    """
    if x > y:
        print ('Exiting... \n' +
        'Floor number needs to be smaller than ceiling number.')
        return None

    output = []
    for i in range(x, y+1):
        # print(i)
        if i%5 == 0:
            if i%7 != 0:
                output.append(i)
    return output

"""
Main Method
"""
if __name__ == '__main__':

    output = divisible_five_not_seven(args.lower_limit,args.upper_limit)
    print(output)
