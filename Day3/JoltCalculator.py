def firstChallenge():
    count = 0
    with open('Day3/input.txt', 'r') as f:
        content = f.readlines()
        for line in content:
            # Split into an array and get rid of the newline character
            numbers = list(line)
            numbers.pop()

            # Max is always going to be part of the solution, whether first or second
            largestNumber = max(numbers)
            largestIndex = numbers.index(largestNumber)

            # Set to 0 instead of deleting so that the index doesn't get messed up
            numbers[largestIndex] = '0'

            # Find the 2nd largest number & its index
            secondNumber = max(numbers)
            secondIndex = numbers.index(secondNumber)

            # Special case where the 2nd number isn't always the 2nd largest
            # Only happens when the largest number isn't at the end of the array
            if ((secondIndex < largestIndex) and largestIndex != (len(numbers) - 1)):
                secondNumber = max(numbers[largestIndex:])
                count += ((int(largestNumber) * 10) + int(secondNumber))
                continue


            if (largestIndex < secondIndex):
                count += ((int(largestNumber) * 10) + int(secondNumber))
            else:
                count += ((int(secondNumber) * 10) + int(largestNumber))
        print("Final Answer: ", count)

def secondChallenge():
    count = 0
    with open('Day3/input.txt', 'r') as f:
        content = f.readlines()
        for line in content:
            # Split into an array and get rid of the newline character
            numbers = list(line)
            numbers.pop()

            #Find the largest numbers from right to left? 

firstChallenge()
secondChallenge