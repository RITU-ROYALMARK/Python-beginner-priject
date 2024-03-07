'''' ALICE HAS SOME CARD EACH CARDS HAS A NUMBER AND NUMBER ARE DECENDING ORDER AND THE CARDS ARE LAYERED FACE DOWN, SO
ALICE SAYS BOB TO PICK OUT A GIVE NUMBER IN THE CARD.
WRITE A FUNCTION TO HELP BOB PICK UP THE CARD WITH THE GIVEN NUMBER

'''

def find_card(cards,query):
    position = 0

    while position < len(cards):
        if cards[position] == query:# FNIDING IF THE THE CARDS MATCH THE GIVEN NUMBER
            return position+1

        position += 1# INCREMENT THE POSITOIN TO PICK EACH CARD

    return -1

cards = [13,11,10,7,4,3,1,0] # THE CARDS
query = 7 # THE GIVEN NUMBER
print(find_card(cards,query))

