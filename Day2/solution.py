import re
# ^(\d+)\1(?!\1)$ - still matches leading 0's
# (\d+)-(\d+) - get each category

def firstChallenge():
    rangeRegex = "(\\d+)-(\\d+)"
    invalidRegex = "^(\\d+)\\1(?!\\1)$"
    sum = 0
    with open('Day2/input.txt', 'r') as f:
        # Get all of the ranges
        matches = re.findall(rangeRegex, f.readline())

        # Go through each start/end pair
        for range in matches:

            # Go through each number from start to end
            count = int(range[0])
            while (count <= int(range[1])):

                # Check if the ID is invalid, then add its number if so
                invalid = re.search(invalidRegex, str(count))
                if (invalid != None):
                    sum += count
                count += 1
            
        print("Final Count: ", sum)

def secondChallenge():
    rangeRegex = "(\\d+)-(\\d+)"

    # This is the only change from challenge 1, just changed the regex
    invalidRegex = "^(\\d+)\\1+$"
    sum = 0
    with open('Day2/input.txt', 'r') as f:
        # Get all of the ranges
        matches = re.findall(rangeRegex, f.readline())

        # Go through each start/end pair
        for range in matches:

            # Go through each number from start to end
            count = int(range[0])
            while (count <= int(range[1])):

                # Check if the ID is invalid, then add its number if so
                invalid = re.search(invalidRegex, str(count))
                if (invalid != None):
                    sum += count
                count += 1
            
        print("REAL Final Count: ", sum)

firstChallenge()
secondChallenge()