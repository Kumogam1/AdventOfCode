sum = 0

with open('input9', 'r') as f:
    for line in f:
        report = line.strip().split()
        report = [int(i) for i in report]
        listList = [report]
        t = 0
        while True:
            diff = list()
            for i in range(1, len(listList[t])):
                diff.append(listList[t][i] - listList[t][i-1])
            listList.append(diff)
            p = True
            for d in diff:
                if d != 0:
                    p = False
            if p:
                diff.append(0)
                break
            t+=1
        
        '''part1
        for i in range(len(listList) - 2, -1, -1):
            listList[i].append(listList[i][-1]+listList[i+1][-1])
        sum += listList[0][-1]
        '''
        for i in range(len(listList) - 2, -1, -1):
            listList[i].insert(0, listList[i][0]-listList[i+1][0])
        sum += listList[0][0]
        
print(sum)