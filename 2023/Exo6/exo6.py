total = 1
lsFrame = []

with open('input6', 'r') as f:
    '''part 1
    time = f.readline().split(':')[1].split()
    record = f.readline().split(':')[1].split()
    '''
    time = int(f.readline().split(':')[1].strip().replace(" ", ""))
    record = int(f.readline().split(':')[1].strip().replace(" ", ""))

    print(time)
    print(record)

    '''part1    
    for i in range(len(time)):
        frame = 0
        limit = int(time[i])
        rec = int(record[i])
        for t in range(limit):
            dist = t * (limit - t)
            if dist > rec:
                frame += 1
        total *= frame
    '''
    frame = 0
    
    for t in range(time):
        dist = t * (time - t)
        if dist > record:
            frame += 1
    total *= frame

    print(total)