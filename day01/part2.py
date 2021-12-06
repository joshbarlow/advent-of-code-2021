with open('input.txt') as file:
    array = file.readlines()

incrementCounter = 0
hasPrevious = False

for inputLine in range(len(array)-2):

    if hasPrevious:

        current = (int(array[inputLine]) + int(array[inputLine+1]) + int(array[inputLine+2]))
        previous = (int(array[inputLine-1]) + int(array[inputLine]) + int(array[inputLine+1]))

        if (current > previous):
            incrementCounter += 1

    hasPrevious = True

print(incrementCounter)