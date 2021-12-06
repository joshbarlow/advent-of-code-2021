with open('input.txt') as file:
    array = file.readlines()

incrementCounter = 0
hasPrevious = False

for inputLine in range(len(array)):

    if hasPrevious:
        if (int(array[inputLine]) > int(array[inputLine-1])):
            incrementCounter += 1

    hasPrevious = True

print(incrementCounter)