import os
import random
#from math import *
import math

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
operatorList = [' ', ' ', ' ', ' ']
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
# print(operandList)

for i in range(len(operatorList)):
    operator = operatorDict[random.randint(1, 4)]
    if operator == '**' and operator in operatorList:
        continue
        # break
    else:
        operatorList[i] = operatorDict[random.randint(1, 4)]
print(operatorList)


# # generating mathematical expression
questionString = " "
for i in range(len(operandList)-1):
    questionString = questionString + str(operandList[i]) + operatorList[i]
print(questionString)

questionString = questionString + str(operandList[-1])

print(questionString)


result = eval(questionString)
print(result)
# # Interacting with the User

questionString = questionString.replace('**', '^')
print("Here is your question: ", questionString)


user_input = int(input("Type in your answer: "))

# print(user_input)
if user_input == result:
    print("You get it right..Congrats!!")

else:
    print("The answer is: ", result + " try another time:(")

# print(getUserPoints("Ann"))

# updateUserPoints(True, "Annie", 200)
updateUserPoints(False, "Ann", 185)