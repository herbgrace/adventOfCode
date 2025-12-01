def firstChallenge():
    current = 50
    count = 0
    with open('Day1/input.txt', 'r') as f:
        content = f.readlines()
        for line in content:
            turn = int(line[1:])
            if(line.startswith('R')):
                # print("Turning right ", turn)
                current += turn
            else:
                # print("Turning left ", turn)
                current -= turn
            if (current % 100 == 0):
                count += 1
        print("The password is: ", count)

def secondChallenge():
    current = 50
    count = 0
    with open('Day1/input.txt', 'r') as f:
        content = f.readlines()
        for line in content:
            startingNum = current
            turn = int(line[1:])
            if (line.startswith('L')):
                turn = -turn

            # print("Starting Number: ", startingNum)
            # print("Number Turned: ", turn)
            current += turn

            # print("Ending Number: ", current)
            # print("Starting Count: ", count)
            count += abs(int(current/100))
            if (current <= 0 and startingNum != 0):
                count += 1
            # print("Ending Count: ", count)
            current %= 100
            # print("")

        print("The REAL password is: ", count)

firstChallenge()
secondChallenge()