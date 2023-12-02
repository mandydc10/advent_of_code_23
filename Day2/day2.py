# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

# PART 1
# bag_red = 12
# bag_green = 13
# bag_blue = 14
# sum_of_ids = 0

# with open("games.txt", encoding="UTF-8", mode="r") as file:
#     reader = file.readlines()
    
#     for line in reader:
#         blues = []
#         reds = []
#         greens = []

#         new_line = line.split(":", 1)
#         game_id = int(new_line[0].strip("Game "))
#         game_grabs = new_line[1].split(";")
#         for grab in game_grabs:
#             colours = grab.split(",")
#             # print(colours)
#             for colour in colours:
#                 no_and_colour = colour.strip().split(" ")
#                 print(game_id, no_and_colour)
#                 number = int(no_and_colour[0])
#                 colour = no_and_colour[1]
#                 if colour == "blue":
#                     blues.append(number)
#                 if colour == "red":
#                     reds.append(number)
#                 if colour == "green":
#                     greens.append(number)
#         # print(f"blues: {blues}; reds: {reds}; greens: {greens}")
#         max_blues = max(blues)
#         max_reds = max(reds)
#         max_greens = max(greens)
#         # print(f"max blue {max_blues}; max green {max_greens}; max red {max_reds}")
#         # print(f"blues: 14 {max_blues}, greens: 13 {max_greens}, reds: 12 {max_reds}")

#         if max_blues <= bag_blue and max_greens <= bag_green and max_reds <= bag_red:
#             # print(game_id)
#             sum_of_ids += game_id
#             # print(sum_of_ids)
# print(f"sum is {sum_of_ids}")

# PART 2

sum_of_powers = 0

with open("games.txt", encoding="UTF-8", mode="r") as file:
    reader = file.readlines()
    
    for line in reader:
        blues = []
        reds = []
        greens = []

        new_line = line.split(":", 1)
        game_id = int(new_line[0].strip("Game "))
        game_grabs = new_line[1].split(";")
        for grab in game_grabs:
            colours = grab.split(",")
            # print(colours)
            for colour in colours:
                no_and_colour = colour.strip().split(" ")
                print(game_id, no_and_colour)
                number = int(no_and_colour[0])
                colour = no_and_colour[1]
                if colour == "blue":
                    blues.append(number)
                if colour == "red":
                    reds.append(number)
                if colour == "green":
                    greens.append(number)
        
        max_blues = max(blues)
        max_reds = max(reds)
        max_greens = max(greens)
        # print(f"max blue {max_blues}; max green {max_greens}; max red {max_reds}")
        # print(f"blues: 14 {max_blues}, greens: 13 {max_greens}, reds: 12 {max_reds}")
        game_power = max_blues * max_greens * max_reds
        sum_of_powers += game_power
        
print(f"sum is {sum_of_powers}")