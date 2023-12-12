def getPos(maps):
    pos = []
    for i in range(len(maps)):
        for idx, value in enumerate(maps[i]):
                if value == "#":
                    pos.append([i, idx])
    return pos

def getSum(pos, col, row, expan = 1):
    sum = 0
    expan -= 1
    lsSum = []
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            xa = pos[i][1]
            xb = pos[j][1]
            ya = pos[i][0]
            yb = pos[j][0]
            for c in col:
                if c < pos[i][1]:
                    xa += expan
                if c < pos[j][1]:
                    xb += expan
            for r in row:
                if r < pos[i][0]:
                    ya += expan
                if r < pos[j][0]:
                    yb += expan
            sum += abs(xa - xb) + abs(ya - yb)

    return sum

if __name__ == "__main__":
    maps = []
    path = []
    row = []
    col = []
    i = 0
    pos = []
    with open('input11', 'r') as f:
        lsLine = list(f.readline().strip())
        col = [False] * len(lsLine)
        maps.append(lsLine)
        try:
            lsLine.index("#")
            for idx, value in enumerate(lsLine):
                if value == "#":
                    col[idx] = True
                    pos.append([i, idx])
            row.append(True)
        except ValueError:
            row.append(False)
            
        for line in f:
            i+=1
            lsLine = list(line.strip())
            maps.append(lsLine)
            try:
                lsLine.index("#")
                for idx, value in enumerate(lsLine):
                    if value == "#":
                        col[idx] = True
                        pos.append([i, idx])
                row.append(True)
            except ValueError:
                row.append(False)
        indC = []
        indR = []
        for i in range(len(col)):
            if not col[i]:
                indC.append(i)
        for i in range(len(row)):
            if not row[i]:
                indR.append(i)

        sum = getSum(pos, indC, indR, 1000000)
        print(sum)