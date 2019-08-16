# import pyperclip
# import re
# import shelve
# patt = re.compile("\W (\w{1,50}) ?\w{1,50}")
# patt1 = re.compile("\w(\w{1,50}) ?\w{1,50}")
# name = pyperclip.paste()
# name = name.split('\n')
# states = []
# capitals = []
# quiz = []
# for i in name:
#     states.append(patt1.search(i).group())
#     temp = patt.search(i).group()
#     capitals.append(temp[2:])
#     quiz.append(patt1.search(i).group() + " : " + temp[2:])
import shelve
import random


def show(a):
    print("What is the capital of " + a + " \t\t Enter 'q' to quit")


def answers(a, b, c, d):
    numd = random.sample(range(4), 4)
    arr = [1,2,3,4]

    arr[numd[0]] = a
    arr[numd[1]] = b
    arr[numd[2]] = c
    arr[numd[3]] = d
    for i in range(4):
        print(i+1 , ". " , arr[i])
    return numd[0] + 1


file = shelve.open('saved')
states = file['states']
capitals = file['answers']


while True:
    num = random.randint(0, 28)
    nums = random.sample(range(29), 3)
    show(states[num])
    ani = answers(capitals[num], capitals[nums[0]], capitals[nums[1]], capitals[nums[2]])

    ans = input()

    try:
        if ans == 'q':
            break
        elif int(ans) == ani:
            print("That's the right answer")
        else:
            print("Opps! wrong try another one")
    except ValueError:
        print("Take it easy man/woman..")






























