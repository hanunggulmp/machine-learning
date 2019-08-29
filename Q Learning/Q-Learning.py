import numpy as np
import random

map = np.loadtxt('DataTugasML3.txt')
#print(map)

reward_list = [[-99,-3,-2,-99],[-99,-5,-1,-1],[-99,-1,-1,-3],[-99,-3,-4,-5],[-99,-3,-2,-1],[-99,-5,-5,-3],[-99,-5,-3,-3],[-99,-1,-5,-5],[-99,100,-5,-5],[-99,-99,-5,-1],
               [-1,-1,-3,-99],[-3,-1,-4,-2],[-5,-4,-4,-1],[-1,-2,-1,-1],[-3,-5,-3,-4],[-3,-3,-5,-2],[-5,-5,-5,-5],[-5,-5,-4,-3],[-1,-5,-3,-5],[100,-99,-5,-5],
               [-2,-4,-3,-99],[-1,-4,-5,-3],[-1,-1,-2,-4],[-4,-3,-5,-4],[-2,-5,-1,-1],[-5,-5,-4,-3],[-3,-4,-5,-5],[-5,-3,-1,-5],[-5,-5,-3,-4],[-5,-99,-4,-3],
               [-3,-5,-4,-99],[-4,-2,-3,-3],[-4,-5,-3,-5],[-1,-1,-2,-2],[-3,-4,-1,-5],[-5,-5,-1,-1],[-5,-1,-1,-4],[-4,-3,-4,-5],[-3,-4,-3,-1],[-5,-99,-4,-3],
               [-3,-3,-4,-99],[-5,-3,-2,-4],[-2,-2,-5,-3],[-5,-1,-2,-3],[-1,-1,-4,-2],[-4,-1,-5,-1],[-5,-4,-1,-1],[-1,-3,-2,-1],[-3,-4,-2,-4],[-4,-99,-4,-3],
               [-4,-2,-4,-99],[-3,-5,-3,-4],[-3,-2,-2,-2],[-2,-4,-3,-5],[-1,-5,-1,-2],[-1,-1,-3,-4],[-1,-2,-4,-5],[-4,-2,-3,-1],[-3,-4,-1,-2],[-4,-99,-3,-2],
               [-4,-3,-4,-99],[-2,-2,-2,-4],[-5,-3,-5,-3],[-2,-1,-4,-2],[-4,-3,-1,-3],[-5,-4,-4,-1],[-1,-3,-5,-3],[-2,-1,-5,-4],[-2,-3,-2,-3],[-4,-99,-4,-1],
               [-4,-2,-2,-99],[-3,-5,-1,-4],[-2,-4,-1,-2],[-3,-1,-4,-5],[-1,-4,-1,-4],[-3,-5,-3,-1],[-4,-5,-5,-4],[-3,-2,-1,-5],[-1,-4,-4,-5],[-3,-99,-1,-2],
               [-4,-1,-5,-99],[-2,-1,-3,-2],[-5,-4,-1,-1],[-4,-1,-2,-1],[-1,-3,-4,-4],[-4,-5,-3,-1],[-5,-1,-5,-3],[-5,-4,-2,-5],[-2,-1,-2,-1],[-4,-99,-2,-4],
               [-2,-3,-99,-99],[-1,-1,-99,-5],[-1,-2,-99,-3],[-4,-4,-99,-1],[-1,-3,-99,-2],[-3,-5,-99,-4],[-5,-2,-99,-3],[-1,-2,-99,-5],[-4,-2,-99,-2],[-1,-99,-99,-2]]

R = np.array(reward_list)
#print('\n',R)

Q = np.zeros((100,4))
gamma = 0.9
eps = 0

print("Agent is Learning. Please wait....")

#LOOPING FOR EPISODE HERE....
while eps !=10000:
    c = 0
    #Initialzie current state
    a = random.randint(0,99)
    #LOOPING TILL REACH THE GOAL
    while c !=9:
        #Random the all among possible action from current state
        #random selection: actions
        b = random.randint(0,3)
        #Re-Random if agent got null value
        if R[a][b] == -99:
            while R[a][b] == -99:
                b = random.randint(0, 3)
                #print(b)
                #print('hasil random ulang',R[a][b])
        reward = R[a][b]
        #print('finalya got this',reward)

        #action that taken by agent
        if b == 0:
            c = a - 10
            act = 'Up'
        elif b == 1:
            c = a + 1
            act = 'Right'
        elif b == 2:
            c = a + 10
            act = 'Down'
        else:
            c = a - 1
            act = 'Left'

        #print('Q sblum di update',Q[a][b])
        Q[a][b] = reward + gamma * max(Q[c])
        #print('Q ssudah di update',Q[a][b],'\n')

        a=c
    eps +=1

print("\nFINAL Q-Result")
print(Q)


#MAIN
#Now, It's time for agent to find the fastest path

#Initial value
state = 90
j = Q[state]
goal = 9
path= []
direction = []
cost = []

while state != goal:
    location = np.argmax(j)
    print(Q[state])
    print('state =',state)
    print('location =',location)

    if Q[state][location] != 0:
        if location == 0:
            nextState = state - 10
            print('up')
            if nextState not in path:
                state = nextState
                j = Q[state]
                path.append(state)
                direction.append('Up')
                cost.append(Q[state][location])
            else:
                Q[state][location] = -99

        elif location == 1:
            nextState = state + 1
            print('ryt')
            if nextState not in path:
                state = nextState
                j = Q[state]
                path.append(state)
                direction.append('Right')
                cost.append(Q[state][location])
            else:
                Q[state][location] = -99

        elif location == 2:
            nextState = state + 10
            print('bot')
            if nextState not in path:
                state = nextState
                j = Q[state]
                path.append(state)
                direction.append('Down')
                cost.append(Q[state][location])
            else:
                Q[state][location] = -99

        elif location == 3:
            nextState = state - 1
            print('lft')
            if nextState not in path:
                state = nextState
                j = Q[state]
                path.append(state)
                direction.append('Left')
                cost.append(Q[state][location])
            else:
                Q[state][location] = -99

    else:
        Q[state][location] = -99

print('The path that crossed by agent',path)
print('The value of cost is with sum %d'%(sum(cost)))
print('Dircetion',direction)