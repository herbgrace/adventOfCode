def firstChallenge():
    accessibleCount = 0
    neighbors = 0
    allLines = []
    with open("./Day4/input.txt") as f:
        fileContents = f.readlines()

        #Setup the 2d array
        for line in fileContents:
            line = list(line)
            line.pop()
            allLines.append(line)
        # print(allLines)
        
        #Each Row
        for r in range(len(allLines)):
            #Each column
            for c in range(len(allLines[r])):

                #Current symbol is a roll
                if (allLines[r][c] == "@"):

                    for i in range(8):
                        # print(i)
                        try:       
                            #Hard coded for now, make this more scalable?
                            #Remember that index of -1 is the last because thanks python
                            match i:
                                case 0:
                                    if (r == 0 or c == 0):
                                        continue
                                    # print(allLines[r-1][c-1])
                                    neighbors += 1 if (allLines[r-1][c-1] == "@") else 0
                                case 1:
                                    if (r == 0):
                                        continue
                                    # print(allLines[r-1][c])
                                    neighbors += 1 if (allLines[r-1][c] == "@") else 0
                                case 2:
                                    if (r == 0):
                                        continue
                                    # print(allLines[r-1][c+1])
                                    neighbors += 1 if (allLines[r-1][c+1] == "@") else 0
                                case 3:
                                    if (c == 0):
                                        continue
                                    # print(allLines[r][c-1])
                                    neighbors += 1 if (allLines[r][c-1] == "@") else 0
                                case 4:
                                    # print(allLines[r][c+1])
                                    neighbors += 1 if (allLines[r][c+1] == "@") else 0
                                case 5:
                                    if (c == 0):
                                        continue
                                    # print(allLines[r+1][c-1])
                                    neighbors += 1 if (allLines[r+1][c-1] == "@") else 0
                                case 6:
                                    # print(allLines[r+1][c])
                                    neighbors += 1 if (allLines[r+1][c] == "@") else 0
                                case 7:
                                    # print(allLines[r+1][c+1])
                                    neighbors += 1 if (allLines[r+1][c+1] == "@") else 0
                        except IndexError:
                            continue
                    # print("Item at row " + str(r+1) + " and column " + str(c+1) + " has " + str(neighbors) + " neighbors")
                    if (neighbors < 4):
                        accessibleCount += 1
                neighbors = 0
    print("Accessible Count: ", accessibleCount)

def secondChallenge():
    accessibleCount = 0
    iterationCount = 0
    neighbors = 0
    allLines = []
    with open("./Day4/input.txt") as f:
        fileContents = f.readlines()

        #Setup the 2d array
        for line in fileContents:
            line = list(line)
            line.pop()
            allLines.append(line)
        # print(allLines)
        
        while True:
        #Each Row
            for r in range(len(allLines)):
                #Each column
                for c in range(len(allLines[r])):

                    #Current symbol is a roll
                    if (allLines[r][c] == "@"):

                        for i in range(8):
                            # print(i)
                            try:       
                                #Hard coded for now, make this more scalable?
                                #Remember that index of -1 is the last because thanks python
                                match i:
                                    case 0:
                                        if (r == 0 or c == 0):
                                            continue
                                        # print(allLines[r-1][c-1])
                                        neighbors += 1 if (allLines[r-1][c-1] == "@") else 0
                                    case 1:
                                        if (r == 0):
                                            continue
                                        # print(allLines[r-1][c])
                                        neighbors += 1 if (allLines[r-1][c] == "@") else 0
                                    case 2:
                                        if (r == 0):
                                            continue
                                        # print(allLines[r-1][c+1])
                                        neighbors += 1 if (allLines[r-1][c+1] == "@") else 0
                                    case 3:
                                        if (c == 0):
                                            continue
                                        # print(allLines[r][c-1])
                                        neighbors += 1 if (allLines[r][c-1] == "@") else 0
                                    case 4:
                                        # print(allLines[r][c+1])
                                        neighbors += 1 if (allLines[r][c+1] == "@") else 0
                                    case 5:
                                        if (c == 0):
                                            continue
                                        # print(allLines[r+1][c-1])
                                        neighbors += 1 if (allLines[r+1][c-1] == "@") else 0
                                    case 6:
                                        # print(allLines[r+1][c])
                                        neighbors += 1 if (allLines[r+1][c] == "@") else 0
                                    case 7:
                                        # print(allLines[r+1][c+1])
                                        neighbors += 1 if (allLines[r+1][c+1] == "@") else 0
                            except IndexError:
                                continue
                        # print("Item at row " + str(r+1) + " and column " + str(c+1) + " has " + str(neighbors) + " neighbors")
                        if (neighbors < 4):
                            iterationCount += 1
                            allLines[r][c] = "."
                    neighbors = 0
            if iterationCount == 0:
                break
            accessibleCount += iterationCount
            iterationCount = 0
    print("REAL Accessible Count: ", accessibleCount)

firstChallenge()
secondChallenge()

#This is definitely a terrible way of doing this, but it works...