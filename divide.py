# import argparse



def divisibe_five_not_seven(x,y):
    """
    A function that takes two integers (x and y) and returns a list of numbers
    between x and y that are divisible by 5 but not by 7.
    :param x: a number where the range would be greater than
    :param y: a number where the range would be less than
    :return: a list of numbers between x and y that are divisible by
    5 but not by 7
    """
    try:
        x = int(x)
        y = int(y)

    except ValueError:
        print('Exiting... \nPlease input valid integers')
    if x > y:
        return ('Exiting... \n' +
        'Floor number needs to be smaller than ceiling number.')

    output = []
    for i in range(x, y+1):
        print(i)
        if i%5 == 0:
            if i%7 != 0:
                output.append(i)
    return output

"""
Main Method
"""
if __name__ == '__main__':

    x = input("Please type in a number for the bottom range: ")
    y = input("Please type in a number for the top range: ")

    output = divisibe_five_not_seven(x,y)
    print(output)


"""
Parse ArgumentParser
"""
# # description =
# parser = argparse.ArgumentParser(description= 'A function that takes two integers (x and y) and returns a'
# + 'list of numbers between x and y that are divisible by 5 but not by 7.\n '+
# + 'Using with input method: python divide.py\n')
# # + 'Using the method directly: pythong divide.py [x param] [y param]')
#
# # parser = argparse.ArgumentParser(description= 'A function that takes two ' +
# #                                 'integers (x and y) and returns a list of'
# #                                 +'numbers between x and y that are divisible' +
# #                                 'by 5 but not by 7.')
# parser.parse_args()
