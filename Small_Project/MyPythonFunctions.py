import os
import random
from math import *

def getUserPoints(user_name):
    contents = []
    try:
        input_file = open('userScores.txt', 'r')
        for line in input_file:
            contents.append(line.split(','))
            # print(contents)
        for i in range(len(contents)):
            if user_name in contents[i]:
                input_file.close()
                value = contents[i][1].split('\n')[0]
                return value
            else:
                input_file.close()
                return -1
    except IOError as e:
        print(e)
        open('userScores.txt', 'w')

        # print(line)
    # print(contents)

def updateUserPoints(new_user, user_name, score):
    if new_user:
        f = open('userScores.txt', 'a')
        f.write('\n' + user_name + ', ' + str(score))
        f.close()
    else:
        nf = open('userScores.tmp', 'w')
        f = open('userScores.txt', 'r')

        for line in f:
            if user_name in line.split(','):
                nf.write(user_name + ', ' + str(score) + '\n')
            else:
                nf.write(line)
        nf.close()
        f.close()

operandList = [0, 0, 0, 0, 0]
operatorList = [' ', ' ', ' ', ' ', ' ']
operatorDict = {1: '+',
2: '-',
3: '*',
4: '**'
}

# operandList[0] = random.randint(1,9)
# operandList[1] = random.randint(1, 9)
# operandList[2] = random.randint(1, 9)
# operandList[3] = random.randint(1, 9)
# operandList[4] = random.randint(1, 9)

for i in range(len(operandList)):
    operandList[i] = random.randint(1, 9)

for i in range(len(operatorList)):
    operator = operatorDict[random.randint(1, 4)]
    if operator == '**' and operator in operatorList:
        continue
    else:
        operatorList[i] = operatorDict[random.randint(1, 4)]

# # generating mathematical expression
questionString = ''
for i in range(len(operandList)):
    questionString = operandList[i] + operatorList[i]

result = eval(questionString)

questionString = questionString.replace('**', '^')

user_input = int(input("Type in your answer: "))




# print(getUserPoints("Ann"))

# updateUserPoints(True, "Annie", 200)
updateUserPoints(False, "Ann", 185)