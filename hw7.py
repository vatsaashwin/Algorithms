def editDistance(a, b):
    m = len(a)
    n = len(b)

    #initialisating matrices
    dist = [[0 for j in range(0, n + 1)] for i in range(0, m + 1)]
    action = [[0 for j in range(0, n + 1)] for i in range(0, m + 1)]
    # print(dist)
    # print(action)

    for i in range(1, m + 1):
        dist[i][0] = i
        action[i][0] = 'D'

    for j in range(1, n + 1):
        dist[0][j] = j
        action[0][j] = 'I'

    # print("After Initialisation:")
    # print(dist)
    # print(action)

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            diff = 1
            act = 'R'

            # Case 1: When letters are same, do nothing.
            if a[i - 1] == b[j - 1]:
                diff = 0
                act = '_'

            # store minimum to compare later and add actions to action dict
            minimum = dist[i - 1][j - 1] + diff

            if dist[i][j - 1] + 1 < minimum:
                minimum = dist[i][j - 1] + 1
                act = 'I'

            if dist[i - 1][j] + 1 < minimum:
                minimum = dist[i - 1][j] + 1
                act = 'D'

            action[i][j] = act
            dist[i][j] = minimum

    # print("After DP:")
    # print(dist)
    # print(action)
    output = ""
    # Backtrace to get the output string
    output = backTrace(m, n, action)

    return (dist[m][n], output)


def backTrace(m, n, action):
    output = ""

    while m > 0 or n > 0:
        output = output + action[m][n]
        # If the action was Delete, backtrace to prev value at (m-1, n)
        if action[m][n] == 'D':
            m -= 1

        # If the action was Insert, backtrace to prev value at (m, n-1)
        elif action[m][n] == 'I':
            n -= 1

        # If the action was Replace or _ ('Do Nothing'), backtrace to prev value at (m-1, n-1)
        else:
            m -= 1
            n -= 1
    # return the reverse string
    return output[::-1]


# print(editDistance('BABBLE', 'APPLE'))
