sum = 0
Cardvalue = {
    '2':'01',
    '3':'02',
    '4':'03',
    '5':'04',
    '6':'05',
    '7':'06',
    '8':'07',
    '9':'08',
    'T':'09',
    'J':'10',
    'Q':'11',
    'K':'12',
    'A':'13'
}
Cardvalue2 = {
    'J':'01',
    '2':'02',
    '3':'03',
    '4':'04',
    '5':'05',
    '6':'06',
    '7':'07',
    '8':'08',
    '9':'09',
    'T':'10',
    'Q':'11',
    'K':'12',
    'A':'13'
}

five = dict()
four = dict()
full = dict()
three = dict()
two = dict()
pair = dict()
other = dict()

lsPos = [other, pair, two, three, full, four, five]

def assignHand(hand, bid):
    nbDiff = len(set(list(hand)))
    
    if nbDiff == 1:
        five[hand] = bid
    elif nbDiff == 4:
        pair[hand] = bid
    elif nbDiff == 5:
        other[hand] = bid
    else:
        handDict = dict()
        for c in hand:
            handDict[c] = handDict.setdefault(c, 0) + 1
        nbDiff = set(handDict.values())
        if nbDiff == {1,3}:
            three[hand] = bid
        elif nbDiff == {2,3}:
            full[hand] = bid
        elif nbDiff == {4,1}:
            four[hand] = bid
        else:
            two[hand] = bid

def assignHand2(hand, bid):
    nbDiff = len(set(list(hand)))
    if nbDiff == 1:
        five[hand] = bid
    elif nbDiff == 4:
        if hand.count('J'):
            three[hand] = bid
        else:
            pair[hand] = bid
    elif nbDiff == 5:
        if hand.count('J') == 1:
            pair[hand] = bid
        else:
            other[hand] = bid
    else:
        handDict = dict()
        for c in hand:
            handDict[c] = handDict.setdefault(c, 0) + 1
        nbDiff = set(handDict.values())
        if nbDiff == {1,3}:
            if hand.count('J'):
                four[hand] = bid
            else:
                three[hand] = bid
        elif nbDiff == {2,3}:
            if hand.count('J')==1:
                four[hand] = bid
            elif hand.count('J')>1:
                five[hand] = bid
            else:
                full[hand] = bid
        elif nbDiff == {4,1}:
            if hand.count('J'):
                five[hand] = bid
            else:
                four[hand] = bid
        else:
            if hand.count('J')==1:
                full[hand] = bid
            elif hand.count('J')>1:
                four[hand] = bid
            else:
                two[hand] = bid
            

with open('input7', 'r') as f:
    for line in f:
        hand, bid = line.strip().split()
        assignHand2(hand, bid)
    
    offset = 0
    for p in lsPos:
        lsValue = dict()
        if p:
            for h in p:
                value = ""
                for c in h:
                    value += Cardvalue2[c]
                lsValue[int(value)] = p[h]
            k = list(lsValue.keys())
            k.sort()
            j=1
            for i in k:
                sum += int(lsValue[i]) * (j+offset)
                j+=1
            offset += len(p)

    print(sum)