filename = 'inputday1.txt'

def readInput():
    with open(filename, 'r') as f:
        data = f.readlines()
        for i in range(len(data)):
            data[i] = int(data[i].replace('\n', ''))
    return data

data = readInput()

def findNumbers(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            test = data[i] + data[j]
            if test == 2020:
                return data[i] * data[j]
    return None

def findNumbers2(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                test2 = data[i] + data[j] + data[k]
                if test2 == 2020:
                    return data[i] * data[j] * data[k]
    return None

print(findNumbers(data))
print(findNumbers2(data))
