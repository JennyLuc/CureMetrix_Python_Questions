import argparse
"""
Parse ArgumentParser
"""
description = ("This file contains a method called rook_distance that takes in"
    + "a list of directions that the rook will travel and returns the distance"
    + "that the rook as travel and distance from the starting point.\n"
    + "Directions can only be: 'up', 'down', 'left', and 'right'."
    + "Directions and steps must match in amount. Ex. "
    + "rook_distance -d up,up,up,up -s 3,3,3,3")
parser = argparse.ArgumentParser(description= description)
parser.add_argument('-d', '--directions',
    help='list of directions seperated by commas',
    type=lambda s: [item for item in s.split(',')])
parser.add_argument('-s','--steps', help='list of steps seperated by commas',
    type=lambda s: [int(item) for item in s.split(',')])

args = parser.parse_args()

def rook_distance(directions,steps):
    """
    A function that takes in a list of tuples. The tuples are the direction
    and spaces that the rook will travel.
    :param directions: a list of tuples that represent the direction and
    distance the rook will travel.
    :return: a tuple where the first value is the distance traveled and the
    second value is the distance from the starting point
    """

    if len(directions) != len(steps):
        print('Number of directions and number of steps must match.')
        return None
    longitude = 0
    latitude = 0
    steps_taken = 0
    direction_dict = ['up', 'down', 'left', 'right']

    #iterate through the list of directions
    for direction, step in zip(directions,steps):
        if direction not in direction_dict:
            print ('Exiting...\nPlease insert the correct directions')
            return None
        steps_taken += step
        if direction == 'up':
            longitude += step
        elif direction == 'down':
            longitude -= step
        elif direction == 'left':
            latitude -= step
        else:
            latitude += step
    from_starting_point = abs(latitude) + abs(longitude)
    return (steps_taken, from_starting_point)

"""
Main Method
"""
if __name__ == '__main__':
    # print(arg.steps)
    output = rook_distance(args.directions, args.steps)
    print(output)
