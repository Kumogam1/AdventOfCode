convert = {
    'L':0,
    'R':1
}
direction = dict()

with open('input8', 'r') as f:
    pattern = list(f.readline().strip())
    pattern = [convert[i] for i in pattern]
    f.readline()
    curPlace = []
    for line in f:
        place, path = line.split('=')
        left, right = (path.split(','))
        place = place.strip()
        direction[place] = [left.strip()[1:], right.strip()[:-1]]
        #part 2
        if place[-1] == 'A':
            curPlace.append(place)
    
    step = 0
    size = len(pattern)
    nbStart = len(curPlace)
    print(curPlace)
    #curPlace = 'AAA'
    while True:
        arrived = True
        chose = pattern[step % size]
        step += 1
        '''part1
        curPlace = direction[curPlace][chose]
        if curPlace == 'ZZZ':
            break
        '''
        for i in range(nbStart):
            newPlace = direction[curPlace[i]][chose]
            curPlace[i] = newPlace
            if newPlace[-1] != 'Z':
                arrived = False
        if arrived:
            break

        if step % 100000000 == 0:
            print(step)
    print(step)