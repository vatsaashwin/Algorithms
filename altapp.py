import numpy as np

def move(tab_original):
    # Check possible movements
    movements = []
    tab = tab_original
    i = 0
    j = 0
    while 0 not in tab[i]: i += 1
    j = tab[i].index(0)

    if i<2:         #move 0 down 
        # print("Moving Down")
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movements.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i>0:         #move 0 up
        # print("Moving up")
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movements.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j<2:         #move 0 right
        # print("Moving Right")
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movements.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    
    if j>0:         #move 0 left
        # print("Moving Left")
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movements.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movements


def bfs(start,end):
    explore = []
    
    print('Explore: ',explore)
    queue = [[start]]
    print('queue: ',queue)
    while queue:
        i = 0
        print("Entering i ====== ", i)
        path = queue[i]
        print("Path is:",path)
        queue = queue[:i] + queue[i+1:]
        print("updated queue: ", queue )
        final = path[-1]
        print("final:",final)
        if final in explore:
            print("Final is in explore")
            continue
        for movements in move(final):

            if movements in explore:
                print("movements in explore")
                continue
            
            queue.append(path + [movements])
            print(" queue after append: ", queue )
            print("moooooooooooovementssssssss: ",movements)
        explore.append(final)
        print('Explore after append: ',explore)
        if final == end: break
    return path

def ShortestPath(goalS, initS):
    initial = [initS[x:x+3] for x in range(0, len(initS), 3)]
    goal = [goalS[x:x+3] for x in range(0, len(goalS), 3)]
    # print(type(initial))
    # getIndex = initial.index('0')
    # print(getIndex)
    for i in bfs(initial,goal):
        output = []
        # getIndex = [x for x in range(len(i)) if i[x]=='0']
        # print(getIndex)
        print(type(i))
        print(i, end="\n")

initS= [1,2,3,4,5,6,8,7,0] 
goalS = [1,2,3,8,0,4,7,6,5] 

ShortestPath(goalS, initS)
