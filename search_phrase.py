import argparse
from os.path import exists
import re
"""
Parse ArgumentParser
"""

parser = argparse.ArgumentParser(description= 'Write a function that takes a ' +
                                'phrase and a text file as inputs. '
                                +'and returns True if the phrase is found' +
                                'in the text file, and False if not found.')
parser.add_argument('-f','--file', type=str,
                    help='directory of text file to search through')
parser.add_argument('-p','--phrase', type=str,
                    help='target phrase to search for')
parser.parse_args()
args = parser.parse_args()

def search_phrase_in_file(text_file,phrase):
    """
    A function that takes in a file and a target phrase and searches in the
    text file if the phrase exists in the file.
    :param text_file: a text file to search through
    :param phrase: a phrase to search for in the text file
    :return: True if phrase is found, and False if phrase is not found
    """
    if not exists(text_file):
        print ('Exiting...\n Please pass in an existing text file.')
        return None

    target = r'^' + phrase + '\s'
    with open(text_file) as file:
        for line in file:
            if re.search(target, line, re.I): #ignore cases
                return True
    return False

"""
Main Method
"""
if __name__ == '__main__':

    output = search_phrase_in_file(args.file,args.phrase)
    print(output)
