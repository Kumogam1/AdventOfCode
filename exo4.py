sum = 0
nbCard = dict()
with open('input4', 'r') as f:
    for line in f:
        """part 1
        win, hand = line.split(':')[1].split('|')
        setWin = set(win.strip().split())
        setHand = set(hand.strip().split())
        
        card = len(setWin.intersection(setHand))-1
        if card >= 0:
            sum += pow(2, card)
        """
        cardId, cardls = line.split(':')
        cardId = int(cardId.strip().split()[1])
        win, hand = cardls.split('|')
        setWin = set(win.strip().split())
        setHand = set(hand.strip().split())
        card = len(setWin.intersection(setHand))

        for i in range(card):
            nbCard[cardId + i + 1] = nbCard.setdefault(cardId + i + 1, 0) + nbCard.setdefault(cardId, 0) + 1
        sum += 1 + nbCard.setdefault(cardId, 0)
        #print(sum)
print(sum)