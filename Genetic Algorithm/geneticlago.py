import random


def mutate(board1, board2):
    b1 = list(board1)
    b2 = list(board2)

    x = random.randint(0, 7)
    b1[x], b2[x] = b2[x], b1[x]
    y = random.randint(0, 7)
    b1[y] = str(int(y)+1)

    return (''.join(b1), ''.join(b2))


def crossover(board1, board2):
    x = random.randint(1, 7)
    b1 = list(board1)
    b2 = list(board2)
    b1[0:x], b2[0:x] = b2[0:x], b1[0:x]
    return (''.join(b1), ''.join(b2))


def fitness(board):
    attacks = 0
    for i in range(8):
        for j in range(i+1, 8):
            if board[i] == board[j] or abs(int(board[i]) - int(board[j])) == j-i:
                attacks += 1

    return attacks


def geneticAlgo(generations, initialPopulation):

    i = 0
    pq = []
    pq.append((fitness(initialPopulation[0]), initialPopulation[0]))
    pq.append((fitness(initialPopulation[1]), initialPopulation[1]))
    while i < generations:
        f1, b1 = pq.pop(0)
        f2, b2 = pq.pop(0)
        pq.clear()

        if f1 == 0:
            print('\nGoal State :', b1, '\nGeneration :', i+1)
            return
        elif f2 == 0:
            print('\nGoal State :', b2, '\nGeneration :', i+1)
            return

        x1, x2 = crossover(b1, b2)
        x3, x4 = crossover(b2, b1)

        newPopulation = [(x1, x2), (x3, x4), mutate(x1, x2), mutate(x2, x1)]

        for child in newPopulation:
            pq.append((fitness(child[0]), child[0]))
            pq.append((fitness(child[1]), child[1]))

        pq.append((f1, b1))
        pq.append((f2, b2))

        pq.sort(key=lambda x: x[0])

        i += 1

    print('\nMost evolved state :',
          pq[0][1], '\nGeneration :', i, '\nAttacks :', pq[0][0])


# print(fitness("17582463"))

geneticAlgo(1000, ["32752411", "24748552"])

geneticAlgo(1000, ["17581234", "56782463"])
