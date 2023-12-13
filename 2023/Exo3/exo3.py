import re

sum = 0
"""part1
indSym = dict()
indNum = []
regSym = re.compile('[^0-9|.]')
regNum = re.compile('[0-9|]+')
"""
indSym = []
indNum = dict()
regSym = re.compile('\*')
regNum = re.compile('[0-9|]+')

with open('input3', 'r') as f:    
    i=0
    for line in f:
        line = line.strip()
        res = regSym.finditer(line)
        for match in res:
            indSym.append([i, match.start()])

        res = regNum.finditer(line)
        lsNum = []
        for match in res:
            lsNum.append([int(match.group()), [match.start(), match.end()-1]])    
        
        indNum[i] = lsNum
        
        i+=1

    for s in indSym:
        lsNum = []
        if s[0]-1 in indNum:
            for n in indNum[s[0]-1]:
                if s[1] >= n[1][0]-1 and s[1] <= n[1][1]+1:
                    lsNum.append(n[0])
        
        if s[0] in indNum:    
            for n in indNum[s[0]]:
                if s[1] >= n[1][0]-1 and s[1] <= n[1][1]+1:
                    lsNum.append(n[0])

        if s[0]+1 in indNum:
            for n in indNum[s[0]+1]:
                if s[1] >= n[1][0]-1 and s[1] <= n[1][1]+1:
                    lsNum.append(n[0])
        
        if len(lsNum) == 2:
            sum += lsNum[0] * lsNum[1]

    """part1
    for line in f:
        line = line.strip()
        res = regSym.finditer(line)
        lsSym = []
        for match in res:
            lsSym.append(match.start())
        indSym[i] = lsSym
        res = regNum.finditer(line)
        for match in res:
            indNum.append([i, [match.start(), match.end()-1], int(match.group())])
        i+=1
    
    i-=1
    for n in indNum:
        contact = False

        if n[0]-1 in indSym:
            for s in indSym[n[0]-1]:
                if s >= n[1][0]-1 and s <= n[1][1]+1:
                    sum += n[2]
                    contact = True
                    break
        if not contact:
            if n[0] in indSym:    
                for s in indSym[n[0]]:
                    if s >= n[1][0]-1 and s <= n[1][1]+1:
                        sum += n[2]
                        contact = True
                        break
        if not contact:
            if n[0]+1 in indSym:
                for s in indSym[n[0]+1]:
                    if s >= n[1][0]-1 and s <= n[1][1]+1:
                        sum += n[2]
                        break
    """
print(sum)