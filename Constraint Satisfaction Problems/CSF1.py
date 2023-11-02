def check(node, color, sol, graph):
    for neighbor in graph[node]:
        if sol[neighbor] == color:
            return False
    return True


def get_node(csp):
    for node in csp:
        if csp[node] == -1:
            return node


def isGoal(assign):
    return all(val != -1 for val in assign.values())


def backtrack(graph, colors):
    assign = {node: -1 for node in graph}
    sol = rec_backtrack(assign, graph, colors)
    return sol


def rec_backtrack(assign, graph, colors):
    if isGoal(assign):
        return assign

    var = get_node(assign)
    for index, color in enumerate(colors):
        if check(var, index, assign, graph):
            assign[var] = index
            result = rec_backtrack(assign, graph, colors)
            if result:
                return result
            assign[var] = -1

    return None


graph = {
    'a':['b','c'],
    'b':['a','c','d','e'],
    'c':['b','e'],
    'd':['a','b','e'],
    'e':['b','c','d'],
}

colors = ["Red", "Green", "Blue"]
sol = backtrack(graph, colors)

if sol:
    for node in sol:
        print('Node :', node, '\tColor :', colors[sol[node]])
else:
    print("No solution exists.")
