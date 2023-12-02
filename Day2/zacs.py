with open ('games.txt') as file:
    lines = file.readlines()


MAX_RED = [12, 'red']
MAX_GREEN = [13, 'green']
MAX_BLUE = [14, 'blue']


valid_game_ids = []

def get_each_hand_reveal(line):
    game_array = []
    first_split = line.split(':')
    game_id = first_split[0].strip('Game ')
    game_array.append(game_id)
    game_data = first_split[1].strip()
    game_array.append(game_data)
    cubes = game_array[1]
    revealed_cubes = cubes.split(';')
    return revealed_cubes

def each_hand_reveal(array):

    for element in array:
        hand = element.split(', ')
        number = hand[0]
        colour = hand[1]

        return hand



for line in lines:
    red = []
    green = []
    blue = []
    game_array = []
    first_split = line.split(':')
    game_id = int(first_split[0].strip('Game '))
    game_array.append(game_id)
    game_data = first_split[1].strip()
    game_array.append(game_data)
    cubes = game_array[1]
    revealed_cubes = cubes.split(';')
    for element in revealed_cubes:
        hands = element.strip().split(", ")
        for item in hands:
            hand = item.split(" ")
            number= int(hand[0])
            colour = hand[1]
            if colour == MAX_RED[1]:
                red.append(number)
            if colour == MAX_GREEN[1]:
                green.append(number)
            if colour == MAX_BLUE[1]:
                blue.append(number)
    if max(red) > MAX_RED[0] or max(blue) > MAX_BLUE[0] or max(green) > MAX_GREEN[0]:
        pass
    else:
        valid_game_ids.append(game_id)
        print(game_id)
print(sum(valid_game_ids))



        # for reveal in hand:
        #     cube_amount = reveal.strip().split(" ")
        #     if cube_amount[1] == MAX_RED[1] and int(cube_amount[0]) > MAX_RED[0] or cube_amount[1] == MAX_GREEN[1] and int(cube_amount[0]) > MAX_GREEN[0] or cube_amount[1] == MAX_BLUE[1] and int(cube_amount[0]) > MAX_BLUE[0]:
        #         game_id = None
        #         break
        #     else:
        #         valid = game_id











