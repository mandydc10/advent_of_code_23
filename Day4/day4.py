array_of_cards = []

class Card:
    def __init__(self,card_number,winning_numbers,user_numbers,points):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.user_numbers = user_numbers
        self.points = points

    def __repr__(self):
        return ({self.card_number}, {self.winning_numbers}, {self.user_numbers}, {self.points})


with open("input.txt", encoding="UTF-8", mode="r") as file:
    reader = file.readlines()

    for line in reader:
        winning_numbers = []
        strip_line = line.strip("Card ")
        line_split = strip_line.split(":",1)
        card = line_split[0]
        both_number_groups = line_split[1].split("|",1)
        first_number_group = both_number_groups[0].split()
        for number in first_number_group:
            number = int(number)
            winning_numbers.append(number)
        user_numbers = both_number_groups[1].split()
        card = Card(card,winning_numbers,user_numbers,0)
        array_of_cards.append(card)
        # print(winning_numbers)
    

print(repr(array_of_cards))
