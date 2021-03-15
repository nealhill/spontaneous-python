"""
 Problem:
     Given an input list of numbers, print out each number in
     order of their frequency, highest frequency first.
 """

"""
inputList=[4, 6, 5, 4, 10, 3, 4, 10, 6, 4]

sorted inputList=[3, 4, 4, 4, 4, 5, 6, 6, 10, 10]

Number =  3 total=1
Number =  4 total=4
Number =  5 total=1
Number =  6 total=2
Number = 10 total=2

Frequency numbers:
{1: [3, 5], 4: [4], 2: [6, 10]}

Ordered:
[4, 6, 10, 3, 5]
"""

inputList = [4, 6, 5, 4, 10, 3, 4, 10, 6, 4]
print("inputList={}\n".format(inputList))

inputList.sort()
print("sorted inputList={}\n".format(inputList))

currentNumber = None
runningCount = 0
frequentNumbers = {}  # This is a dictionary of lists {'k': v} where k=total count and v=numbers with that total count

for n in inputList:
    # First time processing running counts
    if currentNumber is None:
        currentNumber = n
        runningCount = 1

    # If we are now process a new number, save the previous running count
    elif currentNumber != n:
        print("Number = {:2d} total={}".format(currentNumber, runningCount))
        # Save running count:
        # If saving to a running count that already exists, then add this new number list
        if runningCount in frequentNumbers:
            runningCountList = frequentNumbers[runningCount]
            runningCountList.append(currentNumber)
            frequentNumbers[runningCount] = runningCountList
        # Else saving to a running count for the first time, then this new number list is the first in the list
        else:
            frequentNumbers[runningCount] = [currentNumber]
        # Start new running count for new number
        currentNumber = n
        runningCount = 1

    # Else (we are still processing the same number) continue counting
    else:
        runningCount = runningCount + 1

# We're at the and, save this final running count
# If saving to a running count that already exists, then add this new number list
if runningCount in frequentNumbers:
    runningCountList = frequentNumbers[runningCount]
    runningCountList.append(currentNumber)
    frequentNumbers[runningCount] = runningCountList
# Else saving to a running count for the first time, then this new number list is the first in the list
else:
    frequentNumbers[str(runningCount)] = [currentNumber]
print("Number = {:2d} total={}".format(currentNumber, runningCount))

# Now should the frequency dictionary
print("\nFrequency numbers:")
print("{}".format(frequentNumbers))

# Print out the list in reverse order
keys = sorted(frequentNumbers.keys(), reverse=True)
print("\nOrdered:")
orderedFrequent = []
for k in keys:
    for numListItem in frequentNumbers[k]:
        orderedFrequent.append(numListItem)
print(orderedFrequent)