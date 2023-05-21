def poker_hand(cards):
    if len(cards) == 5:
        if check_royal(cards) and check_flush(cards): #Royal Flush -> A, K, Q, J e 10, todos do mesmo naipe
            return "Royal Flush"
        
        if check_straight(cards) and check_flush(cards): #Straight Flush -> Cinco cartas seguidas, todas do mesmo naipe
            return "Straight Flush"
        
        if check_poker(cards): #Poker -> Quatro cartas com o mesmo valor
            return "Poker"
        
        if check_trio(cards) and check_pair(cards): #Full House -> Um trio e um par
            return "Full House"
        
        if check_flush(cards): #Flush -> Quaisquer 5 cartas do mesmo naipe, sem ser em sequência
            return "Flush"

        if check_straight(cards): #Sequência -> Sequência de 5 cartas que não sejam todas do mesmo naipe
            return "Sequência"
        
        if check_trio(cards): #Trio -> 3 cartas com o mesmo valor
            return "Trio"
        
        if check_two_pairs(cards): #Dois Pares ->  Dois pares diferentes na mesma jogada
            return "Dois Pares"
        
        if check_pair(cards): #Par -> Dois cartas do mesmo valor
            return "Par"
        
        return "Carta Alta" #Carta Alta -> Nenhuma das combinações anteriores
    else:
        print("Necessitas de ter 5 cartas!")
        
def check_royal(cards):
    royal_values = ["A", "K", "Q", "J", "10"]
    royal = False
    
    for card in cards:
        if card[:-1] in royal_values:
            royal = True
        else:
            royal = False
    
    return royal

def check_flush(cards):
    suits = []
    flush = False
    
    for card in cards:
        suits.append(card[-1])

    if len(set(suits)) == 1:
        flush = True
    
    return flush

def check_straight(cards):
    values = []
    cards_values = {"J":11, "Q":12, "K":13, "A":14}
    sequence = False
    
    for i in range(0, len(cards)):
        if cards[i][0] in cards_values:
            cards[i] = f"{cards_values[cards[i][0]]}{cards[i][-1]}"
    
    for card in cards:
        values.append(int(card[:-1]))
      
    if sorted(values) == list(range(min(values), max(values) + 1)):
        sequence = True
    
    return sequence

def check_poker(cards): 
    counter = {}
    poker = False 
    
    for card in cards:
        card_number = card[:-1]
        try:
            if counter[card_number]:
                counter[card_number] += 1
            else:
                counter[card_number] = 1
        except KeyError:
            counter[card_number] = 1
            
    for number in counter:
        if counter[number] == 4:
            poker = True
            break
    
    return poker

def check_trio(cards):
    counter = {}
    trio = False 
    
    for card in cards:
        card_number = card[:-1]
        try:
            if counter[card_number]:
                counter[card_number] += 1
            else:
                counter[card_number] = 1
        except KeyError:
            counter[card_number] = 1
            
    for number in counter:
        if counter[number] == 3:
            trio = True
            break
    
    return trio

def check_two_pairs(cards): 
    counter = {}
    amount = 0
    two_pairs = False 
    
    for card in cards:
        card_number = card[:-1]
        try:
            if counter[card_number]:
                counter[card_number] += 1
            else:
                counter[card_number] = 1
        except KeyError:
            counter[card_number] = 1
            
    for number in counter:
        if counter[number] == 2:
            amount += 1
            
    if amount == 2:
        two_pairs = True
    
    return two_pairs

def check_pair(cards): 
    counter = {}
    amount = 0
    pair = False 
    
    for card in cards:
        card_number = card[:-1]
        try:
            if counter[card_number]:
                counter[card_number] += 1
            else:
                counter[card_number] = 1
        except KeyError:
            counter[card_number] = 1
            
    for number in counter:
        if counter[number] == 2:
            amount += 1
        
    if amount == 1:
        pair = True
    
    return pair

poker_hand(["10c", "Jc", "Qc", "Ac", "Kc"]) #Royal Flush
poker_hand(["3c", "5c", "Qe", "9c", "Ao"]) #Carta Alta
poker_hand(["10e", "10p", "8o", "10o", "10c"]) #Poker
poker_hand(["4c", "9e", "2e", "2o", "Ao"]) #Par
poker_hand(["10e", "9e", "8e", "6e", "7e"]) #Straight Flush
poker_hand(["10p", "9p", "9e", "10e", "9c"]) #Full House 
poker_hand(["8c", "2c", "8e", "3e", "3p"]) #Dois Pares
poker_hand(["Jc", "9c", "7c", "5c", "2c"]) #Flush
poker_hand(["Ap", "Qp", "Ae", "Ac", "2o"]) #Trio
poker_hand(["Ao", "Ko", "Qo", "Jo", "9o"]) #Flush
poker_hand(["10c", "Jc", "Qe", "Ke", "Ap"]) #Sequência
poker_hand(["3c", "8c", "2e", "3e", "3o"]) #Trio
poker_hand(["4c", "Ap", "4e", "4o", "4p"]) #Poker
poker_hand(["3c", "8c", "2e", "3e", "2o"]) #Dois Pares
poker_hand(["8c", "8e", "Ae", "Qc", "Kc"]) #Par
poker_hand(["8c", "8e", "Ae", "Qc", "Kc"]) #Par