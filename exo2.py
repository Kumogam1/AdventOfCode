Dict={
    'red':12,
    'green':13,
    'blue':14
}
sum = 0

with open('input', 'r') as f:
    for line in f:
        DictMax={
            'red':0,
            'green':0,
            'blue':0
        }
        gameId, tirage = line.split(':')
        gameId = gameId[5:]
        tirage = tirage.split(';')
        for t in tirage:
            #possible = True
            cube = t.split(',')
            for c in cube:
                val, color = c.strip().split()
                if int(val) > DictMax[color]:
                    DictMax[color] = int(val)

        """part 1
                if Dict[color] < int(val):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum += int(gameId)
        """
        mult = DictMax['red'] * DictMax['green'] * DictMax['blue']
        sum += mult
print(sum)