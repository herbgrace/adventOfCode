def firstChallenge():
    current = 50
    count = 0
    with open('Day1/input.txt', 'r') as f:
        content = f.readlines()
        for line in content:
            # Determine how far/direction to turn
            turn = int(line[1:])
            if(line.startswith('L')):
                turn = -turn

            # Turn the dial
            current += turn

            # Increment count if it's on 0
            if (current % 100 == 0):
                count += 1
        print("The password is: ", count)

def secondChallenge():
    current = 50
    count = 0
    with open('Day1/input.txt', 'r') as f:
        content = f.readlines()
        for line in content:
            # Determine how far/direction to turn
            startingNum = current
            turn = int(line[1:])
            if (line.startswith('L')):
                turn = -turn

            # Turn the dial
            current += turn

            # Determine if 0 was crossed, then increment counter if so
            count += abs(int(current/100))
            if (current <= 0 and startingNum != 0):
                count += 1

            # Reset the dial to be in range
            current %= 100

        print("The REAL password is: ", count)

firstChallenge()
secondChallenge()