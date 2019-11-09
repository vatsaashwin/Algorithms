from collections import deque
import time

class State:
    def __init__(self, state, parent, dirn, depth, cost):
        self.state = state
        self.parent = parent
        self.dirn = dirn
        self.depth = depth
        self.cost = cost
        if self.state:
            self.path = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.path == other.path
    
    def __lt__(self, other):
        return self.path < other.path

def bfs(start_state, brd_length, brd_side, nodes_expanded, max_size,
        max_depth, goal_state):

    global goal_V

    visited, queue = set(), deque([State(start_state, None, None, 0, 0)])

    while queue:

        node = queue.popleft()

        visited.add(node.path)

        if node.state == goal_state:
            goal_V = node
            return queue

        neighbors = recur(node, brd_length, brd_side, nodes_expanded)

        for neighbor in neighbors:
            if neighbor.path not in visited:
                queue.append(neighbor)
                visited.add(neighbor.path)

                if neighbor.depth > max_depth: max_depth += 1

        if len(queue) > max_size: max_size = len(queue)


def recur(node, brd_length, brd_side, nodes_expanded):
    
    nodes_expanded += 1
    
    neighbors = list()
    
    neighbors.append(
        State(tileShift(node.state, 1, brd_length, brd_side), node, 1,
              node.depth + 1, node.cost + 1))
    neighbors.append(
        State(tileShift(node.state, 2, brd_length, brd_side), node, 2,
              node.depth + 1, node.cost + 1))
    neighbors.append(
        State(tileShift(node.state, 3, brd_length, brd_side), node, 3,
              node.depth + 1, node.cost + 1))
    neighbors.append(
        State(tileShift(node.state, 4, brd_length, brd_side), node, 4,
              node.depth + 1, node.cost + 1))

    nodes = [neighbor for neighbor in neighbors if neighbor.state]    
    return nodes


def tileShift(currentState, pos, brd_length, brd_side):

    new_state = currentState[:]
    index = new_state.index(0)

    # Move Down
    if pos == 1:  
        if index not in range(0, brd_side):
            temp = new_state[index - brd_side]
            new_state[index - brd_side] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    # Move Up
    if pos == 2:  
        if index not in range(brd_length - brd_side, brd_length):
            temp = new_state[index + brd_side]
            new_state[index + brd_side] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    # Move Right
    if pos == 3:  
        if index not in range(0, brd_length, brd_side):
            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    # Move Left
    if pos == 4:  
        if index not in range(brd_side - 1, brd_length, brd_side):
            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

def findFootprint(initial_state):
    output = []
    current_node = goal_V

    while initial_state != current_node.state:
        if current_node.dirn == 1: output.append('D')
        elif current_node.dirn == 2: output.append('U')
        elif current_node.dirn == 3: output.append('R')
        else: output.append('L')
        current_node = current_node.parent
        rev = output[::-1]
        fullStr = ''.join(rev)
    return fullStr


def initialize(initial_state, path, configuration, goal_state):
    nodes_expanded = 0
    max_size = 0
    max_depth = 0
    brd_length = 0
    brd_side = 0
    initial_state = configuration
    brd_length = len(initial_state)
    brd_side = int(brd_length**0.5)

    bfs(initial_state, brd_length, brd_side, nodes_expanded,
        max_size, max_depth, goal_state)

    path = findFootprint(initial_state)
    return path


def ShortestPath(goalS, initS):
    output = []
    for x in initS:
        initial_state = x
        configuration = initial_state
        goal_state = goalS
        path = list()
        initial_state = list()
        path = initialize(initial_state, path, configuration, goal_state)
        output.append(path)

    return output

#ShortestPath([1,2,3,8,0,4,7,6,5], [[2, 4, 7, 1, 5, 3, 0, 8, 6], [0, 1, 6, 8, 4, 2, 5, 7, 3]])
print(ShortestPath([1,2,3,8,0,4,7,6,5], [[2, 4, 7, 1, 5, 3, 0, 8, 6], [0, 1, 6, 8, 4, 2, 5, 7, 3]]))


