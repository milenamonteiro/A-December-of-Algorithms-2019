def poker_hand(hand):
    FACE_CARDS = {'t': 10, 'j': 11, 'q': 12, 'k': 13, 'a': 14}
    
    def to_number(card):
        if card[0].isnumeric():
            return int(card[0])
        else:
            return FACE_CARDS[card[0]]
    
    hand.sort(key=to_number)
    
    def is_pair(hand):
        """Verifies if the number of two consecutives cards of a hand are equal"""
        return sum(hand[i][0] == hand[i+1][0] for i in range(len(hand)-1)) == 1
    
    def is_two_pair(hand):
        """Checks if the condition of a pair is satisfied twice"""
        if not is_pair(hand):
            for i in range(len(hand)-1):
                if hand[i][0] == hand[i+1][0]:
                    return any(hand[e][0] == hand[e+1][0] and hand[e][0] != hand[i][0] for e in range(i+1, len(hand)))
            return False
        return False
       
    def is_three_of_a_kind(hand):
        """Verifies if the number of three consecutives cards of a hand are equal"""
        return any(hand[i][0] == hand[i+1][0] == hand[i+2][0] for i in range(len(hand)-2))
        
    def is_full_house(hand):
        """True if the hand has a three of a kind and a pair"""
        for i in range(len(hand)-2):
            if hand[i][0] == hand[i+1][0] == hand[i+2][0]:
                return all(hand[e][0] == hand[e+1][0] and hand[e][0] != hand[i][0] for e in range(i, len(hand)-1-i))
        return False
    
    def is_four_of_a_kind(hand):
        """Verifies if the number of four consecutives cards of a hand are equal"""
        return any(hand[i][0] == hand[i+1][0] == hand[i+2][0] == hand[i+3][0]
                   for i in range(len(hand)-3))
    
    def is_flush(hand):
        """True if the suit of all cards are equal to first's"""
        return all(card[1] == hand[0][1] for card in hand)
    
    def is_straight(hand):
        """Verifies if a card is a sequence of another"""
        if hand[-1][0] == "a" and hand[0][0] == "2":
            return list(map(to_number, hand[1:-1])) == list(range(3, len(hand)+1))
        else: 
            return all(to_number(hand[i])+1 == to_number(hand[i+1]) for i in range(len(hand)-1))
    
    def is_straight_flush(hand):
        """True if a hand is straight and a flush"""
        return is_straight(hand) and is_flush(hand)
    
    def is_royal_flush(hand):
        """True if a hand is straight and a flush and has an A"""
        return hand[-1][0] == 'a' and is_straight(hand) and is_flush(hand)
    
    if len(hand) < 5:
        print("invalid")
    elif is_royal_flush(hand):
        print("royal-flush")
    elif is_straight_flush(hand):
        print("straight-flush")
    elif is_full_house(hand):
        print("full-house")
    elif is_straight(hand):
        print("straight")
    elif is_flush(hand):
        print("flush")
    elif is_four_of_a_kind(hand):
        print("four-of-a-kind")
    elif is_three_of_a_kind(hand):
        print("three-of-a-kind")
    elif is_two_pair(hand):
        print("two-pair")
    elif is_pair(hand):
        print("one-pair")
    else:
        print("high-card")

"""
poker_hand(['2h', '2h', '2h', 'kc', 'qd']) three-of-a-kind
poker_hand(['2h', '5h', '7d', '8c', '9s']) high-card
poker_hand(['ah', '2d', '3d', '4c', '5d']) straight
poker_hand(['2h', '3h', '2d', '3c', '3d']) full-house
poker_hand(['2h', '7h', '2d', '3c', '3d']) two-pair
poker_hand(['2h', '7h', '7d', '7c', '7s']) four-of-a-kind
poker_hand(['th', 'jh', 'qh', 'kh', 'ah']) royal-flush
poker_hand(['th', 'jh', 'qh', 'kh', '9h']) straight-flush
poker_hand(['4h', '4h', 'ks', '5d', 'ts']) one-pair
poker_hand(['qc', 'tc', '7c', '6c', '4c']) flush
"""