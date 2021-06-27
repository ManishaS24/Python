import os
import random

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

# print(getUserPoints("Ann"))

# updateUserPoints(True, "Annie", 200)
updateUserPoints(False, "Ann", 185)