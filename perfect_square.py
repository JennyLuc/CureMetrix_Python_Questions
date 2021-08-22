import argparse

parser = argparse.ArgumentParser(description= 'A generator that takes a ' +
                                'number N and returns all perfect squares less'
                                +'than the user input')
parser.add_argument("-n", "--number", type = int,
                    help="the number that the squares would be less than")
parser.parse_args()
args = parser.parse_args()

def perfect_square(N):
    """
    a generator that takes a number N and returns all
    perfect squares less than N.
    :param N: the number that the squares would be less than
    :return: a list of perfect squares under
    """
    if N < 1:
        raise Exception("Sorry, no numbers below 1")
    i = 1
    while i**2 <= N:
        yield i**2
        i += 1

if __name__ == '__main__':
    output = list(perfect_square (args.number))
    print(output)
